# ♿ Accessibility Guidance

The applications use Streamlit's standard widgets. That does not by itself establish WCAG conformance.

## Authoring rules
- Give each input an unambiguous label and clear instructions.
- Use descriptive headings and concise explanatory text.
- Do not encode success, failure or class meaning through color alone.
- Keep tables and displayed arrays understandable at zoom and narrow widths.
- Provide text explanations for visual or numerical outputs.
- Avoid flashing, auto-refreshing or unnecessary motion.

## Manual checks
| Area | Check |
|---|---|
| Keyboard | Every widget can be reached and operated |
| Focus | Focus order is logical and visible |
| Labels | Screen readers announce each widget's purpose |
| Errors | Invalid input is explained in text |
| Contrast | Text and controls remain perceivable |
| Zoom | Page remains usable at 200% |
| Tables | Headers and values are understandable |

## Scope
This is a review guide, not an accessibility audit or compliance certification. Record real findings in the accessibility review template.
