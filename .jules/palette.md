## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-14 - [Missing keyboard focus indicators]
**Learning:** Found a pattern where standalone HTML heads (like Athena) using custom interactive elements lack default keyboard `:focus-visible` styles, hindering navigation for users relying on keyboards or assistive tech.
**Action:** Always verify keyboard accessibility (`Tab` navigation) and explicitly define `:focus-visible` styles for interactive elements in custom CSS files.

## 2025-03-25 - [Missing visual feedback on form submission]
**Learning:** Primary forms (like login) redirect so fast locally that users can double-click and cause unexpected behavior. This creates a clunky, non-intentional interaction model.
**Action:** Always provide visual feedback (e.g., a loading spinner and disabling the submit button) for primary form submissions, even for fast local redirects, to prevent double-clicks and make actions feel intentional.
