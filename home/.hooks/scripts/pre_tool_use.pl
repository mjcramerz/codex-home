#!/usr/bin/env perl
use strict;
use warnings;

use FindBin qw($Bin);
use Cwd qw(abs_path);
use File::Spec;

BEGIN {
    my @candidates = (
        File::Spec->catdir($Bin, "..", "modules"),
        File::Spec->catdir($Bin, "lib"),
    );
    for my $candidate (@candidates) {
        my $resolved = abs_path($candidate);
        next if !defined $resolved || !-d $resolved;
        unshift @INC, $resolved;
        last;
    }
}

use Codex::Hook::Script qw(dispatch_named_wrapper);

dispatch_named_wrapper(
    script_dir    => $Bin,
    wrapper_name  => $0,
);
