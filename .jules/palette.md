## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-14 - [Missing keyboard focus indicators]
**Learning:** Found a pattern where standalone HTML heads (like Athena) using custom interactive elements lack default keyboard `:focus-visible` styles, hindering navigation for users relying on keyboards or assistive tech.
**Action:** Always verify keyboard accessibility (`Tab` navigation) and explicitly define `:focus-visible` styles for interactive elements in custom CSS files.

## 2026-04-10 - Provide Visual Feedback on Instantaneous Redirects
**Learning:** For instantaneous, synchronous local redirects (like updating `window.location.href`), setting a loading state on a button may happen too fast for the user to perceive it, or it may not render at all before the browser unloads the page.
**Action:** Wrap the redirect in a minimal timeout (e.g., `setTimeout(..., 500)`) so the visual loading state is perceptible. This provides better feedback that an action was registered and prevents accidental double-clicks.
