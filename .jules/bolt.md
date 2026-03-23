## 2024-05-24 - Avoid per-request instantiation of static data structures
**Learning:** Re-instantiating large static dictionaries (like mock databases) in a class `__init__` method can cause unnecessary overhead, especially if the class is instantiated on every request.
**Action:** Move static data out of `__init__` into class-level attributes to initialize them only once and share across instances. This resulted in a >50% performance improvement in instantiation time in benchmarks.

## 2024-03-14 - Throttling inactivityTimer on mousemove
**Learning:** Attaching an unthrottled `resetTimer` function (which invokes `clearTimeout` and `setTimeout`) directly to `document.onmousemove` can cause significant performance degradation due to rapid, successive calls and garbage collection when the user moves the mouse.
**Action:** Always throttle or debounce event listeners for high-frequency events like `mousemove`, `scroll`, or `resize` to reduce unnecessary CPU overhead and prevent main thread blocking.

## 2024-05-25 - Offload synchronous endpoints to thread pool
**Learning:** Defining FastAPI endpoints with `async def` when they contain no `await` calls forces synchronous, CPU-bound operations to run directly on the main asynchronous event loop, blocking all other requests and significantly degrading concurrency and overall performance.
**Action:** Always define endpoints that perform synchronous or blocking operations without `await` calls as standard `def` functions instead of `async def`. This offloads the execution to an external thread pool managed by FastAPI/Starlette, preventing the main event loop from being blocked.
