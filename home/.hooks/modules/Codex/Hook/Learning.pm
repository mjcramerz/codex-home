package Codex::Hook::Learning;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(prompt_keyword_context_lines tool_response_summary_lines transcript_summary_lines);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

# Do not resurrect transcript-derived or tool-response-derived ambient context.
# The active runner uses only bounded identifiers and typed failure booleans.
sub prompt_keyword_context_lines { return (); }
sub tool_response_summary_lines { return (); }
sub transcript_summary_lines { return (); }

1;
