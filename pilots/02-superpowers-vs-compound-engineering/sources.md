# Pilot 02 Sources

**Evidence snapshot:** 2026-07-19

This file separates primary-source facts, user-approved editorial premises, and CSDL synthesis. Visible slides do not present editorial synthesis as a quotation from either project.

## Primary sources

1. **Superpowers repository and current README**  
   <https://github.com/obra/superpowers>  
   Supports automatic skill triggering, the brainstorm/design → plan → execute workflow, red/green TDD, systematic debugging, verification before completion, current installation syntax, current 14-skill inventory, and attribution to Jesse Vincent and Prime Radiant.

2. **Superpowers systematic debugging skill, release v6.1.1**  
   Local evidence: `/Users/vladyslav.ohirenko/.codex/plugins/cache/openai-curated-remote/superpowers/6.1.1/skills/systematic-debugging/SKILL.md`  
   Supports root-cause-first debugging and the instruction to stop and question the architecture after three or more failed fixes.

3. **Superpowers test-driven development skill, release v6.1.1**  
   Local evidence: `/Users/vladyslav.ohirenko/.codex/plugins/cache/openai-curated-remote/superpowers/6.1.1/skills/test-driven-development/SKILL.md`  
   Supports the requirement to observe a failing test before implementation.

4. **Compound Engineering repository and current README, release v3.19.0**  
   <https://github.com/EveryInc/compound-engineering-plugin>  
   Supports the 80% planning/review and 20% execution framing, the current `brainstorm → plan → work → simplify → review → compound` workflow, `docs/solutions/` knowledge capture, current installation syntax, 31 skills, 0 standalone agents, and current maintainers Kieran Klaassen and Trevin Chow.

5. **Compound Engineering: How Every Codes With Agents**  
   <https://every.to/source-code/compound-engineering-how-every-codes-with-agents-af3a1bae-cf9b-458e-8048-c6b4ba860e62>  
   Supports the historical `Plan → Work → Review → Compound → Repeat` core and the statement that the method emerged from building Cora.

6. **Compound Engineering Gets an Upgrade**  
   <https://every.to/guides/compound-engineering-gets-an-upgrade>  
   Supports the evolution from the four-step core to the expanded workflow and identifies Compound as the return arrow that makes later work easier.

## User-approved editorial premises

- Agents can already generate code faster than the intended audience; process is the practical bottleneck.
- A bare agent predictably creates rework, regressions, and debt when it skips planning, tests, or self-verification.
- Superpowers primarily disciplines execution inside the current task.
- Compound Engineering primarily compounds reusable context across tasks.
- The approaches are orthogonal and can be combined.
- For a new solo project, Superpowers is a sensible starting point; for a long-lived product with recurring patterns, Compound Engineering may yield greater return.
- Risks may be summarized as ceremony on small tasks for Superpowers and a wider surface area plus higher multi-agent review token cost for Compound Engineering.

## Time-sensitive snapshot claims

- `14 SKILLS` for Superpowers was counted from the v6.1.1 skill inventory available on 2026-07-19.
- `31 SKILLS · 0 STANDALONE AGENTS` is stated by the Compound Engineering v3.19.0 README available on 2026-07-19.
- These point-in-time values remain in the research record but were removed from Slide 05 at the user's request; re-verify them before any future use.
