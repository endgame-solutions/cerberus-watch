## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-14 - [Missing keyboard focus indicators]
**Learning:** Found a pattern where standalone HTML heads (like Athena) using custom interactive elements lack default keyboard `:focus-visible` styles, hindering navigation for users relying on keyboards or assistive tech.
**Action:** Always verify keyboard accessibility (`Tab` navigation) and explicitly define `:focus-visible` styles for interactive elements in custom CSS files.

## 2025-03-26 - [Missing focus management in SPA view transitions]
**Learning:** Found an accessibility issue pattern where custom SPA-like view transitions (e.g., toggling `.hidden` classes in standalone heads like Athena) do not manage keyboard focus, leaving screen readers unaware of the new screen context.
**Action:** When implementing custom SPA-like view transitions, explicitly manage focus by setting `tabindex="-1"` and calling `.focus()` on the primary heading (`<h1>`) of the newly revealed screen. Add `outline: none` to the heading's focus state in CSS to prevent a distracting visual focus ring while preserving navigational context for screen readers.
