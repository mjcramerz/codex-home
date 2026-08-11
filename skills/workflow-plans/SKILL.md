---
name: workflow-plans
description: Generate concise execution plans for multi-step or ambiguous engineering tasks
  with milestones, risks, and validation checkpoints. Use when the user asks for a plan, roadmap,
  or phased implementation strategy.
metadata:
  version: '1.0'
  short-description: Generate a plan for a complex task
  tags:
  - plan
  - guide
  - onboarding
interface:
  display-name: WORKFLOW-Plans
  short-description: Generate a plan for a complex task
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CCC132'
  default-prompt: Act as the "WORKFLOW-Plans" specialist for "Generate a plan for a complex
    task". Deliver focused, deterministic results with minimal, reviewable changes and explicit
    assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks,
    and report concrete actions, evidence, and residual risks.
---

# WORKFLOW-Plans

## Overview

Draft structured plans that clarify intent, scope, requirements, action items, testing/validation, and risks.

Optionally, save plans to disk as markdown files with YAML frontmatter and free-form content. When drafting in chat, output only the plan body without frontmatter; add frontmatter only when saving to disk. Save/update actions write to `$CODEX_HOME/plans`, while read/list/template discovery paths use `$CODEX_HOME/plans`.

This skill can also be used to draft codebase or system overviews.

## Core rules

- Resolve the save directory as `$CODEX_HOME/plans`.
- Use `$CODEX_HOME/plans` for read/list/template discovery.
- Create the plans directory if it does not exist.
- Never write to a repo when generating user plans; only read files to understand context.
- Require frontmatter with `name`, `description`, and `metadata` (`version`, `short-description`, `tags`) for on-disk plans.
- When presenting a draft plan in chat, omit frontmatter and start at `# Plan`.
- Enforce naming rules: short, lower-case, hyphen-delimited; filename must equal `<name>.md`.
- If a plan is not found, state it clearly and offer to create one.
- Allow overview-style plans that document flows, architecture, or context without a work checklist.

## Workflow

1. **Find/list**: discover plans by frontmatter summary under `$CODEX_HOME/plans`; confirm if multiple matches exist.
2. **Read/use**: validate frontmatter from `$CODEX_HOME/plans`; present summary and full contents.
3. **Create**: inspect repo read-only; choose plan style (implementation vs overview); draft plan; write to plans directory only.
4. **Update**: load plan; revise content and/or description; preserve frontmatter keys; overwrite the plan file.
5. **Delete**: confirm intent, then remove the plan file if asked.

## Plan discovery

- Prefer workflow-plans skill script `scripts/list_plans.py` for quick summaries from `$CODEX_HOME/plans`.
- Use workflow-plans skill script `scripts/read_plan_frontmatter.py` to validate a specific plan under `$CODEX_HOME/plans`.
- If name mismatches filename or frontmatter is missing fields, call it out and ask whether to fix.
- For plan templates, use `--template` to load from `$CODEX_HOME/plans` (implementation/overview/workflow/skill/framework).
- Avoid `path:` templates that point outside the pack; keep templates under `$CODEX_HOME`.

## Plan creation workflow

1. Scan context quickly: read README.md and obvious docs (`$CODEX_HOME/docs/`, CONTRIBUTING.md, ARCHITECTURE.md); skim likely touched files; identify constraints (language, frameworks, CI/test commands, deployment).
2. Ask follow-ups only if blocked: at most 1-2 questions, prefer multiple-choice. If unsure but not blocked, state assumptions and proceed.
3. Identify scope, constraints, and data model/API implications (or capture existing behavior for an overview).
4. Draft either an ordered implementation plan or a structured overview plan with diagrams/notes as needed.
5. Immediately output the plan body only (no frontmatter), then ask the user if they want to 1. Make changes, 2. Implement it, 3. Save it as per plan.
6. If the user wants to save it, prepend frontmatter and save the plan under the computed save directory using workflow-plans skill script `scripts/create_plan.py` (the script requires `CODEX_HOME` to be an absolute path).

