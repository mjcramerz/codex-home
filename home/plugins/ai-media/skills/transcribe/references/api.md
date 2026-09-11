# gpt-4o-transcribe-diarize quick reference

Consult this reference when gpt-4o-transcribe-diarize quick reference is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

- Input formats: mp3, mp4, mpeg, mpga, m4a, wav, webm.
- Max file size: 25 MB per request.
- response_format options: text, json, diarized_json.
- For audio longer than ~30 seconds, pass chunking_strategy (use "auto" to split into chunks).
- Known speakers: up to 4 references via extra_body known_speaker_names + known_speaker_references (data URLs).
- Prompting is not supported for gpt-4o-transcribe-diarize.
