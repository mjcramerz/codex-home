package Codex::Hook::Driver;

use strict;
use warnings;

use Exporter qw(import);
use JSON::PP qw(decode_json);

use Codex::Hook::Environment qw(
  environment_report
  stringify_payload_text
);
use Codex::Hook::Event;
use Codex::Hook::Learning qw(
  prompt_keyword_context_lines
  tool_response_summary_lines
  transcript_summary_lines
);
use Codex::Hook::MultiAgent qw(
  multi_agent_prompt_context
  subagent_role_context
);
use Codex::Hook::Model qw(normalize_input);
use Codex::Hook::McpTool qw(mcp_post_tool_lines);
use Codex::Hook::Output qw(
  emit_block
  emit_context
  emit_payload
  emit_stop
  emit_system_message
  json_true
);
use Codex::Hook::Policy qw(
  compact_system_message
  destructive_command_reason
  permission_request_message
  pre_tool_policy_lines
);
use Codex::Hook::PluginHint qw(plugin_catalog_context);
use Codex::Hook::Repo qw(
  current_branch
  git_root
  has_patch_release_dir
  has_salsa_packaging_layout
  list_changed_files
  list_mirror_refs
  list_packaging_refs
  preferred_mirror_main_branch
  preview_paths
  summarize_worktree
);
use Codex::Hook::Runner qw(read_file_tail);
use Codex::Hook::Schema qw(validate_event_input);
use Codex::Hook::Subagent qw(start_context);
use Codex::Hook::SubagentStop qw(stop_system_message);
use Codex::Hook::RuntimeConfig qw(runtime_config);
use Codex::Hook::ToolProfile qw(
  active_tool_profile_is_primary
  tool_group_label
  tool_group_name
  tool_hooks_enabled
);

our @EXPORT_OK = qw(run_event);

sub _load_input {
    local $/;
    my $raw = <STDIN>;
    return {} if !defined $raw || $raw !~ /\S/;
    my $payload = decode_json($raw);
    die "hook input must decode to an object\n" if ref($payload) ne 'HASH';
    return $payload;
}

