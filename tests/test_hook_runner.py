"""Exercise bounded hook processes without needing the optional Perl modules."""
import importlib.util
import json
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('hook_runner',ROOT/'home/.hooks/runner.py')
runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)

class HookRunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);(self.root/'scripts').mkdir()
        self.patch=patch.object(runner,'ROOT',self.root);self.patch.start();self.addCleanup(self.patch.stop)
    def run_script(self,source,seconds=2):
        path=self.root/'scripts/test.pl';path.write_text(source)
        return runner.execute(path,b'{"hook_event_name":"PreToolUse"}',time.monotonic()+seconds)
    def test_passes_json_without_reformat(self):
        result=self.run_script('use JSON::PP; local $/; my $in=<STDIN>; print "{\\"continue\\":true}\\n";')
        self.assertEqual(result,b'{"continue":true}\n')
    def test_empty_success_is_allowed(self):
        self.assertEqual(self.run_script('local $/; <STDIN>; exit 0;'),b'')
    def test_policy_failure_stops_without_secret(self):
        value=json.loads(runner.failure('PermissionRequest'))
        self.assertFalse(value['continue']);self.assertIn('stopReason',value)
    def test_observation_failure_warns(self):
        self.assertTrue(json.loads(runner.failure('PostToolUse'))['continue'])
    def test_nonzero_failure_suppresses_raw_stderr(self):
        with self.assertRaises(runner.HookFailure):self.run_script('local $/; <STDIN>; die "SECRET_TOKEN";')
    def test_malformed_output_rejected(self):
        with self.assertRaises(ValueError):self.run_script('local $/; <STDIN>; print "not json";')
    def test_output_flood_is_bounded(self):
        with self.assertRaises(runner.HookFailure):self.run_script('local $/; <STDIN>; print "x" x 300000;')
    def test_stderr_flood_is_bounded(self):
        with self.assertRaises(runner.HookFailure):self.run_script('local $/; <STDIN>; print STDERR "x" x 40000;')
    def test_timeout_kills_descendants(self):
        with self.assertRaises(runner.HookFailure):self.run_script('local $/; <STDIN>; my $pid=fork(); sleep 30;',.1)
    def test_path_escape_rejected(self):
        with self.assertRaises(runner.HookFailure):runner.execute(Path('/tmp/untrusted.pl'),b'{}',time.monotonic()+1)
    def test_symlink_rejected(self):
        target=self.root/'target';target.write_text('exit 0;')
        link=self.root/'scripts/link.pl';link.symlink_to(target)
        with self.assertRaises(runner.HookFailure):runner.execute(link,b'{}',time.monotonic()+1)
    def test_invalid_input_rejected(self):
        path=self.root/'scripts/test.pl';path.write_text('exit 0;')
        with self.assertRaises(runner.HookFailure):runner.execute(path,b'[]',time.monotonic()+1)

if __name__=='__main__':unittest.main()
