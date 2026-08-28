---
name: openai-docs
description: Reference official OpenAI developer documentation and cite current guidance for
  APIs and platform features. Use when the user asks how to build with OpenAI products, SDKs,
  models, or API capabilities and needs up-to-date doc-backed answers.
metadata:
  version: '1.0'
  short-description: Reference the official OpenAI Developer docs
  tags:
  - openai-docs
  - openai
  - docs
  - api
  - sdk
interface:
  display-name: OpenAI Docs
  short-description: Reference the official OpenAI Developer docs
  icon-small: assets/openai-small.svg
  icon-large: assets/openai.png
  brand-color: '#10A37F'
  default-prompt: Act as the "OpenAI Docs" specialist for "Reference the official OpenAI Developer
    docs". Deliver focused, deterministic results with minimal, reviewable changes and explicit
    assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks,
    and report concrete actions, evidence, and residual risks.
---


# OpenAI Docs

## Overview

Provide authoritative, current guidance from OpenAI developer docs using the developers.openai.com MCP server. Always prioritize the developer docs MCP tools over web.run for OpenAI-related questions. Only if the MCP server is installed and returns no meaningful results should you fall back to web search.

## Quick start

- Use `mcp__openaiDeveloperDocs__search_openai_docs` to find the most relevant doc pages.
- Use `mcp__openaiDeveloperDocs__fetch_openai_doc` to pull exact sections and quote/paraphrase accurately.
- Use `mcp__openaiDeveloperDocs__list_openai_docs` only when you need to browse or discover pages without a clear query.

## OpenAI product snapshots

1. Apps SDK: Build ChatGPT apps by providing a web component UI and an MCP server that exposes your app's tools to ChatGPT.
2. Responses API: A unified endpoint designed for stateful, multimodal, tool-using interactions in agentic workflows.
3. Chat Completions API: Generate a model response from a list of messages comprising a conversation.
4. Codex: OpenAI's coding agent for software development that can write, understand, review, and debug code.
5. gpt-oss: Open-weight OpenAI reasoning models (gpt-oss-120b and gpt-oss-20b) released under the Apache 2.0 license.
6. Realtime API: Build low-latency, multimodal experiences including natural speech-to-speech conversations.
7. Agents SDK: A toolkit for building agentic apps where a model can use tools and context, hand off to other agents, stream partial results, and keep a full trace.

## If MCP server is missing

If MCP tools fail or no OpenAI docs resources are available:

1. Run the install command yourself: `codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp`
2. If it fails due to permissions/sandboxing, immediately retry the same command with escalated permissions and include a 1-sentence justification for approval. Do not ask the user to run it yet.
3. Only if the escalated attempt fails, ask the user to run the install command.
4. Ask the user to restart Codex.
5. Re-run the doc search/fetch after restart.

## Workflow

1. Clarify the product scope (Codex, OpenAI API, or ChatGPT Apps SDK) and the task.
2. Search docs with a precise query.
3. Fetch the best page and the specific section needed (use `anchor` when possible).
4. Answer with concise guidance and cite the doc source.
5. Provide code snippets only when the docs support them.

## Quality rules

- Treat OpenAI docs as the source of truth; avoid speculation.
- Keep quotes short and within policy limits; prefer paraphrase with citations.
- If multiple pages differ, call out the difference and cite both.
- If docs do not cover the user’s need, say so and offer next steps.

## Tooling notes

- Always use MCP doc tools before any web search for OpenAI-related questions.
- If the MCP server is installed but returns no meaningful results, then use web search as a fallback.
- When falling back to web search, restrict to official OpenAI domains (developers.openai.com, platform.openai.com) and cite sources.

## Agent orchestration

- Confirm the OpenAI product scope and user outcome before searching docs.
- Use focused queries first, then fetch only the most relevant sections.
- If multiple skills apply, state the sequence and keep `openai-docs` focused on sourced documentation guidance.

## Validation and testing

- Validate that each answer is backed by OpenAI docs MCP results or official OpenAI domain sources.
- Keep tool usage bounded: narrow queries, fetch specific sections, and avoid bulk page dumps.
- If docs are missing or conflicting, state that explicitly and provide the exact gap.

## Outputs

- Concise, source-backed implementation guidance.
- Citations for each key claim.
- Clear follow-up actions when documentation does not fully cover the user request.

## References

- OpenAI Developer Docs MCP endpoint: `https://developers.openai.com/mcp`
- OpenAI developer docs: `https://developers.openai.com/`
- OpenAI platform docs: `https://platform.openai.com/docs`
