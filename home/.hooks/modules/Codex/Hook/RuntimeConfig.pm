package Codex::Hook::RuntimeConfig;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(runtime_config);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

sub runtime_config {
    return {
        version => 2,
        context_engine => 'runner.py',
        manifest => 'hooks.json',
        schema_context => 0,
        transcript_context => 0,
        repository_execution => 0,
        max_context_characters => 7200,
        multi_agent => {
            trigger_patterns => [], shared_lines => [], prompt_submit_lines => [],
            roles => [], subagent_profiles => [],
        },
        repos => [],
    };
}

1;
