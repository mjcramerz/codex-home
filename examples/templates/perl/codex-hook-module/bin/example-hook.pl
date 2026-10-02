#!/usr/bin/env perl
use strict;
use warnings;
use JSON::PP qw(encode_json decode_json);
use FindBin qw($Bin);
use lib "$Bin/../lib";
use Codex::Hook::Example;

my $raw = do { local $/; <STDIN> };
my $payload = length($raw) ? decode_json($raw) : {};
my $result = Codex::Hook::Example::run(payload => $payload);
print encode_json($result), "
";
