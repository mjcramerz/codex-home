package Codex::Hook::Policy;

use strict;
use warnings;

use Exporter qw(import);
use Codex::Hook::Environment qw(stringify_payload_text);
use Codex::Hook::McpTool qw(
  mcp_permission_lines
  mcp_pre_tool_lines
);
use Codex::Hook::ToolProfile qw(tool_group_label tool_group_name);

our @EXPORT_OK = qw(
  compact_system_message
  destructive_command_reason
  permission_request_message
  pre_tool_policy_lines
  subagent_stop_system_message
);

sub destructive_command_reason {
    my (%args) = @_;
    my $tool_name = $args{tool_name} // '';
    my $tool_input = $args{tool_input};
    return undef if $tool_name !~ /(?:\Aexec_command\z|\Aapply_patch\z|\b(?:shell|bash|write)\b)/i;
    my $text = stringify_payload_text(value => $tool_input);
    return undef if !defined $text || !length $text;

    return 'PreToolUse rejected a destructive `git reset --hard` path. Use a non-destructive alternative unless the user explicitly requested that exact operation.'
      if $text =~ /\bgit\s+reset\s+--hard\b/i;
    return 'PreToolUse rejected a destructive `git checkout --` path. Preserve user changes unless they explicitly asked to discard them.'
      if $text =~ /\bgit\s+checkout\s+--\b/i;
    return 'PreToolUse rejected a destructive `git clean -fd` path. Preserve untracked files unless the user explicitly requested their removal.'
      if $text =~ /\bgit\s+clean\b[^\n]*\s-(?:[^\n]*f[^\n]*d|[^\n]*d[^\n]*f)/i;
    return 'PreToolUse rejected an unsafe root-targeted remove path.'
      if $text =~ /\brm\s+-rf\s+--?\s*\/(?:\s|\z)/i;
    return 'PreToolUse rejected an unsafe workspace-targeted remove path.'
      if $text =~ /\brm\s+-rf\b[^\n]*(?:\s--)?\s+\.(?:\s|\z|\/)/i;
    return undef;
}

sub pre_tool_policy_lines {
    my (%args) = @_;
    my $repo_has_patch_release = $args{repo_has_patch_release};
    my $tool_name = $args{tool_name} // 'tool';
    my $group = tool_group_name($tool_name);
    my $label = tool_group_label($tool_name);

    my @lines = ("Pre-tool guardrails for `$label` (`$tool_name`):");
    if ($group eq 'shell') {
        push @lines, '- Keep shell execution deterministic, bounded, and scoped to the smallest command that proves the next claim.';
        push @lines, '- Avoid destructive git history rewrites or broad filesystem deletes unless the user explicitly requested them.';
    } elsif ($group eq 'edit') {
        push @lines, '- Keep edits reviewable and minimal; prefer focused patches over large rewrites.';
        push @lines, '- Preserve user-authored changes and avoid deleting files or compatibility branches unless the request explicitly requires it.';
    } elsif ($group eq 'mcp') {
        push @lines, '- Keep MCP calls narrow, with the smallest connector/tool scope that answers the current question.';
        push @lines, '- Avoid follow-up connector work that spends money, mutates external state, or widens access without an explicit user need.';
    } elsif ($group eq 'memory') {
        push @lines, '- Memory search is for continuity and prior decisions; start with the smallest specific keywords such as repo paths, feature names, rollout ids, or account names.';
        push @lines, '- Prefer targeted hits in `MEMORY.md`, then follow only the cited rollout or skill files you need instead of broad rescans of all memory artifacts.';
        push @lines, '- Treat memory as guidance: verify drift-prone facts against the current repo, runtime, or user message before acting on them.';
    } elsif ($group =~ /\Amcp_/) {
        push @lines, '- Keep MCP calls narrow, with the smallest connector/tool scope that answers the current question.';
        push @lines, '- Avoid follow-up connector work that spends money, mutates external state, or widens access without an explicit user need.';
        push @lines, map { "- $_" } mcp_pre_tool_lines($tool_name);
    } else {
        push @lines, '- Prefer deterministic inputs, bounded I/O, and the smallest reviewable mutation.';
    }
    push @lines, '- Patch-release repo detected; keep local patch operations check-only with `git apply --check` until the patch contract is satisfied.'
      if $repo_has_patch_release;
    return @lines;
}

sub permission_request_message {
    my (%args) = @_;
    my $tool_name = $args{tool_name} // 'tool';
    my $label = tool_group_label($tool_name);
    my @lines = (
        "Permission request for `$label` (`$tool_name`):",
        '- Keep the scope minimal and name the exact files, paths, or network boundary being requested.',
        '- The justification should connect directly to the current task and avoid broad future-looking access asks.',
    );
    push @lines, map { "- $_" } mcp_permission_lines($tool_name)
      if tool_group_name($tool_name) =~ /\Amcp_/;
    return join("\n", @lines);
}

sub compact_system_message {
    my ($phase) = @_;
    return join(
        "\n",
        "$phase compact guidance:",
        '- Preserve repo identity, current branch, changed files, pending validation work, and explicit user constraints.',
        '- Preserve hook-derived context around source builds, release patches, memory cues, and subagent ownership boundaries.',
    );
}

sub subagent_stop_system_message {
    return join(
        "\n",
        'Subagent stop guidance:',
        '- Summarize owned files, checks run, unresolved risks, and whether follow-up validation is still required.',
        '- If validation could not complete, state the exact blocker before the parent turn ends.',
    );
}

1;
