## TASK
Generate a commit message describing the changes in this git diff.

## GUIDELINES
- Use imperative mood ("Add feature" not "Added feature")
- Prioritize functional impacts over files changed
- Identify patterns suggesting unified purpose across changes
- Consider relationships between changes when determining significance
- Limit body to ~200 characters unless complexity requires more detail
- Omit body entirely if the subject line captures the change adequately

## EMOJI SUPPORT
{% if use_emojis %}
Emoji prefixes are ENABLED - include appropriate emoji before the commit type
(e.g., ✨ feat: Add new feature, 🐛 fix: Resolve issue)
{% else %}
Emoji prefixes are DISABLED - do not include any emojis in the commit message
{% endif %}

## INPUT
File statuses:
{{ status }}

Diff:
{{ diff }}
