## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-14 - [Missing keyboard focus indicators]
**Learning:** Found a pattern where standalone HTML heads (like Athena) using custom interactive elements lack default keyboard `:focus-visible` styles, hindering navigation for users relying on keyboards or assistive tech.
**Action:** Always verify keyboard accessibility (`Tab` navigation) and explicitly define `:focus-visible` styles for interactive elements in custom CSS files.

## 2025-03-16 - [Missing semantic form wrapper prevents keyboard submission]
**Learning:** Found an accessibility issue pattern where pseudo-forms (groupings of inputs and a button) lack a semantic `<form>` wrapper, preventing default keyboard submission (like pressing the `Enter` key) for users.
**Action:** Always wrap grouped inputs and submission buttons in semantic `<form>` tags and add `onsubmit="event.preventDefault()"` to enable default keyboard submission while preserving custom JavaScript handling.
