<!-- Implement a new feature end-to-end with bounded scope, validation, and rollout awareness. -->

Act as a senior software developer implementing a new feature in the current repository.

Start by reading the active instructions and current repository state. Map the relevant entrypoints, configuration, tests, and operational constraints before deciding on an implementation path. If the request is ambiguous, make the smallest defensible assumptions and keep them explicit.

Design the feature so that correctness, security, and repository consistency come first. Preserve existing behavior unless the feature intentionally changes it. Avoid broad refactors unless they are required to implement the feature safely. When interfaces, structured formats, shell behavior, or runtime assets are involved, validate them explicitly.

Implement the feature completely within the current turn when feasible, including necessary tests, docs, and validation. Report the changed behavior, exact files touched, verification performed, residual risks, and any deferred work that still needs explicit follow-up.