sub _load_runtime_config {
    my $payload = runtime_config();
    die "hook runtime config must decode to an object\n" if ref($payload) ne 'HASH';
    die "hook runtime config must declare version = 1\n"
      if ($payload->{version} // 0) != 1;
    die "hook runtime config must contain a repos list\n"
      if ref($payload->{repos}) ne 'ARRAY';
    return $payload;
}

sub _join_sections {
    my (@sections) = @_;
    my @filtered = grep { defined($_) && length($_) } @sections;
    return undef if !@filtered;

    my %seen_bullets;
    my @rendered_sections;
    for my $section (@filtered) {
        my @section_lines;
        for my $line (split /\n/, $section) {
            next if !defined $line;
            my $normalized = $line;
            $normalized =~ s/^\s+|\s+$//g;
            next if !length $normalized;
            if ($normalized =~ /^-\s+/) {
                next if $seen_bullets{$normalized}++;
            }
            push @section_lines, $normalized;
        }
        next if !@section_lines;
        push @rendered_sections, join("\n", @section_lines);
    }
    return undef if !@rendered_sections;
    return join("\n\n", @rendered_sections);
}

sub _section {
    my ($header, @lines) = @_;
    return undef if !defined $header || !length $header;
    my @rendered;
    for my $line (@lines) {
        next if !defined $line;
        my $trimmed = $line;
        $trimmed =~ s/^\s+|\s+$//g;
        next if !length $trimmed;
        push @rendered, ($trimmed =~ /^-\s+/ ? $trimmed : "- $trimmed");
    }
    return undef if !@rendered;
    return join("\n", $header, @rendered);
}

sub _format_item_list {
    my ($items, $limit) = @_;
    return '' if ref($items) ne 'ARRAY' || !@{$items};
    my @values = grep { defined($_) && length($_) } @{$items};
    return '' if !@values;
    if (defined $limit && $limit =~ /\A[0-9]+\z/ && $limit > 0 && @values > $limit) {
        my $last = $limit - 1;
        my $rendered = '`' . join('`, `', @values[0 .. $last]) . '`';
        my $remaining = @values - ($last + 1);
        $rendered .= " (+$remaining more)" if $remaining > 0;
        return $rendered;
    }
    return '`' . join('`, `', @values) . '`';
}

sub _glob_regex {
    my ($glob) = @_;
    my $token_any_dirs = '__CODEX_HOOK_ANY_DIRS__';
    my $token_any = '__CODEX_HOOK_ANY__';
    my $token_one = '__CODEX_HOOK_ONE__';
    my $regex = $glob // '';
    $regex =~ s/\*\*/$token_any_dirs/g;
    $regex =~ s/\*/$token_any/g;
    $regex =~ s/\?/$token_one/g;
    $regex = quotemeta($regex);
    $regex =~ s/\Q$token_any_dirs\E/.*/g;
    $regex =~ s/\Q$token_any\E/[^\/\\\n]*/g;
    $regex =~ s/\Q$token_one\E/[^\/\\\n]/g;
    return qr/\A$regex\z/;
}

sub _matches_any_glob {
    my ($path, $globs) = @_;
    return 0 if !defined $path || ref($globs) ne 'ARRAY';
    for my $glob (@{$globs}) {
        next if !defined $glob || !length($glob);
        return 1 if $path =~ _glob_regex($glob);
    }
    return 0;
}

my @RESTRICTED_MIRROR_ALLOWLIST_GLOBS = (
    'AGENTS.override.md',
    '.gitlab-ci.yml',
    '.cirrus.yml',
    'Makefile',
    'justfile',
    '.github/**',
    'scripts/release/**',
    'patches/release/**',
    '.mcr/**',
    '.circleci/**',
    '.devcontainer/**',
    '.vscode/**',
    '.codex/**',
    '.agents/**',
    'debian/**',
    '.bazelversion',
    '.bazelignore',
    '.bazelrc',
    'bazel/**',
);

sub _restricted_mirror_disallowed_paths {
    my ($changed_files) = @_;
    return () if ref($changed_files) ne 'ARRAY';
    return grep {
        defined($_) && length($_) && !_matches_any_glob($_, \@RESTRICTED_MIRROR_ALLOWLIST_GLOBS)
    } @{$changed_files};
}

sub _focus_areas {
    my ($manifest, $profiles) = @_;
    my @groups;
    for my $container ($manifest, @{$profiles || []}) {
        next if ref($container) ne 'HASH';
        next if ref($container->{focus_areas}) ne 'ARRAY';
        push @groups, @{$container->{focus_areas}};
    }
    return @groups;
}

sub _detect_changed_areas {
    my ($changed_files, $manifest, $profiles) = @_;
    return () if ref($changed_files) ne 'ARRAY' || !@{$changed_files};
    my @areas;
    my %seen;
    for my $group (_focus_areas($manifest, $profiles)) {
        next if ref($group) ne 'HASH';
        my $label = $group->{label} // '';
        next if !length($label);
        my $globs = $group->{path_globs};
        next if ref($globs) ne 'ARRAY' || !@{$globs};
        for my $path (@{$changed_files}) {
            next if !_matches_any_glob($path, $globs);
            push @areas, $label if !$seen{$label}++;
            last;
        }
    }
    return @areas;
}

sub _repo_matches {
    my ($repo_root, $profile) = @_;
    return 0 if !defined $repo_root || ref($profile) ne 'HASH';
    my $match = $profile->{match};
    return 0 if ref($match) ne 'HASH';

    my $repo_name = $repo_root;
    $repo_name =~ s{.*/}{};
    my $matched = 0;
    my $repo_names = $match->{repo_names};
    if (ref($repo_names) eq 'ARRAY' && @{$repo_names}) {
        return 0 if !grep { defined($_) && $_ eq $repo_name } @{$repo_names};
        $matched = 1;
    }

    my $all_of = $match->{all_of_paths};
    if (ref($all_of) eq 'ARRAY' && @{$all_of}) {
        for my $path (@{$all_of}) {
            return 0 if !-e "$repo_root/$path";
        }
        $matched = 1;
    }

    my $any_of = $match->{any_of_paths};
    if (ref($any_of) eq 'ARRAY' && @{$any_of}) {
        for my $path (@{$any_of}) {
            if (-e "$repo_root/$path") {
                $matched = 1;
                return 1 if !(ref($repo_names) eq 'ARRAY' && @{$repo_names}) && !(ref($all_of) eq 'ARRAY' && @{$all_of});
                last;
            }
        }
        return 0 if !$matched;
    }

    return $matched ? 1 : 0;
}

sub _find_repo_profiles {
    my ($manifest, $repo_root) = @_;
    return () if ref($manifest->{repos}) ne 'ARRAY' || !defined $repo_root;
    return grep { _repo_matches($repo_root, $_) } @{$manifest->{repos}};
}

sub _format_template {
    my ($text, $values) = @_;
    my $rendered = $text // '';
    return '' if !length($rendered);
    $rendered =~ s/\{([a-z_]+)\}/exists($values->{$1}) ? $values->{$1} : "{$1}"/ge;
    return $rendered;
}

sub _format_lines {
    my ($lines, $values) = @_;
    return () if ref($lines) ne 'ARRAY';
    my @rendered;
    for my $line (@{$lines}) {
        next if !defined $line || !length($line);
        push @rendered, _format_template($line, $values);
    }
    return @rendered;
}

sub _manifest_block_entries {
    my ($manifest, $profiles, $section) = @_;
    my @blocks;
    if (ref($manifest->{$section}) eq 'HASH') {
        push @blocks, $manifest->{$section};
    }
    for my $profile (@{$profiles || []}) {
        next if ref($profile) ne 'HASH';
        next if ref($profile->{$section}) ne 'HASH';
        push @blocks, $profile->{$section};
    }
    return @blocks;
}

sub _environment_blocks {
    my ($manifest, $profiles) = @_;
    my @blocks;
    if (ref($manifest->{environment}) eq 'HASH') {
        push @blocks, $manifest->{environment};
    }
    for my $profile (@{$profiles || []}) {
        next if ref($profile) ne 'HASH';
        next if ref($profile->{environment}) ne 'HASH';
        push @blocks, $profile->{environment};
    }
    return @blocks;
}

sub _environment_lines {
    my ($report) = @_;
    return () if ref($report) ne 'HASH';
    my @lines = ('Local environment signals:');
    push @lines, '- Required commands available: ' . _format_item_list($report->{required_available}, 6) . '.'
      if ref($report->{required_available}) eq 'ARRAY' && @{ $report->{required_available} };
    push @lines, '- Required commands missing: ' . _format_item_list($report->{required_missing}, 6) . '.'
      if ref($report->{required_missing}) eq 'ARRAY' && @{ $report->{required_missing} };
    push @lines, '- Optional commands available: ' . _format_item_list($report->{optional_available}) . '.'
      if ref($report->{optional_available}) eq 'ARRAY' && @{ $report->{optional_available} };
    push @lines, '- Optional commands missing: ' . _format_item_list($report->{optional_missing}) . '.'
      if ref($report->{optional_missing}) eq 'ARRAY' && @{ $report->{optional_missing} };
    if (ref($report->{probes}) eq 'ARRAY') {
        for my $probe (@{ $report->{probes} }) {
            next if ref($probe) ne 'HASH';
            my $label = $probe->{label} // 'probe';
            my $status = $probe->{status} // 'unknown';
            my $detail = $probe->{detail} // '';
            my $line = "- Probe `$label`: $status";
            $line .= " ($detail)" if length $detail;
            push @lines, $line . '.';
        }
    }
    return @lines > 1 ? @lines : ();
}

sub _environment_has_warnings {
    my ($report) = @_;
    return 0 if ref($report) ne 'HASH';
    return 1 if ref($report->{required_missing}) eq 'ARRAY' && @{ $report->{required_missing} };
    return 1 if ref($report->{probes}) eq 'ARRAY' && grep {
        ref($_) eq 'HASH' && ($_->{status} // '') ne 'ok'
    } @{ $report->{probes} };
    return 0;
}

sub _multi_agent_context {
    my ($manifest, $prompt) = @_;
    return multi_agent_prompt_context(
        manifest => $manifest,
        prompt   => $prompt,
    );
}

sub _session_start_context {
    my ($manifest, $payload) = @_;
    my $repo_root = git_root($payload->{cwd} // '');
    return undef if !defined $repo_root;

    my @profiles = _find_repo_profiles($manifest, $repo_root);
    my $environment = environment_report(
        blocks => [ _environment_blocks($manifest, \@profiles) ],
        cwd    => $repo_root,
    );
    my @changed_files = list_changed_files($repo_root);
    my @changed_areas = _detect_changed_areas(\@changed_files, $manifest, \@profiles);
    my $current = current_branch($repo_root);
    my @mirror_refs = list_mirror_refs($repo_root);
    my @packaging_refs = list_packaging_refs($repo_root);
    my $mirror_main = preferred_mirror_main_branch($repo_root);
    my $restricted_mirror = length($mirror_main) ? 1 : 0;
    my $has_salsa_packaging = has_salsa_packaging_layout($repo_root);
    my $worktree = summarize_worktree($repo_root);
    my @profile_ids = map { $_->{id} } grep { ref($_) eq 'HASH' && defined($_->{id}) && length($_->{id}) } @profiles;
    my $profile_id = @profile_ids ? $profile_ids[0] : '';
    my %values = (
        changed_areas_csv       => @changed_areas ? join(', ', @changed_areas) : 'none',
        changed_files_preview   => preview_paths(\@changed_files),
        current_branch          => $current,
        profile_ids_csv         => @profile_ids ? join(', ', @profile_ids) : 'none',
        repo_id                 => length($profile_id) ? $profile_id : ($repo_root =~ s{.*/}{}r),
        repo_name               => ($repo_root =~ s{.*/}{}r),
        repo_root               => $repo_root,
        runtime_hooks_dir       => '$CODEX_HOME/.hooks',
        runtime_hooks_driver_path => '$CODEX_HOME/.hooks/scripts/hook_driver.pl',
        runtime_hooks_modules_dir => '$CODEX_HOME/.hooks/modules',
        runtime_hooks_config_path => '$CODEX_HOME/hooks.json',
    );

    my @repo_lines = (
        "Repo root: `$repo_root`",
        "Current branch: `$current`",
        'Authored edits are only allowed on `mcr/main`.',
    );
    push @repo_lines, "Root instructions: follow the repo-root `AGENTS.md`, plus any deeper `AGENTS.md` files under touched paths."
      if -f "$repo_root/AGENTS.md";
    push @repo_lines, 'Active hook runtime profiles: `' . join(', ', @profile_ids) . '` from the installed Perl hook runtime.'
      if @profile_ids;
    push @repo_lines, "Restricted mirror workflow detected (`$mirror_main` exists). On `mcr/main`, edits are limited to the repository-root allowlist unless deeper repo instructions expand scope."
      if $restricted_mirror;
    push @repo_lines, 'Debian Salsa packaging mirror detected (`gitlab/*` + `pristine-tar`). Preserve packaging refs such as `pristine-tar`, `upstream/*`, and `debian/*` for rebuild/import workflows.'
      if $has_salsa_packaging;
    push @repo_lines, "Packaging refs preview: `" . preview_paths(\@packaging_refs) . "`"
      if $has_salsa_packaging && @packaging_refs;
    push @repo_lines, "Current branch `$current` is not `mcr/main`; move authored changes to `mcr/main` before editing or finishing."
      if $current ne 'mcr/main';
    push @repo_lines, "Current branch `$current` is a read-only mirror branch."
      if $restricted_mirror && $current =~ m{\A(?:github|gitlab)/};
    push @repo_lines, "`patches/release/` exists. Keep local patch work check-only with commands such as `git apply --check`, `scripts/release/check_release_patches.sh HEAD`, `git mcr-fork-check`, or `git mcr-fork-test`."
      if has_patch_release_dir($repo_root);
    my @runtime_lines = (
        "Config: `$values{runtime_hooks_config_path}`",
        "Entrypoints: `$values{runtime_hooks_dir}/scripts`",
        "Modules: `$values{runtime_hooks_modules_dir}`",
    );
    my @worktree_lines;
    push @worktree_lines, 'Changed areas: `' . join('`, `', @changed_areas) . '`.' if @changed_areas;
    my @environment_lines = _environment_lines($environment);
    if (@changed_files && (($payload->{source} // '') eq 'resume' || @changed_areas)) {
        my @bits;
        for my $label (qw(staged unstaged untracked deleted renamed conflicts)) {
            my $value = int($worktree->{$label} // 0);
            push @bits, "$label=$value" if $value > 0;
        }
        push @worktree_lines, 'Worktree summary: ' . join(', ', @bits) if @bits;
        if (ref($worktree->{preview}) eq 'ARRAY' && @{$worktree->{preview}}) {
            push @worktree_lines, 'Changed files preview: `' . preview_paths($worktree->{preview}) . '`';
        }
    }
    my $source_name = lc($payload->{source} // '');
    my @recurring = $source_name eq 'resume'
      ? transcript_summary_lines(path => $payload->{transcript_path})
      : ();

    my @sections;
    push @sections, _section("Repository context for `$values{repo_name}`:", @repo_lines);
    push @sections, _section('Installed hook runtime:', @runtime_lines);
    push @sections, _section('Worktree state:', @worktree_lines) if @worktree_lines;
    push @sections, join("\n", @environment_lines) if @environment_lines;
    push @sections, _section('Resume transcript signals:', @recurring) if @recurring;
    my $index = 0;
    for my $block (_manifest_block_entries($manifest, \@profiles, 'session_start')) {
        my @lines = $source_name eq 'resume'
          ? _format_lines($block->{resume_context} || [], \%values)
          : _format_lines($block->{startup_context} || [], \%values);
        next if !@lines;
        my $header = $index++ == 0 ? 'Hook pack context:' : "Repository profile `$values{repo_id}`:";
        push @sections, _section($header, @lines);
    }
    return _join_sections(@sections);
}

sub _user_prompt_context {
    my ($manifest, $payload) = @_;
    my $prompt = $payload->{prompt} // '';
    my $repo_root = git_root($payload->{cwd} // '');
    return undef if !length($prompt) || !defined $repo_root;

    my @profiles = _find_repo_profiles($manifest, $repo_root);
    my $environment = environment_report(
        blocks => [ _environment_blocks($manifest, \@profiles) ],
        cwd    => $repo_root,
    );
    my @changed_files = list_changed_files($repo_root);
    my @changed_areas = _detect_changed_areas(\@changed_files, $manifest, \@profiles);
    my @profile_ids = map { $_->{id} } grep { ref($_) eq 'HASH' && defined($_->{id}) && length($_->{id}) } @profiles;
    my $primary = @profiles ? $profiles[0] : undef;
    my %values = (
        changed_areas_csv       => @changed_areas ? join(', ', @changed_areas) : 'none',
        changed_files_preview   => preview_paths(\@changed_files),
        current_branch          => current_branch($repo_root),
        profile_ids_csv         => @profile_ids ? join(', ', @profile_ids) : 'none',
        repo_id                 => defined($primary) ? ($primary->{id} // ($repo_root =~ s{.*/}{}r)) : ($repo_root =~ s{.*/}{}r),
        repo_name               => ($repo_root =~ s{.*/}{}r),
        repo_root               => $repo_root,
        runtime_hooks_dir       => '$CODEX_HOME/.hooks',
        runtime_hooks_driver_path => '$CODEX_HOME/.hooks/scripts/hook_driver.pl',
        runtime_hooks_modules_dir => '$CODEX_HOME/.hooks/modules',
        runtime_hooks_config_path => '$CODEX_HOME/hooks.json',
    );

    my @sections;
    if (@changed_files) {
        push @sections, join(
            "\n",
            'Current repository signals:',
            "- Current branch: `$values{current_branch}`",
            "- Changed files preview: `$values{changed_files_preview}`",
            (@changed_areas ? ('- Changed areas: `' . join('`, `', @changed_areas) . '`.') : ()),
        );
    }
    my $multi_agent = _multi_agent_context($manifest, $prompt);
    push @sections, $multi_agent if defined $multi_agent;
    push @sections, 'Review requests should lead with concrete findings ordered by severity, supported by file and line evidence plus explicit residual risks.'
      if $prompt =~ /\b(review|audit)\b/i;
    if ($prompt =~ /\b(github|gitlab|mirror|patch|patches|release|mcr\/)\b/i) {
        my @lines;
        my $mirror_main = preferred_mirror_main_branch($repo_root);
        my $restricted_mirror = length($mirror_main) ? 1 : 0;
        my $has_salsa_packaging = has_salsa_packaging_layout($repo_root);
        push @lines, 'Authored edits belong on `mcr/main` in every repository.';
        if ($restricted_mirror) {
            push @lines, 'Restricted mirror workflow detected via `'
              . $mirror_main
              . '`. On `mcr/main`, edits are limited to the repository-root allowlist unless deeper repo instructions expand scope.';
        }
        push @lines, '`gitlab/*` plus `pristine-tar` indicates a Debian Salsa packaging mirror; preserve `pristine-tar`, `upstream/*`, and `debian/*` refs for rebuild/import flows.'
          if $has_salsa_packaging;
        push @lines, '`patches/release/` exists. Keep local patch work check-only with commands such as `git apply --check`, `scripts/release/check_release_patches.sh HEAD`, `git mcr-fork-check`, or `git mcr-fork-test`.'
          if has_patch_release_dir($repo_root);
        push @sections, join("\n", @lines) if @lines;
    }
    my @environment_lines = _environment_lines($environment);
    if (@environment_lines && (
            _environment_has_warnings($environment)
            || $prompt =~ /\b(build|install|runtime|verify|validation|test|tests|docker|container|shellcheck|wrangler|node|npx|uv|make|bash)\b/i
        )) {
        push @sections, join("\n", @environment_lines);
    }
    my @keyword_lines = prompt_keyword_context_lines(prompt => $prompt);
    push @sections, join("\n", @keyword_lines) if @keyword_lines;
    my $plugin_context = plugin_catalog_context(prompt => $prompt);
    push @sections, $plugin_context if defined $plugin_context && length $plugin_context;
    for my $block (_manifest_block_entries($manifest, \@profiles, 'user_prompt_submit')) {
        next if ref($block->{rules}) ne 'ARRAY';
        for my $rule (@{$block->{rules}}) {
            next if ref($rule) ne 'HASH' || ref($rule->{patterns}) ne 'ARRAY';
            my $matched = 0;
            for my $pattern (@{$rule->{patterns}}) {
                next if !defined $pattern || !length($pattern);
                if ($prompt =~ /$pattern/i) {
                    $matched = 1;
                    last;
                }
            }
            next if !$matched;
            my @lines = _format_lines($rule->{lines} || [], \%values);
            push @sections, join("\n", @lines) if @lines;
        }
    }
    return _join_sections(@sections);
}

sub _validation_evidence {
    my ($payload) = @_;
    my $last = stringify_payload_text(value => $payload->{last_assistant_message});
    my $tail = read_file_tail(path => $payload->{transcript_path});
    return join("\n", grep { defined($_) && length($_) } ($last, $tail));
}

sub _has_skip_rationale {
    my ($text) = @_;
    return 0 if !defined $text || !length($text);
    return 1 if $text =~ /\b(could not run|couldn't run|unable to run|did not run|didn't run|cannot run|can't run|blocked)\b.*\bbecause\b/i;
    return 0 if $text !~ /\b(?:test|tests|verify|verification|validate|validation|check|checks|lint|shellcheck|ruff|mypy|eslint|clippy|taplo|py_compile|compileall|pytest|unittest|prove|perl -c)\b/i;
    return $text =~ /\b(could not run|couldn't run|unable to run|did not run|didn't run|skipped|cannot run|can't run|not run|not executed|permission boundary|permission denied|requires approval|sandbox|tool unavailable|command not found|not installed|missing dependency|out of scope)\b/i;
}

sub _has_any_evidence {
    my ($text, $patterns) = @_;
    return 0 if ref($patterns) ne 'ARRAY';
    for my $pattern (@{$patterns}) {
        next if !defined $pattern || !length($pattern);
        return 1 if $text =~ /$pattern/i;
    }
    return 0;
}

sub _has_all_evidence {
    my ($text, $patterns) = @_;
    return 0 if ref($patterns) ne 'ARRAY';
    for my $pattern (@{$patterns}) {
        next if !defined $pattern || !length($pattern);
        return 0 if $text !~ /$pattern/i;
    }
    return 1;
}

sub _collect_generic_validation_issues {
    my ($repo_root, $changed_files, $evidence, $current) = @_;
    my @issues;
    my @patch_files = grep { /\.patch\z/ || m{\Apatches/release/} } @{$changed_files};
    my $mirror_main = preferred_mirror_main_branch($repo_root);
    my $restricted_mirror = length($mirror_main) ? 1 : 0;

    if ($current ne 'mcr/main' && @{$changed_files}) {
        if ($restricted_mirror && $current =~ m{\A(?:github|gitlab)/}) {
            push @issues, "Current branch `$current` is a read-only mirror; move authored work to `mcr/main` before finishing. Changed files: " . preview_paths($changed_files) . '.';
        } else {
            push @issues, "Authored changes are only allowed on `mcr/main`; current branch `$current` must be synchronized or moved before finishing. Changed files: " . preview_paths($changed_files) . '.';
        }
    }
    if ($restricted_mirror && $current eq 'mcr/main' && @{$changed_files}) {
        my @disallowed = _restricted_mirror_disallowed_paths($changed_files);
        if (@disallowed) {
            push @issues, "Restricted mirror workflow detected via `$mirror_main`. On `mcr/main`, only the repository-root allowlist may be edited unless deeper repo instructions expand scope. Disallowed changed files: " . preview_paths(\@disallowed) . '.';
        }
    }
    if ((has_patch_release_dir($repo_root) || @patch_files) && !_has_any_evidence(
            $evidence,
            [
                qr/\bgit mcr-fork-(check|test)\b/,
                qr/\bscripts\/release\/check_release_patches\.sh\b/,
                qr/\bgit apply( --verbose)? --check\b/,
            ],
        )) {
        push @issues, 'Patch-release repo shape detected (' . (@patch_files ? preview_paths(\@patch_files) : 'patches/release/') . '). Keep local patch work check-only with `git apply --check`, `scripts/release/check_release_patches.sh HEAD`, `git mcr-fork-check`, or `git mcr-fork-test`.';
    }

    my @python_files = grep { /\.py\z/ } @{$changed_files};
    my @perl_files = grep { /\.(?:pl|pm)\z/ } @{$changed_files};
    my @shell_files = grep { /\.(sh|bash|zsh)\z/ } @{$changed_files};
    my @json_files = grep { /\.json\z/ } @{$changed_files};
    my @toml_files = grep { /\.toml\z/ } @{$changed_files};

    if (@python_files && !_has_any_evidence($evidence, [ qr/\bpython3? -m (py_compile|compileall|pytest|unittest)\b/, qr/\bpytest\b/ ])) {
        push @issues, 'Python changes (' . preview_paths(\@python_files) . ') need `python3 -m py_compile <file>` or a targeted unittest/pytest command.';
    }
    if (@perl_files && !_has_any_evidence($evidence, [ qr/\bperl\s+-c\b/, qr/\bprove\b/, qr/\bperlcritic\b/ ])) {
        push @issues, 'Perl changes (' . preview_paths(\@perl_files) . ') need `perl -c <file>` or targeted `prove` coverage.';
    }
    if (@shell_files && !_has_any_evidence($evidence, [ qr/\bshellcheck\b/, qr/\bbash -n\b/, qr/\bzsh -n\b/, qr/\b(?:sh|dash) -n\b/ ])) {
        push @issues, 'Shell changes (' . preview_paths(\@shell_files) . ') need `bash -n` and/or `shellcheck` coverage.';
    }
    if (@json_files && !_has_any_evidence($evidence, [ qr/\bpython3? -m json\.tool\b/, qr/\bjq \./ ])) {
        push @issues, 'JSON changes (' . preview_paths(\@json_files) . ') need `python3 -m json.tool` or `jq .` validation.';
    }
    if (@toml_files && !_has_any_evidence($evidence, [ qr/\btomllib\b/, qr/\btaplo\b/ ])) {
        push @issues, 'TOML changes (' . preview_paths(\@toml_files) . ') need a `tomllib` parse, `taplo`, or equivalent validation.';
    }
    return @issues;
}

sub _collect_stop_rule_issues {
    my ($manifest, $profiles, $changed_files, $evidence, $values, $current_branch, $mirror_refs_present) = @_;
    my @issues;
    for my $block (_manifest_block_entries($manifest, $profiles, 'stop')) {
        next if ref($block->{rules}) ne 'ARRAY';
        for my $rule (@{$block->{rules}}) {
            next if ref($rule) ne 'HASH';
            my @globs = ref($rule->{changed_path_globs}) eq 'ARRAY' ? @{$rule->{changed_path_globs}} : ();
            my @matched_paths = !@globs ? @{$changed_files} : grep { _matches_any_glob($_, \@globs) } @{$changed_files};
            next if @globs && !@matched_paths;

            if (ref($rule->{branch_matches_any}) eq 'ARRAY' && @{$rule->{branch_matches_any}}) {
                next if !_has_any_evidence($current_branch, $rule->{branch_matches_any});
            }
            if (exists $rule->{when_has_mirror_refs}) {
                next if (!!$rule->{when_has_mirror_refs}) != (!!$mirror_refs_present);
            }
            my %rendered_values = %{$values};
            $rendered_values{changed_files_preview} = preview_paths(\@matched_paths);
            $rendered_values{changed_areas_csv} = join(', ', _detect_changed_areas(\@matched_paths, $manifest, $profiles)) || 'none';
            my $message = _format_template($rule->{message} // '', \%rendered_values);
            next if !length $message;

            my $forbid = ref($rule->{forbid_any_patterns}) eq 'ARRAY' ? $rule->{forbid_any_patterns} : [];
            if (@{$forbid} && _has_any_evidence($evidence, $forbid)) {
                push @issues, $message;
                next;
            }
            my $require_all = ref($rule->{require_all_patterns}) eq 'ARRAY' ? $rule->{require_all_patterns} : [];
            my $require_any = ref($rule->{require_any_patterns}) eq 'ARRAY' ? $rule->{require_any_patterns} : [];
            if (!@{$require_all} && !@{$require_any} && !@{$forbid}) {
                push @issues, $message;
                next;
            }
            my $all_ok = !@{$require_all} || _has_all_evidence($evidence, $require_all);
            my $any_ok = !@{$require_any} || _has_any_evidence($evidence, $require_any);
            push @issues, $message if !$all_ok || !$any_ok;
        }
    }
    return @issues;
}

sub _stop_common {
    my ($manifest, $payload, $label) = @_;
    my $repo_root = git_root($payload->{cwd} // '');
    return if !defined $repo_root;
    my @changed_files = list_changed_files($repo_root);
    return if !@changed_files;

    my @profiles = _find_repo_profiles($manifest, $repo_root);
    my $primary = @profiles ? $profiles[0] : undef;
    my $evidence = _validation_evidence($payload);
    return if _has_skip_rationale($evidence);
    my $current = current_branch($repo_root);
    my @profile_ids = map { $_->{id} } grep { ref($_) eq 'HASH' && defined($_->{id}) && length($_->{id}) } @profiles;
    my @pattern_lines = transcript_summary_lines(path => $payload->{transcript_path});
    my $pattern_message = @pattern_lines
      ? join("\n", 'Repeated transcript signals:', map { "- $_" } @pattern_lines)
      : undef;
    my %values = (
        changed_areas_csv       => join(', ', _detect_changed_areas(\@changed_files, $manifest, \@profiles)) || 'none',
        changed_files_preview   => preview_paths(\@changed_files),
        current_branch          => $current,
        profile_ids_csv         => @profile_ids ? join(', ', @profile_ids) : 'none',
        repo_id                 => defined($primary) ? ($primary->{id} // ($repo_root =~ s{.*/}{}r)) : ($repo_root =~ s{.*/}{}r),
        repo_name               => ($repo_root =~ s{.*/}{}r),
        repo_root               => $repo_root,
        runtime_hooks_dir       => '$CODEX_HOME/.hooks',
        runtime_hooks_driver_path => '$CODEX_HOME/.hooks/scripts/hook_driver.pl',
        runtime_hooks_modules_dir => '$CODEX_HOME/.hooks/modules',
        runtime_hooks_config_path => '$CODEX_HOME/hooks.json',
    );
    my @mirror_refs = list_mirror_refs($repo_root);
    my @issues = _collect_generic_validation_issues($repo_root, \@changed_files, $evidence, $current);
    push @issues, _collect_stop_rule_issues($manifest, \@profiles, \@changed_files, $evidence, \%values, $current, scalar @mirror_refs);
    if (!@issues) {
        emit_system_message($pattern_message) if defined $pattern_message && length $pattern_message;
        return;
    }

    if ($payload->{stop_hook_active}) {
        my $stop_reason = "$label hook follow-up is still unresolved, so the turn is ending instead of blocking again:";
        $stop_reason .= join('', map { "\n- $_" } @issues);
        emit_stop($stop_reason, $pattern_message);
        return;
    }
    my $reason = "Repository and validation follow-up is required before this turn can finish:";
    $reason .= join('', map { "\n- $_" } @issues);
    $reason .= "\n- Run the missing checks now, or explain concretely why they could not be run in this environment before ending the turn.";
    emit_block($reason, $pattern_message);
}

sub _pre_tool_use_context {
    my ($manifest, $payload) = @_;
    my $tool_name = $payload->{tool_name} // '';
    my $tool_input = $payload->{tool_input};
    my $repo_root = git_root($payload->{cwd} // '');
    my $label = tool_group_label($tool_name);
    my $reason = destructive_command_reason(
        tool_name  => $tool_name,
        tool_input => $tool_input,
    );
    if (defined $reason && length $reason) {
        emit_block($reason);
        return undef;
    }

    my @lines = pre_tool_policy_lines(
        repo_has_patch_release => defined $repo_root && has_patch_release_dir($repo_root),
        tool_name              => $tool_name,
    );
    my $rendered_input = stringify_payload_text(value => $tool_input);
    if (length $rendered_input) {
        my @learned = tool_response_summary_lines(text => $rendered_input);
        if (@learned) {
            push @lines, "Input cues for `$label`:";
            push @lines, map { "- $_" } @learned;
        }
    }
    return join("\n", @lines);
}

sub _permission_request_context {
    my ($payload) = @_;
    return undef if !tool_hooks_enabled($payload->{tool_name});
    return undef if !active_tool_profile_is_primary($payload->{tool_name});
    return permission_request_message(tool_name => $payload->{tool_name});
}

sub _post_tool_use_context {
    my ($payload) = @_;
    my $tool_name = $payload->{tool_name} // 'tool';
    my $label = tool_group_label($tool_name);
    my $group = tool_group_name($tool_name);
    my $rendered = stringify_payload_text(value => $payload->{tool_response});
    return undef if $rendered !~ /\b(error|failed|exception|permission denied|not found|timed out|warning)\b/i;

    my @lines = ("Post-tool follow-up for `$label` (`$tool_name`):");
    if ($group eq 'shell') {
        push @lines, '- The shell output shows a failure or warning; tighten the next step to the failing command, flag, or path instead of widening scope.';
    } elsif ($group eq 'edit') {
        push @lines, '- The edit result shows a failure or warning; inspect the exact patch boundary before attempting another mutation.';
    } elsif ($group eq 'mcp') {
        push @lines, '- The MCP response shows a failure or warning; keep the next connector call scoped to the failing server, tool, or argument.';
    } elsif ($group eq 'memory') {
        push @lines, '- The memory tool response shows a failure or warning; retry with narrower memory keywords tied to the exact repo path, feature name, rollout id, or account you need.';
        push @lines, '- If the result still looks wrong, inspect `$CODEX_SQLITE_HOME/state_*.*` to confirm the local memory state the runtime is searching before widening the query.';
    } elsif ($group =~ /\Amcp_/) {
        push @lines, '- The MCP response shows a failure or warning; keep the next connector call scoped to the failing server, tool, or argument.';
        push @lines, map { "- $_" } mcp_post_tool_lines($tool_name);
    } else {
        push @lines, '- The tool output shows a failure or warning signal; tighten the next step to the failing boundary instead of widening scope.';
    }
    push @lines, '- If execution stayed blocked, explain the boundary concretely before asking for more permissions or ending the turn.';
    my @learned = tool_response_summary_lines(text => $rendered);
    if (@learned) {
        push @lines, 'Learned from tool output:';
        push @lines, map { "- $_" } @learned;
    }
    return join("\n", @lines);
}

sub _compact_context {
    my ($phase) = @_;
    return compact_system_message($phase);
}

sub _subagent_start_context {
    my ($manifest, $payload) = @_;
    my $agent_type = $payload->{agent_type} // 'subagent';
    my $role_context = subagent_role_context(
        manifest   => $manifest,
        agent_type => $agent_type,
        phase      => 'start',
        profile_id => ($ENV{CODEX_HOOK_SUBAGENT_PROFILE} // ''),
    );
    return start_context(
        agent_type  => $agent_type,
        role_context => $role_context,
    );
}

sub _subagent_stop_context {
    my ($manifest, $payload) = @_;
    my $role_context = subagent_role_context(
        manifest   => $manifest,
        agent_type => $payload->{agent_type},
        phase      => 'stop',
        profile_id => ($ENV{CODEX_HOOK_SUBAGENT_PROFILE} // ''),
    );
    return stop_system_message(
        payload      => $payload,
        role_context => $role_context,
    );
}

sub run_event {
    my ($event_arg) = @_;
    my $event = Codex::Hook::Event->new(
        event_arg => $event_arg,
        payload   => normalize_input($event_arg, _load_input()),
    );
    my $payload = $event->payload;

    if ($event->is_event('session-end')) {
        validate_event_input($event->event_arg, $payload, cwd => $event->cwd);
        return 0;
    }

    my $manifest = _load_runtime_config();
    validate_event_input($event->event_arg, $payload, cwd => $event->cwd);
    local $Codex::Hook::Output::CURRENT_EVENT_ARG = $event->event_arg;

    if ($event->is_event('session-start')) {
        emit_context('SessionStart', _session_start_context($manifest, $payload), undef);
        return 0;
    }
    if ($event->is_event('user-prompt-submit')) {
        emit_context('UserPromptSubmit', _user_prompt_context($manifest, $payload), undef);
        return 0;
    }
    if ($event->is_event('stop')) {
        _stop_common($manifest, $payload, 'Stop');
        return 0;
    }
    if ($event->is_event('pre-tool-use')) {
        my $tool_name = $event->payload_value('tool_name');
        return 0 if !tool_hooks_enabled($tool_name);
        return 0 if !active_tool_profile_is_primary($tool_name);
        my $context = _pre_tool_use_context($manifest, $payload);
        emit_context('PreToolUse', $context, undef) if defined $context && length $context;
        return 0;
    }
    if ($event->is_event('permission-request')) {
        my $context = _permission_request_context($payload);
        emit_system_message($context) if defined $context && length $context;
        return 0;
    }
    if ($event->is_event('post-tool-use')) {
        my $tool_name = $event->payload_value('tool_name');
        return 0 if !tool_hooks_enabled($tool_name);
        return 0 if !active_tool_profile_is_primary($tool_name);
        my $context = _post_tool_use_context($payload);
        emit_context('PostToolUse', $context, undef) if defined $context && length $context;
        return 0;
    }
    if ($event->is_event('pre-compact')) {
        emit_system_message(_compact_context('Pre'));
        return 0;
    }
    if ($event->is_event('post-compact')) {
        emit_system_message(_compact_context('Post'));
        return 0;
    }
    if ($event->is_event('subagent-start')) {
        emit_context('SubagentStart', _subagent_start_context($manifest, $payload), undef);
        return 0;
    }
    if ($event->is_event('subagent-stop')) {
        emit_system_message(_subagent_stop_context($manifest, $payload));
        _stop_common($manifest, $payload, 'SubagentStop');
        return 0;
    }
    die "unsupported hook event: " . $event->event_arg . "\n";
}

1;
