## 2025-03-05 - Visual Feedback for Fast Local Redirects
**Learning:** Even for fast local storage operations or fast redirects, forms missing a loading spinner or disabled state lead to double-clicks and a lack of intentionality in the UI feedback.
**Action:** Always add visual loading feedback (like a spinner and disabled button) for primary form submissions and artificial delays if needed, even if the underlying action is near-instant, to ensure the action feels intentional to the user.
