## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-14 - [Missing keyboard focus indicators]
**Learning:** Found a pattern where standalone HTML heads (like Athena) using custom interactive elements lack default keyboard `:focus-visible` styles, hindering navigation for users relying on keyboards or assistive tech.
**Action:** Always verify keyboard accessibility (`Tab` navigation) and explicitly define `:focus-visible` styles for interactive elements in custom CSS files.
## 2024-05-24 - Login Visual Feedback
**Learning:** Fast local redirects can feel confusing without visual feedback. Adding an artificial loading state before redirecting makes the authentication action feel more secure and intentional, while preventing double-clicks.
**Action:** Always add loading states to primary form submissions.
