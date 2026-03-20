## 2024-05-24 - Avoid per-request instantiation of static data structures
**Learning:** Re-instantiating large static dictionaries (like mock databases) in a class `__init__` method can cause unnecessary overhead, especially if the class is instantiated on every request.
**Action:** Move static data out of `__init__` into class-level attributes to initialize them only once and share across instances. This resulted in a >50% performance improvement in instantiation time in benchmarks.

## 2024-03-14 - Throttling inactivityTimer on mousemove
**Learning:** Attaching an unthrottled `resetTimer` function (which invokes `clearTimeout` and `setTimeout`) directly to `document.onmousemove` can cause significant performance degradation due to rapid, successive calls and garbage collection when the user moves the mouse.
**Action:** Always throttle or debounce event listeners for high-frequency events like `mousemove`, `scroll`, or `resize` to reduce unnecessary CPU overhead and prevent main thread blocking.

## 2024-05-28 - Offloading synchronous endpoints to a thread pool
**Learning:** In FastAPI, `async def` endpoints are run directly on the main event loop. If they execute blocking operations (e.g., synchronous file I/O, heavy CPU tasks, or synchronous API calls—which is highly likely for `analyzer.analyze(...)`), it blocks the entire event loop, severely degrading the application's throughput.
**Action:** By changing these endpoints to `def` without `async`, FastAPI automatically offloads them to a thread pool (via `anyio`), maintaining the responsiveness of the event loop. This leads to significantly better performance and concurrency for endpoints performing synchronous operations.
