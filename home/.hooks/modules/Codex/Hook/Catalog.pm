package Codex::Hook::Catalog;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(hook_catalog);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

sub hook_catalog {
    return {
        version => 2,
        manifest => 'hooks.json',
        engine => 'runner.py',
        tool_profiles => [{ id => 'generic', matcher => '.*', label => 'Use the current tool contract', events => {} }],
        roles => [],
        subagent_profiles => [],
    };
}

1;
