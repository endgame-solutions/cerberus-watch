## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-14 - [Missing keyboard focus indicators]
**Learning:** Found a pattern where standalone HTML heads (like Athena) using custom interactive elements lack default keyboard `:focus-visible` styles, hindering navigation for users relying on keyboards or assistive tech.
**Action:** Always verify keyboard accessibility (`Tab` navigation) and explicitly define `:focus-visible` styles for interactive elements in custom CSS files.

## 2025-03-15 - [Missing semantic forms and SPA focus management]
**Learning:** Identified that pseudo-forms (groupings of inputs without semantic `<form>` tags) prevent default keyboard submission behavior (e.g., using the `Enter` key). Additionally, when using custom SPA-like view transitions (toggling `.hidden` classes), screen readers and keyboard users lose their place because focus isn't intentionally managed.
**Action:** Always wrap input groupings with semantic `<form>` tags and add `onsubmit="event.preventDefault()"` to handle submissions via JS. For SPA transitions, explicitly manage focus by setting `tabindex="-1"` and calling `.focus()` on the primary heading (`<h1>`) of the newly revealed screen, with `outline: none` to prevent a distracting focus ring.
