from __future__ import annotations

import io
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from PIL import Image, ImageDraw, ImageFont, ImageOps

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.design_book_common import (
    assemble_markdown,
    build_page_documents,
    derive_index,
    dump_yaml,
    load_yaml,
    repository_root,
    sha256_bytes,
    sha256_file,
    strip_inline_markdown,
)


PAPER = "#F7F5F0"
RAISED = "#FBFAF6"
INK = "#1B1B19"
SECONDARY = "#535457"
CORAL = "#C96157"
DATA_BLUE = "#4C6A8A"
LINE = "#85847F"


@dataclass(frozen=True)
class FontPaths:
    regular: Path
    bold: Path
    mono: Path


def _first_existing(candidates: list[str]) -> Path:
    for candidate in candidates:
        path = Path(candidate)
        if path.is_file():
            return path
    raise RuntimeError("no Ukrainian-capable local font fallback is available")


def find_font_paths() -> FontPaths:
    regular = _first_existing(
        [
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
        ]
    )
    bold = _first_existing(
        [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
            str(regular),
        ]
    )
    mono = _first_existing(
        [
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf",
            str(regular),
        ]
    )
    return FontPaths(regular=regular, bold=bold, mono=mono)


def _font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size=size)


def _contrast_ratio(foreground: str, background: str) -> float:
    def luminance(value: str) -> float:
        channels = [int(value[index : index + 2], 16) / 255 for index in (1, 3, 5)]
        linear = [channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4 for channel in channels]
        return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

    first, second = sorted([luminance(foreground), luminance(background)], reverse=True)
    return (first + 0.05) / (second + 0.05)


