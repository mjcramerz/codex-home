"""Exercise the hook protocol, privacy, lifecycle and filesystem boundaries."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

SOURCE = Path(__file__).resolve().parents[1]/'home/.hooks'


class HookTests(unittest.TestCase):
    def test_configuration_edit_requires_real_filename_evidence(self):
        for tool_input in [{'path': '/repo/.codex/config.toml'},
                           {'file_path': '/repo/home/unleash.config.toml'},
                           '*** Begin Patch\n*** Update File: /repo/hooks.json\n@@\n-secret\n+private\n*** End Patch']:
            with self.subTest(tool_input=type(tool_input).__name__):
                output = self.call('PostToolUse', tool_name='apply_patch', tool_input=tool_input)
                context = output['hookSpecificOutput']['additionalContext']
                self.assertIn('configuration changed', context)
                self.assertNotIn('secret', context)
                self.assertIn('Configuration edits were observed', self.call('Stop')['systemMessage'])
                self.call('SessionEnd')
        self.assertFalse(self.runner.configuration_edit({'tool_name':'apply_patch',
                         'tool_input':{'path':'/repo/main.py','body':'config.toml'}}))
        self.assertFalse(self.runner.configuration_edit({'tool_name':'exec_command',
                         'tool_input':{'cmd':'cat config.toml'}}))

    def test_failed_configuration_edit_does_not_claim_a_change(self):
        output = self.call('PostToolUse', tool_name='apply_patch',
                          tool_input={'path':'/repo/config.toml'}, tool_response={'isError':True})
        self.assertNotIn('configuration changed', str(output))
        self.assertNotIn('Configuration edits were observed', str(self.call('Stop')))

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.home = self.root/'home'
        self.hook = self.home/'.hooks'
        shutil.copytree(SOURCE, self.hook, ignore=shutil.ignore_patterns('state', '__pycache__'))
        self.repo = self.root/'repo'
        self.repo.mkdir()
        (self.repo/'.git').mkdir()
        (self.repo/'pyproject.toml').write_text('[project]\nname="fixture"\nversion="1"\n')
        spec = importlib.util.spec_from_file_location('hook_runner', self.hook/'runner.py')
        self.runner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.runner)

    def payload(self, event, **extra):
        data = {'hook_event_name': event, 'cwd': str(self.repo), 'session_id': 'fixture-session',
                'transcript_path': None, 'model': 'gpt-6.1-sol', 'permission_mode': 'default',
                'turn_id': 'fixture-turn', 'source': 'startup', 'reason': 'other',
                'trigger': 'manual', 'agent_id': 'fixture-child', 'agent_type': 'tester',
                'agent_transcript_path': None, 'last_assistant_message': None,
                'stop_hook_active': False, 'prompt': 'Inspect Python code',
                'tool_name': 'exec_command', 'tool_input': {'cmd': 'python3 -m unittest'},
                'tool_use_id': 'fixture-tool', 'tool_response': {'exit_code': 0}}
        data.update(extra)
        name = self.runner.ALIASES.get(event, event)
        filename = __import__('re').sub(r'(?<!^)(?=[A-Z])', '-', name).lower()
        schema = json.loads((self.hook/'schemas'/f'{filename}.command.input.schema.json').read_text())
        return {key: data[key] for key in schema['properties'] if key in data}

    def call(self, event, **extra):
        output = self.runner.handle(event, self.payload(event, **extra), time.monotonic()+2)
        self.runner.validate_contract(event, output, 'output')
        return output

    def process(self, event, data, budget='1'):
        result = subprocess.run([sys.executable, '-I', str(self.hook/'runner.py'),
                                 '--event', event, '--timeout', budget],
                                input=data, text=True, capture_output=True, timeout=4)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, '')
        return json.loads(result.stdout)

    def test_all_twelve_events_accept_and_emit_the_supplied_contract(self):
        for event in sorted(self.runner.EVENTS):
            with self.subTest(event=event):
                payload = self.payload(event)
                output = self.process(event, json.dumps(payload))
                self.runner.validate_contract(event, output, 'output')
                self.assertNotEqual(output, self.runner.failure_output(event))

    def test_current_hook_schemas_are_identical_in_both_paths(self):
        first = self.hook/'schemas'
        second = self.hook/'schema/generated'
        self.assertEqual({p.name for p in first.glob('*.json')}, {p.name for p in second.glob('*.json')})
        self.assertTrue((first/'interrupt.command.input.schema.json').is_file())
        self.assertTrue((first/'interrupt.command.output.schema.json').is_file())
        for path in first.glob('*.json'):
            self.assertEqual(path.read_bytes(), (second/path.name).read_bytes())
            self.runner._schema_module.check_schema(json.loads(path.read_text()))

    def test_static_discovery_never_executes_make_or_project_imports(self):
        marker = self.root/'executed'
        (self.repo/'Makefile').write_text(f'$(shell touch {marker})\nall: test\ntest:\n\tfalse\ninclude generated.mk\n')
        (self.repo/'schema_check.py').write_text(f'open({str(marker)!r}, "w").write("bad")\n')
        output = self.process('SessionStart', json.dumps(self.payload('SessionStart')))
        text = output['hookSpecificOutput']['additionalContext']
        self.assertIn('literal targets', text)
        self.assertRegex(text, r'literal targets: (?:all, test|test, all)\.')
        self.assertIn('additional targets', text)
        self.assertFalse(marker.exists())
        self.assertNotIn('touch', text)

    def test_private_payloads_and_transcripts_are_never_replayed(self):
        marker = 'PRIVATE_PAYLOAD_SENTINEL'
        transcript = self.root/'transcript.jsonl'
        transcript.write_text(marker)
        payload = self.payload('UserPromptSubmit', prompt='Python '+marker, transcript_path=str(transcript))
        output = self.process('UserPromptSubmit', json.dumps(payload))
        self.assertNotIn(marker, json.dumps(output))
        self.call('PostToolUse', tool_response={'exit_code': 1, 'output': marker})
        for path in (self.hook/'state').glob('*.json'):
            self.assertEqual(path.stat().st_mode & 0o777, 0o600)
            self.assertNotIn(marker, path.read_text())
            data = json.loads(path.read_text())
            self.assertEqual(set(data), {'latest', 'flags'})
            self.assertTrue(all(isinstance(v, bool) for v in data['flags'].values()))

    def test_tool_hook_does_not_rescan_the_repository(self):
        self.runner.detected_context = lambda *args: self.fail('per-tool repository scan')
        output = self.call('PreToolUse')
        self.assertIn('argument', output['hookSpecificOutput']['additionalContext'])
        self.assertEqual(self.call('PreToolUse'), {})

    def test_latest_digest_refreshes_when_context_changes_and_changes_back(self):
        state = self.runner.SessionState(self.payload('SessionStart'), self.repo)
        self.addCleanup(state.close)
        self.assertTrue(state.first('repository-context', 'A'))
        self.assertFalse(state.first('repository-context', 'A'))
        self.assertTrue(state.first('repository-context', 'B'))
        self.assertTrue(state.first('repository-context', 'A'))

    def test_code_mode_and_mcp_guidance_preserve_nested_boundaries(self):
        code = self.call('PreToolUse', tool_name='exec')['hookSpecificOutput']['additionalContext']
        self.assertIn('nested tool retains its own permission', code)
        self.assertNotIn('permissionDecision', code)
        mcp = self.call('PreToolUse', tool_name='mcp__filesystem__write_file')['hookSpecificOutput']['additionalContext']
        self.assertIn('credential scope and side effects', mcp)
        self.assertEqual(self.call('PreToolUse', tool_name='mcp__fetch__fetch'), {})

    def test_validation_failure_is_reported_without_a_stop_loop(self):
        self.call('PostToolUse', tool_response={'exit_code': 1})
        output = self.call('Stop')
        self.assertIn('validation command reported failure', output['systemMessage'])
        self.assertNotIn('decision', output)
        self.assertEqual(self.call('Stop'), {})
        self.assertEqual(self.call('Stop', stop_hook_active=True), {})

    def test_unknown_response_text_does_not_invent_a_validation_result(self):
        self.assertEqual(self.call('PostToolUse', tool_response='exit_code=1: tests failed'), {})
        self.assertEqual(self.call('Stop'), {})

    def test_edits_are_observed_and_compaction_preserves_only_status_flags(self):
        self.call('PostToolUse', tool_name='apply_patch', tool_response={})
        pre = self.call('PreCompact')
        self.assertNotIn('hookSpecificOutput', pre)
        self.assertEqual(self.call('PostCompact'), {})
        self.assertIn('Edits were observed', self.call('Stop')['systemMessage'])
        for p in (self.hook/'state').glob('*.json'):
            self.assertNotIn('tool_input', p.read_text())

    def test_permission_request_leaves_the_native_decision_untouched(self):
        self.assertEqual(self.call('PermissionRequest'), {})

    def test_subagent_scope_and_completion_evidence(self):
        start = self.call('SubagentStart', agent_type='reviewer')
        self.assertIn('concrete reachable defects', start['hookSpecificOutput']['additionalContext'])
        end = self.call('SubagentStop')
        self.assertIn('acceptance criteria', end['systemMessage'])

    def test_interrupt_and_session_end_cleanup(self):
        self.call('SessionStart')
        self.assertEqual(self.call('Interrupt'), {})
        self.assertEqual(self.call('SessionEnd'), {})
        self.assertFalse(list((self.hook/'state').glob('*.json')))

    def test_session_end_handles_a_removed_cwd(self):
        gone = self.root/'gone'
        gone.mkdir()
        self.call('SessionStart', cwd=str(gone))
        gone.rmdir()
        self.assertEqual(self.call('SessionEnd', cwd=str(gone)), {})
        self.assertFalse(list((self.hook/'state').glob('*.json')))

    def test_session_end_cleans_the_canonical_state_for_a_symlinked_cwd(self):
        link = self.root/'repo-link'
        link.symlink_to(self.repo, target_is_directory=True)
        self.call('SessionStart', cwd=str(link))
        self.assertEqual(self.call('SessionEnd', cwd=str(link)), {})
        self.assertFalse(list((self.hook/'state').glob('*.json')))

    def test_unsafe_state_directory_is_not_followed(self):
        elsewhere = self.root/'elsewhere'
        elsewhere.mkdir()
        (self.hook/'state').symlink_to(elsewhere, target_is_directory=True)
        self.assertIn('hookSpecificOutput', self.call('SessionStart'))
        self.assertEqual(list(elsewhere.iterdir()), [])

    def test_symlink_and_fifo_manifests_are_not_read(self):
        secret = self.root/'secret.json'
        secret.write_text('{"scripts":{"PRIVATE_SENTINEL":"echo token"}}')
        (self.repo/'package.json').symlink_to(secret)
        os.mkfifo(self.repo/'Makefile')
        text = self.call('SessionStart')['hookSpecificOutput']['additionalContext']
        self.assertNotIn('PRIVATE_SENTINEL', text)
        self.assertNotIn('literal targets', text)

    def test_missing_fields_and_event_mismatch_fail_closed_for_policy_events(self):
        for data in [{}, self.payload('PreToolUse', hook_event_name='PostToolUse')]:
            output = self.process('PreToolUse', json.dumps(data))
            self.assertEqual(output['hookSpecificOutput']['permissionDecision'], 'deny')
            self.assertNotIn('additionalContext', output['hookSpecificOutput'])

    def test_duplicate_keys_and_non_json_numbers_are_rejected(self):
        for raw in ['{"cwd":"a","cwd":"b"}', '{"cwd":NaN}']:
            output = self.process('PermissionRequest', raw)
            self.assertEqual(output['hookSpecificOutput']['decision']['behavior'], 'deny')

    def test_input_bound_does_not_echo_or_log_oversized_payload(self):
        raw = json.dumps(self.payload('PreToolUse', tool_input={'cmd': 'SECRET' * 50000}))
        output = self.process('PreToolUse', raw)
        self.assertEqual(output['hookSpecificOutput']['permissionDecision'], 'deny')
        self.assertNotIn('SECRET', json.dumps(output))

    def test_slow_or_incomplete_stdin_is_bounded(self):
        process = subprocess.Popen([sys.executable, '-I', str(self.hook/'runner.py'),
                                    '--event', 'PreToolUse', '--timeout', '0.1'],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            process.wait(timeout=2)
            output = json.loads(process.stdout.read())
            self.assertEqual(output['hookSpecificOutput']['permissionDecision'], 'deny')
            self.assertEqual(process.stderr.read(), b'')
        finally:
            if process.poll() is None:
                process.kill()
                process.wait()
            for stream in [process.stdin, process.stdout, process.stderr]:
                stream.close()

    def test_perl_compatibility_dispatch_uses_the_same_isolated_engine(self):
        payload = self.payload('SessionStart')
        result = subprocess.run(['/usr/bin/perl', str(self.hook/'scripts/hook_driver.pl'), 'SessionStart'],
                                input=json.dumps(payload), capture_output=True, text=True, timeout=4)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.runner.validate_contract('SessionStart', json.loads(result.stdout), 'output')


if __name__ == '__main__':
    unittest.main()
