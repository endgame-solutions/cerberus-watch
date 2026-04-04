## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-14 - [Missing keyboard focus indicators]
**Learning:** Found a pattern where standalone HTML heads (like Athena) using custom interactive elements lack default keyboard `:focus-visible` styles, hindering navigation for users relying on keyboards or assistive tech.
**Action:** Always verify keyboard accessibility (`Tab` navigation) and explicitly define `:focus-visible` styles for interactive elements in custom CSS files.

## 2025-03-16 - [Missing visual feedback on form submission]
**Learning:** When primary forms submit via JS redirects that process quickly, failing to provide immediate visual feedback (disabling the button and showing a spinner) can lead to user confusion or double-clicks.
**Action:** Always disable primary action buttons and show a loading spinner on submission. Adding a slight delay before local redirects ensures the visual feedback is perceptible and the action feels stable.