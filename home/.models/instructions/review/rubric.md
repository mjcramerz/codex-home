# Review the changed behavior

Identify actionable defects introduced by the patch, not stylistic preferences or
pre-existing problems. Trace relevant callers, failure paths, permission boundaries
and configuration. Explain the scenario that makes each finding reachable and
support it with the smallest useful line range in the changed code.

Use P0 only for an immediate, broadly applicable release blocker; use P1 for urgent
correctness or security failures, P2 for ordinary defects, and P3 for low-impact
issues. Do not claim exploitability or a failing test without evidence. Omit a
finding when the suspected issue is not sufficiently supported.

## Output contract

Return one JSON object, without Markdown fences or surrounding prose. Use the
following field names and types; substitute actual values for the example:

```json
{
  "findings": [
    {
      "title": "[P2] Preserve the required input validation",
      "body": "Explain the reachable defect, its impact and the affected code.",
      "confidence_score": 0.9,
      "priority": 2,
      "code_location": {
        "absolute_file_path": "/absolute/path/to/file",
        "line_range": {"start": 10, "end": 12}
      }
    }
  ],
  "overall_correctness": "patch is incorrect",
  "overall_explanation": "Summarize the evidence for the verdict in one to three sentences.",
  "overall_confidence_score": 0.9
}
```

Use an empty `findings` array when no actionable defect is supported. Use exactly
`patch is correct` or `patch is incorrect` for `overall_correctness`. Keep scores
between 0 and 1, priorities between 0 and 3, and line ranges as narrow as possible.
Do not substitute an unsupported claim of live validation for code-review evidence.
