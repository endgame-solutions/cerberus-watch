## 2024-05-24 - Avoid per-request instantiation of static data structures
**Learning:** Re-instantiating large static dictionaries (like mock databases) in a class `__init__` method can cause unnecessary overhead, especially if the class is instantiated on every request.
**Action:** Move static data out of `__init__` into class-level attributes to initialize them only once and share across instances. This resulted in a >50% performance improvement in instantiation time in benchmarks.

## 2024-06-25 - Throttle high-frequency event listeners in frontend components
**Learning:** Binding synchronous, state-updating functions directly to high-frequency events like `document.onmousemove` can block the main thread and drastically increase CPU overhead, especially when these functions invoke methods like `setTimeout` or `clearTimeout` hundreds of times per second.
**Action:** Always wrap high-frequency DOM event listeners in a throttle or debounce utility. This ensures the handler fires at a controlled, performant rate (e.g., once every 1000ms), preserving responsiveness and saving resources.
