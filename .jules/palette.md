## 2025-03-13 - [Missing form associations and ARIA labels]
**Learning:** Found an accessibility issue pattern where inputs in the admin panel lack corresponding `for` and `id` associations with labels, and a disguised search input missing an `aria-label`. This hinders screen reader accessibility.
**Action:** Always add `for` and `id` attributes to link labels and inputs, and use `aria-label` for disguised or icon-only inputs.

## 2025-03-15 - [Missing semantic form wrappers]
**Learning:** Discovered an accessibility issue pattern where pseudo-forms (groupings of `<div>` and `<input>` tags) lack a semantic `<form>` wrapper. This prevents users from utilizing default keyboard submission behavior (e.g. the `Enter` key) after typing in input fields.
**Action:** Always wrap input groupings with a `<form>` element, ensure default event prevention (`event.preventDefault()`) when attaching custom submit handlers, and set the submit button's type to `"submit"`.
