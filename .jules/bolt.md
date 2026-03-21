## 2024-05-24 - Avoid per-request instantiation of static data structures
**Learning:** Re-instantiating large static dictionaries (like mock databases) in a class `__init__` method can cause unnecessary overhead, especially if the class is instantiated on every request.
**Action:** Move static data out of `__init__` into class-level attributes to initialize them only once and share across instances. This resulted in a >50% performance improvement in instantiation time in benchmarks.

## 2024-03-14 - Throttling inactivityTimer on mousemove
**Learning:** Attaching an unthrottled `resetTimer` function (which invokes `clearTimeout` and `setTimeout`) directly to `document.onmousemove` can cause significant performance degradation due to rapid, successive calls and garbage collection when the user moves the mouse.
**Action:** Always throttle or debounce event listeners for high-frequency events like `mousemove`, `scroll`, or `resize` to reduce unnecessary CPU overhead and prevent main thread blocking.

## 2024-05-24 - Thread Pool Offloading in FastAPI
**Learning:** Defining endpoints that perform strictly synchronous operations as `async def` in FastAPI forces them to execute on the main event loop, causing requests to block the application's concurrency and degrading throughput.
**Action:** Remove the `async` keyword and declare purely synchronous endpoints as standard `def` to allow FastAPI to automatically offload their execution to a separate thread pool.
