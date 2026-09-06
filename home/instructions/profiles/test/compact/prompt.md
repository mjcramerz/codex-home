# Test Context Checkpoint

Create a reproducible handoff for the next testing agent. Preserve the behavior
contract, test evidence, and the narrowest remaining validation.

Output Markdown with these exact sections:

## Behavior Under Test
- User outcome, acceptance criteria, affected component, and in-scope behavior.
- Applicable instructions, environment, fixtures, data boundaries, and user
  changes that must remain untouched.

## Test Evidence
- Commands run, test names, setup steps, results, failures, and relevant
  sanitized output.
- Separate passing evidence, failing evidence, flaky behavior, and unrun checks.

## Changes and Decisions
- Files inspected or changed, test strategy, fixtures or mocks, and the reason
  each check proves or fails to prove the behavior.

## Next Validation
1. Exact next test or setup command.
2. Follow-up implementation or regression check if needed.
3. Blockers, missing dependencies, and residual confidence gaps.

Rules:
- Do not claim coverage, determinism, or a pass without direct evidence.
- Preserve failure details that make reproduction possible.
- Exclude secrets, private data, and private reasoning.
