## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-14 - [Missing keyboard focus indicators]
**Learning:** Found a pattern where standalone HTML heads (like Athena) using custom interactive elements lack default keyboard `:focus-visible` styles, hindering navigation for users relying on keyboards or assistive tech.
**Action:** Always verify keyboard accessibility (`Tab` navigation) and explicitly define `:focus-visible` styles for interactive elements in custom CSS files.

## 2026-03-28 - [SPA view transition focus management and keyboard submission]
**Learning:** In vanilla JS single-page applications (like the Athena head), toggling CSS `.hidden` classes for view transitions causes screen readers to lose context. Furthermore, custom form-like UI patterns often rely purely on JS `onclick` and lack semantic `<form>` wrappers, breaking default `Enter` key submission behavior.
**Action:** Always programmatically manage focus during simulated view transitions (e.g., set `tabindex="-1"` and `.focus()` on the newly revealed heading) and wrap input clusters in a `<form>` with a `type="submit"` button.
