package Codex::Hook::McpTool;

use strict;
use warnings;
use Exporter qw(import);
our @EXPORT_OK = qw(mcp_permission_lines mcp_post_tool_lines mcp_pre_tool_lines);

# Use hooks.json and runner.py for lifecycle dispatch. Keep this compatibility
# surface free of schema injection, transcript replay and repository execution.

sub mcp_pre_tool_lines {
    return ('Read the advertised MCP tool contract. Keep credentials and returned text out of ambient context; check authorization before externally visible writes.');
}
sub mcp_permission_lines {
    return ('Evaluate the exact target and side effects. An installed MCP server does not grant permission to perform the action.');
}
sub mcp_post_tool_lines { return (); }

1;
