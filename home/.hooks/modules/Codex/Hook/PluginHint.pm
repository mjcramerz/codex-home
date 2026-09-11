package Codex::Hook::PluginHint;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(plugin_catalog_context);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

# Let runner.py suggest fixed local candidates from repository evidence. Never
# turn marketplace prose or an installed-cache manifest into developer authority.
sub plugin_catalog_context { return undef; }

1;
