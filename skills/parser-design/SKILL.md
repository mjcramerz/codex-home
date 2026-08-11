---
name: parser-design
description: Design and refactor parsers, tokenizers, grammars, AST transforms, and syntax-error handling with explicit contracts and bounded input handling. Use when the user asks about parsing, grammar changes, query languages, or text-to-structure conversion.
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
  default-prompt: Act as the "PARSER-Design" specialist for "Design parsers, grammars, and AST transforms safely". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Define the input grammar and failure cases before changing parsing code.
2) Keep tokenization, parsing, and validation responsibilities separated.
3) Add positive and negative-path fixtures for malformed input, not just happy paths.

## Agent orchestration
- Confirm ownership, validation scope, and whether another skill or plugin should be combined before editing.
- Delegate only bounded scouting or independent verification work.

## Validation and testing
- Run the narrowest syntax, parser, or unit checks that prove the change.
- Explicitly call out skipped checks and why they remain out of scope.

## Outputs
- Minimal, reviewable edits aligned to the skill contract.
- Concrete validation commands and residual risks.

## References
- [Lark parser](https://lark-parser.readthedocs.io/)
- [Tree-sitter](https://tree-sitter.github.io/tree-sitter/)
- [Python re module](https://docs.python.org/3/library/re.html)
