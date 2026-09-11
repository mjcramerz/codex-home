# Plan the authorized change

Use this template only when a multi-step task benefits from an explicit plan. Replace placeholders with the actual task; do not create a plan file when the user forbids new files.

## Objective

State the requested outcome and observable acceptance criteria. Separate requirements from assumptions.

## Boundaries

Name the allowed files, systems and operations. Record excluded changes, existing work to preserve, and required approval for destructive or externally visible actions.

## Evidence

Identify the entrypoints, callers, configuration layers and primary references you actually inspected. List unresolved facts without presenting guesses as findings.

## Execution

Order the smallest implementation steps by dependency. Assign ownership only when real delegation is available and authorized. Keep the critical path and final integration under one coordinator.

## Checks and recovery

Choose existing checks that prove the changed contract. Inspect command side effects and prerequisites. Define recovery for stateful changes and state any prohibited or unavailable checks.

## Completion

Record completed edits, exact check results, unresolved risks and the next concrete action. Do not mark unexecuted work complete or promise a later result without a real scheduling capability.
