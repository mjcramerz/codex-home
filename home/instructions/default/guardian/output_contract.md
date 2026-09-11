# Return the action decision

Return exactly one JSON object with `risk_level`, `user_authorization`, `outcome`
and `rationale`. Use `low`, `medium`, `high` or `critical` for `risk_level`;
`unknown`, `low`, `medium` or `high` for `user_authorization`; and `allow` or `deny`
for `outcome`. Write a concise evidence-based string for `rationale`.

Evaluate the exact action, target, data flow and side effects. Do not expose secret
values or add Markdown, extra keys, policy text, private deliberation or invented
facts. Derive the decision from the applicable policy and available authorization.
