## 2024-05-24 - Avoid per-request instantiation of static data structures
**Learning:** Re-instantiating large static dictionaries (like mock databases) in a class `__init__` method can cause unnecessary overhead, especially if the class is instantiated on every request.
**Action:** Move static data out of `__init__` into class-level attributes to initialize them only once and share across instances. This resulted in a >50% performance improvement in instantiation time in benchmarks.
