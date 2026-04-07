## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-14 - [Missing keyboard focus indicators]
**Learning:** Found a pattern where standalone HTML heads (like Athena) using custom interactive elements lack default keyboard `:focus-visible` styles, hindering navigation for users relying on keyboards or assistive tech.
**Action:** Always verify keyboard accessibility (`Tab` navigation) and explicitly define `:focus-visible` styles for interactive elements in custom CSS files.

## 2025-04-07 - Synchronous Redirect Feedback
**Learning:** Fast local redirects (like `window.location.href = 'index.html'`) without visual feedback can feel abrupt or like the button click didn't register if there is even a slight micro-stutter in the browser navigation.
**Action:** Always provide visual feedback (e.g., a loading spinner and disabling the submit button) for primary form submissions, even for fast local redirects, to prevent double-clicks and make actions feel intentional.

## 2025-04-07 - Disabled Hover States
**Learning:** Applying a generic `:hover` state to buttons (e.g., `.btn-primary:hover`) can inadvertently override disabled states if not carefully scoped, causing disabled buttons to transform or change color when hovered.
**Action:** When adding hover effects, explicitly chain `:not(:disabled)` (e.g., `.btn-primary:not(:disabled):hover`) to ensure disabled elements remain static.