def _wrap(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, width: int) -> list[str]:
    if not text:
        return [""]
    words = text.split()
    if not words:
        return [""]
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if draw.textlength(candidate, font=font) <= width:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def _markdown_blocks(markdown: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    in_code = False
    for raw in markdown.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not line:
            blocks.append(("space", ""))
            continue
        if in_code:
            blocks.append(("code", line))
        elif line.startswith("# "):
            continue
        elif line.startswith("## "):
            blocks.append(("h2", strip_inline_markdown(line[3:])))
        elif re.match(r"^\|?\s*:?-{3,}", line):
            continue
        elif line.startswith("|"):
            cells = [strip_inline_markdown(cell) for cell in line.strip("|").split("|")]
            blocks.append(("table", "  ·  ".join(cell for cell in cells if cell)))
        elif re.match(r"^\d+\.\s+", line):
            blocks.append(("bullet", strip_inline_markdown(line)))
        elif line.startswith(("- ", "* ")):
            blocks.append(("bullet", "• " + strip_inline_markdown(line[2:])))
        else:
            blocks.append(("body", strip_inline_markdown(line)))
    compact: list[tuple[str, str]] = []
    for item in blocks:
        if item[0] == "space" and (not compact or compact[-1][0] == "space"):
            continue
        compact.append(item)
    return compact


def _layout_blocks(
    draw: ImageDraw.ImageDraw,
    blocks: list[tuple[str, str]],
    font_paths: FontPaths,
    body_size: int,
    width: int,
) -> tuple[list[tuple[str, str, ImageFont.FreeTypeFont, int]], int]:
    fonts = {
        "body": _font(font_paths.regular, body_size),
        "bullet": _font(font_paths.regular, body_size),
        "table": _font(font_paths.regular, max(16, body_size - 2)),
        "h2": _font(font_paths.bold, body_size + 7),
        "code": _font(font_paths.mono, max(14, body_size - 5)),
    }
    leading = {
        "body": int(body_size * 1.38),
        "bullet": int(body_size * 1.34),
        "table": int(body_size * 1.25),
        "h2": int((body_size + 7) * 1.28),
        "code": int(max(14, body_size - 5) * 1.30),
        "space": max(7, body_size // 3),
    }
    output: list[tuple[str, str, ImageFont.FreeTypeFont, int]] = []
    height = 0
    for kind, text in blocks:
        if kind == "space":
            height += leading[kind]
            output.append((kind, "", fonts["body"], leading[kind]))
            continue
        font = fonts[kind]
        prefix_indent = 28 if kind == "bullet" else 0
        wrapped = _wrap(draw, text, font, width - prefix_indent)
        for index, line in enumerate(wrapped):
            rendered = ("   " + line) if prefix_indent and index else line
            output.append((kind, rendered, font, leading[kind]))
            height += leading[kind]
        if kind == "h2":
            height += 4
    return output, height


def _font_missing_chars(font: ImageFont.FreeTypeFont, text: str) -> list[str]:
    missing = []
    for char in sorted(set(text)):
        if char.isspace() or char in {"\u200b", "\ufe0f"}:
            continue
        try:
            if font.getmask(char).getbbox() is None:
                missing.append(char)
        except Exception:
            missing.append(char)
    return missing


def _place_evidence_image(
    image: Image.Image,
    draw: ImageDraw.ImageDraw,
    document: dict[str, Any],
    repository: Path,
    font_paths: FontPaths,
) -> None:
    relative = document.get("evidence_image")
    if not relative:
        return
    source = Image.open(repository / relative).convert("RGB")
    source.thumbnail((420, 300), Image.Resampling.LANCZOS)
    x = image.width - source.width - 92
    y = image.height - source.height - 120
    draw.rounded_rectangle((x - 14, y - 14, x + source.width + 14, y + source.height + 40), radius=12, fill=RAISED, outline=LINE, width=2)
    image.paste(source, (x, y))
    caption = _font(font_paths.regular, 15)
    draw.text(
        (x, y + source.height + 10),
        "accepted evidence · source SHA-256 pinned",
        font=caption,
        fill=SECONDARY,
    )


def render_page(
    document: dict[str, Any],
    size: tuple[int, int],
    font_paths: FontPaths,
    repository: Path,
) -> tuple[Image.Image, bool, list[str], int]:
    width, height = size
    image = Image.new("RGB", size, PAPER)
    draw = ImageDraw.Draw(image)
    page_id = document["id"]
    title = document["metadata"]["title_uk"]
    if document["kind"] == "cover":
        draw.rectangle((width - 540, 0, width, height), fill=CORAL)
        draw.rectangle((width - 710, 160, width - 420, 450), fill=INK)
        title_font = _font(font_paths.bold, 74)
        subtitle_font = _font(font_paths.bold, 38)
        body_font = _font(font_paths.regular, 24)
        draw.text((110, 130), "CSDL", font=_font(font_paths.bold, 126), fill=INK)
        draw.multiline_text((116, 315), "COOKBOOK AND\nDESIGN BOOK v1.0", font=title_font, fill=INK, spacing=4)
        plain_lines = [line for line in document["plain_text"].splitlines()[1:] if line]
        y = 610
        for line in plain_lines[:5]:
            if not line:
                y += 14
                continue
            active = subtitle_font if y < 700 else body_font
            for wrapped in _wrap(draw, line, active, 850):
                draw.text((118, y), wrapped, font=active, fill=INK)
                y += int(active.size * 1.3)
        draw.text((118, height - 90), "UK editorial · EN canonical vocabulary · A4 landscape", font=_font(font_paths.regular, 19), fill=SECONDARY)
        missing = _font_missing_chars(body_font, document["plain_text"])
        return image, y > height - 74, missing, body_font.size

    draw.rectangle((0, 0, 18, height), fill=CORAL)
    draw.rectangle((80, 72, 102, 94), fill=CORAL)
    draw.text((118, 69), document["section"].upper(), font=_font(font_paths.bold, 17), fill=SECONDARY)
    draw.text((width - 145, 69), page_id, font=_font(font_paths.bold, 20), fill=INK)
    title_font = _font(font_paths.bold, 58 if len(title) < 38 else 50)
    draw.text((108, 112), title, font=title_font, fill=INK)
    draw.line((108, 194, width - 94, 194), fill=LINE, width=2)

    has_evidence = bool(document.get("evidence_image"))
    content_width = width - 220 - (480 if has_evidence else 0)
    blocks = _markdown_blocks(document["expanded_markdown"])
    selected: list[tuple[str, str, ImageFont.FreeTypeFont, int]] = []
    block_height = 0
    selected_size = 26
    max_height = height - 292
    for body_size in range(26, 17, -1):
        selected, block_height = _layout_blocks(draw, blocks, font_paths, body_size, content_width)
        selected_size = body_size
        if block_height <= max_height:
            break
    y = 225
    for kind, line, active_font, leading in selected:
        if kind == "space":
            y += leading
            continue
        color = DATA_BLUE if kind == "code" else INK
        if kind == "h2":
            color = INK
        draw.text((108, y), line, font=active_font, fill=color)
        y += leading
        if kind == "h2":
            y += 4

    _place_evidence_image(image, draw, document, repository, font_paths)
    draw.text((108, height - 58), "CSDL Cookbook and Design Book v1.0", font=_font(font_paths.regular, 15), fill=SECONDARY)
    draw.line((width - 310, height - 50, width - 98, height - 50), fill=CORAL, width=4)
    body_font = _font(font_paths.regular, selected_size)
    missing = _font_missing_chars(body_font, document["plain_text"])
    overflow = block_height > max_height or y > height - 82
    return image, overflow, missing, selected_size


def _save_png(image: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, format="PNG", optimize=False, compress_level=9)


def _jpeg_bytes(image: Image.Image) -> bytes:
    output = io.BytesIO()
    image.save(output, format="JPEG", quality=94, subsampling=0, optimize=False, progressive=False)
    return output.getvalue()


def _utf16_hex(value: str) -> str:
    return (b"\xfe\xff" + value.encode("utf-16-be")).hex().upper()


class _PdfObjects:
    def __init__(self) -> None:
        self.objects: list[bytes] = [b""]

    def add(self, value: bytes = b"") -> int:
        self.objects.append(value)
        return len(self.objects) - 1

    def set(self, identifier: int, value: bytes) -> None:
        self.objects[identifier] = value


def _stream(dictionary: str, data: bytes) -> bytes:
    return f"<< {dictionary} /Length {len(data)} >>\nstream\n".encode("ascii") + data + b"\nendstream"


def _to_unicode_stream(code_map: dict[str, int]) -> bytes:
    reverse = sorted(((code, char) for char, code in code_map.items()))
    lines = [
        "/CIDInit /ProcSet findresource begin",
        "12 dict begin",
        "begincmap",
        "/CIDSystemInfo << /Registry (CSDL) /Ordering (Unicode) /Supplement 0 >> def",
        "/CMapName /CSDLUnicode def",
        "/CMapType 2 def",
        "1 begincodespacerange",
        "<01> <FF>",
        "endcodespacerange",
    ]
    for offset in range(0, len(reverse), 100):
        chunk = reverse[offset : offset + 100]
        lines.append(f"{len(chunk)} beginbfchar")
        for code, char in chunk:
            lines.append(f"<{code:02X}> <{char.encode('utf-16-be').hex().upper()}>")
        lines.append("endbfchar")
    lines.extend(["endcmap", "CMapName currentdict /CMap defineresource pop", "end", "end"])
    return "\n".join(lines).encode("ascii")


def build_pdf(images: list[Image.Image], page_texts: list[str], output: Path, page_size: tuple[float, float]) -> None:
    characters = sorted(set("".join(page_texts)) - {"\n", "\r", "\t"})
    if len(characters) > 254:
        raise ValueError(f"publication text layer uses {len(characters)} unique characters; maximum is 254")
    code_map = {char: index + 1 for index, char in enumerate(characters)}
    objects = _PdfObjects()
    catalog_id = objects.add()
    pages_id = objects.add()
    blank_charproc_id = objects.add(_stream("", b"0 0 d0"))
    to_unicode_id = objects.add(_stream("", _to_unicode_stream(code_map)))
    differences = " ".join(f"/g{code:03d}" for code in range(1, len(characters) + 1))
    char_procs = " ".join(f"/g{code:03d} {blank_charproc_id} 0 R" for code in range(1, len(characters) + 1))
    widths = " ".join("500" for _ in characters)
    font = (
        f"<< /Type /Font /Subtype /Type3 /Name /F1 /FontBBox [0 0 0 0] "
        f"/FontMatrix [0.001 0 0 0.001 0 0] /CharProcs << {char_procs} >> "
        f"/Encoding << /Type /Encoding /Differences [1 {differences}] >> "
        f"/FirstChar 1 /LastChar {len(characters)} /Widths [{widths}] "
        f"/Resources << >> /ToUnicode {to_unicode_id} 0 R >>"
    ).encode("ascii")
    font_id = objects.add(font)
    page_ids: list[int] = []
    media_width, media_height = page_size
    for image, text in zip(images, page_texts, strict=True):
        jpeg = _jpeg_bytes(image)
        image_id = objects.add(
            _stream(
                f"/Type /XObject /Subtype /Image /Width {image.width} /Height {image.height} "
                "/ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode",
                jpeg,
            )
        )
        commands = [f"q {media_width:.4f} 0 0 {media_height:.4f} 0 0 cm /Im1 Do Q", "BT /F1 8 Tf 3 Tr"]
        line_y = media_height - 18
        for line in text.splitlines():
            encoded = bytes(code_map[char] for char in line if char in code_map).hex().upper()
            commands.append(f"1 0 0 1 18 {line_y:.2f} Tm <{encoded}> Tj")
            line_y -= 9
        commands.append("ET")
        content_id = objects.add(_stream("", "\n".join(commands).encode("ascii")))
        page_id = objects.add(
            (
                f"<< /Type /Page /Parent {pages_id} 0 R /MediaBox [0 0 {media_width:.4f} {media_height:.4f}] "
                f"/Tabs /S /Resources << /XObject << /Im1 {image_id} 0 R >> /Font << /F1 {font_id} 0 R >> >> "
                f"/Contents {content_id} 0 R >>"
            ).encode("ascii")
        )
        page_ids.append(page_id)
    objects.set(pages_id, f"<< /Type /Pages /Count {len(page_ids)} /Kids [{' '.join(f'{item} 0 R' for item in page_ids)}] >>".encode("ascii"))
    objects.set(
        catalog_id,
        f"<< /Type /Catalog /Pages {pages_id} 0 R /Lang (uk-UA) /PageLayout /SinglePage /ViewerPreferences << /DisplayDocTitle true >> >>".encode("ascii"),
    )
    info_id = objects.add(
        (
            f"<< /Title <{_utf16_hex('CSDL Cookbook and Design Book v1.0')}> "
            f"/Author (CSDL) /Subject <{_utf16_hex('Bilingual design language guide')}> "
            "/Creator (tools/build_design_book.py) /Producer (CSDL deterministic PDF writer) "
            "/CreationDate (D:20260718000000Z) /ModDate (D:20260718000000Z) >>"
        ).encode("ascii")
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = bytearray(b"%PDF-1.7\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for identifier, value in enumerate(objects.objects[1:], 1):
        offsets.append(len(payload))
        payload.extend(f"{identifier} 0 obj\n".encode("ascii"))
        payload.extend(value)
        payload.extend(b"\nendobj\n")
    xref = len(payload)
    payload.extend(f"xref\n0 {len(objects.objects)}\n".encode("ascii"))
    payload.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        payload.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    digest = sha256_bytes("".join(page_texts).encode("utf-8"))[:32].upper()
    payload.extend(
        (
            f"trailer\n<< /Size {len(objects.objects)} /Root {catalog_id} 0 R /Info {info_id} 0 R "
            f"/ID [<{digest}><{digest}>] >>\nstartxref\n{xref}\n%%EOF\n"
        ).encode("ascii")
    )
    output.write_bytes(payload)


def _build_contact_sheet(images: list[Image.Image], output: Path, font_paths: FontPaths) -> None:
    width, height = 3840, 2160
    sheet = Image.new("RGB", (width, height), INK)
    draw = ImageDraw.Draw(sheet)
    columns, rows = 8, 4
    margin_x, margin_y, gap = 64, 86, 18
    cell_width = (width - margin_x * 2 - gap * (columns - 1)) // columns
    cell_height = (height - margin_y * 2 - gap * (rows - 1)) // rows
    label_font = _font(font_paths.bold, 18)
    for index, page in enumerate(images):
        row, column = divmod(index, columns)
        thumb = page.copy()
        thumb.thumbnail((cell_width, cell_height - 28), Image.Resampling.LANCZOS)
        x = margin_x + column * (cell_width + gap) + (cell_width - thumb.width) // 2
        y = margin_y + row * (cell_height + gap) + 26
        sheet.paste(thumb, (x, y))
        draw.text((x, y - 24), f"{index + 1:02d}", font=label_font, fill=PAPER)
    _save_png(sheet, output)


def _verify_rasters(repository: Path, inventory: dict[str, Any]) -> tuple[list[str], list[dict[str, str]]]:
    mismatches: list[str] = []
    verified: list[dict[str, str]] = []
    for item in inventory["files"]:
        path = repository / item["path"]
        actual = sha256_file(path) if path.is_file() else "missing"
        if actual != item["sha256"]:
            mismatches.append(item["path"])
        verified.append({"path": item["path"], "sha256": actual})
    return mismatches, verified


def build_design_book(book_root: Path) -> list[Path]:
    book_root = book_root.resolve()
    repository = repository_root(book_root)
    manifest = load_yaml(book_root / "manifest.yaml")
    documents = build_page_documents(book_root)
    generated = book_root / "generated"
    output_root = book_root / "output"
    generated.mkdir(parents=True, exist_ok=True)
    output_root.mkdir(parents=True, exist_ok=True)

    assembled_path = generated / "csdl-cookbook-design-book-v1.0.md"
    index_path = generated / "index.yaml"
    assembled_path.write_text(assemble_markdown(book_root, documents), encoding="utf-8")
    index_path.write_text(dump_yaml(derive_index(book_root, documents)), encoding="utf-8")

    format_contract = manifest["publication"]["format"]
    size = (format_contract["render_width_px"], format_contract["render_height_px"])
    font_paths = find_font_paths()
    images: list[Image.Image] = []
    overflow_pages: list[str] = []
    missing_glyph_pages: list[str] = []
    render_sizes: dict[str, int] = {}
    outputs: list[Path] = [assembled_path, index_path]
    for document in documents:
        image, overflow, missing, selected_size = render_page(document, size, font_paths, repository)
        images.append(image)
        render_sizes[document["id"]] = selected_size
        if overflow:
            overflow_pages.append(document["id"])
        if missing:
            missing_glyph_pages.append(document["id"])
        page_path = output_root / "pages" / f"{int(document['id']):03d}.png"
        grayscale_path = output_root / "grayscale" / f"{int(document['id']):03d}.png"
        _save_png(image, page_path)
        _save_png(ImageOps.grayscale(image).convert("RGB"), grayscale_path)
        outputs.extend([page_path, grayscale_path])

    page_texts = [document["plain_text"] for document in documents]
    pdf_path = output_root / "pdf/csdl-cookbook-design-book-v1.0.pdf"
    build_pdf(
        images,
        page_texts,
        pdf_path,
        (format_contract["pdf_width_pt"], format_contract["pdf_height_pt"]),
    )
    contact_sheet = output_root / "contact-sheet.png"
    _build_contact_sheet(images, contact_sheet, font_paths)
    extracted_text = output_root / "extracted-text.txt"
    extracted_text.write_text(
        "\n\n".join(f"PAGE {document['id']}\n{document['plain_text'].rstrip()}" for document in documents) + "\n",
        encoding="utf-8",
    )
    outputs.extend([pdf_path, contact_sheet, extracted_text])

    inventory = load_yaml(repository / manifest["publication"]["accepted_raster_inventory"])
    raster_mismatches, _ = _verify_rasters(repository, inventory)
    evidence_images = [
        {"page": document["id"], "path": document["evidence_image"], "sha256": sha256_file(repository / document["evidence_image"])}
        for document in documents
        if document.get("evidence_image")
    ]
    contrast_checks = {
        "text": {"foreground": INK, "background": PAPER, "ratio": round(_contrast_ratio(INK, PAPER), 6), "minimum": 4.5},
        "secondary_text": {"foreground": SECONDARY, "background": PAPER, "ratio": round(_contrast_ratio(SECONDARY, PAPER), 6), "minimum": 4.5},
        "non_text_signal": {"foreground": CORAL, "background": PAPER, "ratio": round(_contrast_ratio(CORAL, PAPER), 6), "minimum": 3.0},
    }
    for check in contrast_checks.values():
        check["passes"] = check["ratio"] >= check["minimum"]
    report = {
        "publication": manifest["publication"]["id"],
        "version": manifest["publication"]["version"],
        "page_count": len(documents),
        "format": format_contract["name"],
        "deterministic": True,
        "fixed_metadata_date": "2026-07-18T00:00:00Z",
        "font": {
            "regular_path": str(font_paths.regular),
            "regular_sha256": sha256_file(font_paths.regular),
            "bold_path": str(font_paths.bold),
            "bold_sha256": sha256_file(font_paths.bold),
            "mono_path": str(font_paths.mono),
            "mono_sha256": sha256_file(font_paths.mono),
            "boundary": "local build fallback; not a global licensed-font lock",
        },
        "overflow_pages": overflow_pages,
        "missing_glyph_pages": missing_glyph_pages,
        "minimum_body_size_px": min(render_sizes.values()),
        "render_body_sizes_px": render_sizes,
        "contrast_checks": contrast_checks,
        "reading_order": [document["id"] for document in documents],
        "text_layer_sha256": sha256_file(extracted_text),
        "pdf_sha256": sha256_file(pdf_path),
        "contact_sheet_sha256": sha256_file(contact_sheet),
        "assembled_markdown_sha256": sha256_file(assembled_path),
        "index_sha256": sha256_file(index_path),
        "page_render_sha256": {f"{index + 1:03d}": sha256_bytes(image.tobytes()) for index, image in enumerate(images)},
        "accepted_raster_count": inventory["file_count"],
        "accepted_raster_mismatches": raster_mismatches,
        "embedded_evidence": evidence_images,
        "generated_raster_authority": False,
        "public_release": False,
    }
    report_path = output_root / "build-report.yaml"
    report_path.write_text(dump_yaml(report), encoding="utf-8")
    outputs.append(report_path)
    return outputs


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: build_design_book.py <book-root>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1])
    outputs = build_design_book(root)
    print(f"design book built: 32 pages, {len(outputs)} derived files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
