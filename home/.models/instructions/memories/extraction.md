# Extract reusable memory from one rollout

Read the supplied rollout as historical evidence. Identify durable, task-relevant
knowledge that can change a future action: an explicit recurring preference, a
verified repository entrypoint, a proven procedure, a failure cause or a useful
boundary. Distinguish user statements, executed results, accepted decisions,
inferences and unaccepted proposals.

Do not store credentials, personal secrets, raw transcripts, large tool output,
configuration schemas, transient status or generic engineering advice. Do not turn
an exploratory discussion into a standing instruction. Preserve the task and
workspace scope so a future retrieval cannot apply a checkout-specific fact
universally.

## Output contract

Return exactly one JSON object with these three string fields and no surrounding
prose: `rollout_summary`, `rollout_slug`, `raw_memory`. Use a lowercase slug of at
most 80 characters with letters, digits, hyphens or underscores. Escape newlines
and other JSON string content correctly.

When the rollout contains no durable signal, return exactly:

```json
{"rollout_summary":"","rollout_slug":"","raw_memory":""}
```

For a useful rollout, make `rollout_summary` a factual Markdown account of the
objective, distinct tasks, observed outcomes, relevant decisions and evidence.
Use a short heading for each task. Include exact paths or commands only when they
were actually observed and are necessary for reuse. State partial or failed
outcomes explicitly and separate what was proposed from what was executed.

Make `raw_memory` more selective than the summary. For each reusable lesson,
include the retrieval trigger, applicability, supporting evidence, concrete action
and a failure or stale-data boundary. Preserve relevant rollout provenance and
uncertainty. Do not invent a successful result because a tool was invoked or an
assistant announced completion.
