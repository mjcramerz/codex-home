package Codex::Hook::Runner;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(run_command read_file_tail);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

# Retire implicit process probes. Return a distinct non-success status rather
# than pretending that an unexecuted command passed or the tool was absent.
sub run_command {
    return { rc => 125, stdout => '', stderr => 'Legacy hook process probes are disabled; inspect through an explicitly authorized tool.' };
}
# Never read or replay transcripts, logs, schemas or arbitrary payload paths.
sub read_file_tail { return ''; }

1;
