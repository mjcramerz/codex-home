---
name: notion-meeting-intelligence
description: Prepare meeting materials with Notion context and Codex research; use when gathering
  context, drafting agendas/pre-reads, and tailoring materials to attendees.
metadata:
  version: '1.0'
  short-description: Prep meetings with Notion context and tailored agendas
  tags:
  - notion
  - meetings
  - agenda
  - planning
interface:
  display-name: NOTION-Meeting Intelligence
  short-description: Prep meetings with Notion context and tailored agendas
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32A5CC'
  default-prompt: Act as the "NOTION-Meeting Intelligence" specialist for "Prep meetings with
    Notion context and tailored agendas". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O,
    run the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

# NOTION-Meeting Intelligence

## Use this skill when
- preparing agendas or pre-reads for upcoming meetings in Notion
- converting meeting context into actionable notes, decisions, and follow-ups
- maintaining a consistent meeting artifact pattern across teams


Prep meetings by pulling Notion context, tailoring agendas/pre-reads, and enriching with Codex research.

## Quick start
1) Confirm meeting goal, attendees, date/time, and decisions needed.
2) Gather context: search with `Notion:notion-search`, then fetch with `Notion:notion-fetch` (prior notes, specs, OKRs, decisions).
3) Pick the right template via `reference/template-selection-guide.md` (status, decision, planning, retro, 1:1, brainstorming).
4) Draft agenda/pre-read in Notion with `Notion:notion-create-pages`, embedding source links and owner/timeboxes.
5) Enrich with Codex research (industry insights, benchmarks, risks) and update the page with `Notion:notion-update-page` as plans change.

## Workflow
### 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
1. Add the Notion MCP:
   - `codex mcp add notion --url https://mcp.notion.com/mcp`
2. Enable remote MCP client:
   - Set `[features].rmcp_client = true` in `config.toml` **or** run `codex --enable rmcp_client`
3. Log in with OAuth:
   - `codex mcp login notion`

After successful login, the user will have to restart codex. You should finish your answer and tell them so when they try again they can continue with Step 1.

### 1) Gather inputs
- Ask for objective, desired outcomes/decisions, attendees, duration, date/time, and prior materials.
- Search Notion for relevant docs, past notes, specs, and action items (`Notion:notion-search`), then fetch key pages (`Notion:notion-fetch`).
- Capture blockers/risks and open questions up front.

### 2) Choose format
- Status/update → status template.
- Decision/approval → decision template.
- Planning (sprint/project) → planning template.
- Retro/feedback → retrospective template.
- 1:1 → one-on-one template.
- Ideation → brainstorming template.
- Use `reference/template-selection-guide.md` to confirm.

### 3) Build the agenda/pre-read
- Start from the chosen template in `reference/` and adapt sections (context, goals, agenda, owner/time per item, decisions, risks, prep asks).
- Include links to pulled Notion pages and any required pre-reading.
- Assign owners for each agenda item; call out timeboxes and expected outputs.

### 4) Enrich with research
- Add concise Codex research where helpful: market/industry facts, benchmarks, risks, best practices.
- Keep claims cited with source links; separate fact from opinion.

### 5) Finalize and share
- Add next steps and owners for follow-ups.
- If tasks arise, create/link tasks in the relevant Notion database.
- Update the page via `Notion:notion-update-page` when details change; keep a brief changelog if multiple edits.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs

- Actionable steps or artifacts aligned to the skill.
- References to relevant files, commands, or templates.

## References and examples
- `reference/` — template picker and meeting templates (e.g., `template-selection-guide.md`, `status-update-template.md`, `decision-meeting-template.md`, `sprint-planning-template.md`, `one-on-one-template.md`, `retrospective-template.md`, `brainstorming-template.md`).
- `examples/` — end-to-end meeting preps (e.g., `executive-review.md`, `project-decision.md`, `sprint-planning.md`, `customer-meeting.md`).
