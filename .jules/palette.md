## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-14 - [Missing keyboard focus indicators]
**Learning:** Found a pattern where standalone HTML heads (like Athena) using custom interactive elements lack default keyboard `:focus-visible` styles, hindering navigation for users relying on keyboards or assistive tech.
**Action:** Always verify keyboard accessibility (`Tab` navigation) and explicitly define `:focus-visible` styles for interactive elements in custom CSS files.

## 2025-02-28 - Add loading state to login form
**Learning:** Immediate local redirects (like updating `localStorage` and `window.location.href`) occur too fast for users to perceive visual feedback (e.g., disabled buttons, loading spinners). Without intentional delays, users may double-click out of uncertainty, leading to a clunky experience.
**Action:** When implementing synchronous, instantaneous actions, always wrap the action in a minimal timeout (e.g., `setTimeout(..., 500)`) after disabling inputs and showing visual loading feedback to make the submission feel intentional and secure.