## Plan update workflow

- Re-read the plan and related code/docs before updating.
- Keep the plan name stable unless the user explicitly wants a rename.
- If renaming, update both frontmatter `name` and filename together.

## Scripts (low-freedom helpers)

Create a plan file (body only; frontmatter is written for you). Run from the plan skill directory:

```bash
python scripts/create_plan.py \
  --name codex-rate-limit-overview \
  --description "Scope and update plan for Codex rate limiting" \
  --tags "plan,rate-limit,codex" \
  --body-file /tmp/plan-body.md
```

Read frontmatter summary for a plan (run from the plan skill directory):

```bash
python scripts/read_plan_frontmatter.py $CODEX_HOME/plans/OVERVIEW.md
```

List plan summaries (optional filter; run from the plan skill directory):

```bash
python scripts/list_plans.py --query "rate limit"
```

Create a plan from a framework template (no frontmatter in the template body):

```bash
python scripts/create_plan.py \
  --name codex-new-feature \
  --description "Plan for <feature>" \
  --template framework:plan-feature-delivery
```

## Plan file format

Use one of the structures below for the plan body. When drafting, output only the body (no frontmatter). When saving, prepend this frontmatter:

```markdown
---
name: <plan-name>
description: <1-line summary>
metadata:
  version: "1.0"
  short-description: <short summary>
  tags: [plan, <tag>]
---
```

### Implementation plan body template

```markdown
# Plan

<1-3 sentences: intent, scope, and approach.>

## Requirements
- <Requirement 1>
- <Requirement 2>

## Scope
- In:
- Out:

## Files and entry points
- <File/module/entry point 1>
- <File/module/entry point 2>

## Data model / API changes
- <If applicable, describe schema or contract changes>

## Action items
[ ] <Step 1>
[ ] <Step 2>
[ ] <Step 3>
[ ] <Step 4>
[ ] <Step 5>
[ ] <Step 6>

## Testing and validation
- <Tests, commands, or validation steps>

## Risks and edge cases
- <Risk 1>
- <Risk 2>

## Open questions
- <Question 1>
- <Question 2>
```

### Overview plan body template

```markdown
# Plan

<1-3 sentences: intent and scope of the overview.>

## Overview
<Describe the system, flow, or architecture at a high level.>

## Diagrams
<Include text or Mermaid diagrams if helpful.>

## Key file references
- <File/module/entry point 1>
- <File/module/entry point 2>

## Auth / routing / behavior notes
- <Capture relevant differences (e.g., auth modes, routing paths).>

## Current status
- <What is live today vs pending work, if known.>

## Action items
- None (overview only).

## Testing and validation
- None (overview only).

## Risks and edge cases
- None (overview only).

## Open questions
- None.
```

## Writing guidance

- Start with 1 short paragraph describing intent and approach.
- Keep action items ordered and atomic (discovery -> changes -> tests -> rollout); use verb-first phrasing.
- Scale action item count to complexity (simple: 1-2; complex: up to about 10).
- Include file/entry-point hints and concrete validation steps where useful.
- Always include testing/validation and risks/edge cases in implementation plans; include safe rollout/rollback when relevant.
- Use open questions only when necessary (max 3).
- Avoid vague steps, micro-steps, and code snippets; keep the plan implementation-agnostic.
- For overview plans, keep action items minimal and set non-applicable sections to "None."

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

- Actionable plan body with ordered steps and validation.
- Optional saved plan file under `$CODEX_HOME/plans` with valid frontmatter (save only).

## Examples

- Example request: "Draft a plan for adding rate limits."
- Example output: "Plan with scope, steps, tests, and risks."

## References
- `$CODEX_HOME/plans/OVERVIEW.md`
- workflow-plans skill script `scripts/create_plan.py`
- `$CODEX_HOME/docs/prompt-writing.md`
