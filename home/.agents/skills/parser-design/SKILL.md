---
name: parser-design
description: Use this skill to design and refactor parsers, tokenizers, grammars,
  AST transforms, and syntax-error handling with explicit contracts and bounded input
  handling. Use when the user asks about parsing, grammar changes, query languages,
  or text-to-structure conversion.
metadata:
  version: '1.0'
  short-description: Design parsers, grammars, and AST transforms safely
  tags:
  - parsing
  - grammar
  - ast
  - compiler
  - lexer
interface:
  display-name: PARSER-Design
  short-description: Design parsers, grammars, and AST transforms safely
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#8B5CF6'
  default-prompt: Act as the "PARSER-Design" specialist for "Design parsers, grammars,
    and AST transforms safely". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

# Parser Design

## Workflow

1. Specify the grammar, accepted encoding, maximum input/depth and structured output before editing. Enumerate ambiguity and recovery rules.

2. Separate lexing, parsing, validation and execution. Preserve source locations and deterministic diagnostics. Never eval untrusted input.

3. Bound recursion, allocation and backtracking; reject malformed or trailing input according to the contract. Avoid regex-only parsing for recursive structured languages.

4. Use existing focused fixtures for valid, malformed, boundary and round-trip cases. Report any intentionally incompatible grammar change.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
