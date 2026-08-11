# HTML
Purpose: tell the Codex coding agent how to use `docs/lang/html.md` as a runtime-pack surface and when to stop browsing.
Guidance for accessible, maintainable HTML.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/lang/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must prefer semantic elements (`header`, `main`, `nav`, `section`).
- Ensure accessible labels for forms and controls.
- You must validate color contrast and keyboard navigation.

## Safety
- Avoid inline scripts when possible.
- Sanitize user-generated HTML; never trust raw input.

See also:
- `overview.md`
- `../web/htmx.md`
- `$CODEX_HOME/templates/web/html-static/`
- `$CODEX_HOME/snippets/web/html/index.html`
- You must use skill web-html.
- `$CODEX_HOME/index/domains/lang/languages.md`
- `$CODEX_HOME/index/domains/lang/html.md`
