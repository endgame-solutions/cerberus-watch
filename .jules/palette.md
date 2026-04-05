## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-14 - [Missing keyboard focus indicators]
**Learning:** Found a pattern where standalone HTML heads (like Athena) using custom interactive elements lack default keyboard `:focus-visible` styles, hindering navigation for users relying on keyboards or assistive tech.
**Action:** Always verify keyboard accessibility (`Tab` navigation) and explicitly define `:focus-visible` styles for interactive elements in custom CSS files.

## 2026-04-05 - Add loading state to fast local redirects
**Learning:** Fast local redirects (like updating `window.location.href` immediately after synchronous JS validation) can happen so fast that users double-click buttons if there's no visual change, or conversely, feel jarring. Adding a brief artificial loading state (e.g., spinner, disabled button, 800ms delay) prevents duplicate submissions and makes the authentication action feel more secure and intentional.
**Action:** Always provide visual feedback (e.g., a loading spinner and disabling the submit button) for primary form submissions, even for fast local redirects, to prevent double-clicks and make actions feel intentional.
