# Debugging Context Checkpoint

Create a reproducible handoff for the next debugging agent. The summary must
make the current failure and best next experiment immediately actionable.

Output Markdown with these exact sections:

## Bug Contract
- Expected behavior, observed behavior, impact, affected versions or paths,
  and the smallest known reproduction.
- Active instructions, repository constraints, environment details, and any
  user changes that must be preserved.

## Evidence
- Commands run, inputs, outputs, stack traces, logs, and instrumentation
  results needed to reproduce the issue.
- Clearly distinguish confirmed facts, hypotheses, and disproven theories.

## Investigation
- Files inspected or changed, relevant code paths, decisions, and why each
  experiment did or did not reduce uncertainty.
- Tests run and their precise status.

## Next Experiment
1. The next smallest discriminating check, including command or file.
2. Follow-up fix and validation steps if the hypothesis is confirmed.
3. Remaining blockers, environmental gaps, and risks.

Rules:
- Preserve exact error text and versions when they are material.
- Do not replace evidence with a narrative or claim a root cause without proof.
- Exclude secrets and private reasoning.
