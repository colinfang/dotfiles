# Benchmark

- {Python High Performance 2nd} - 1: Benchmarking and Profiling
- `%time`: Call bash `time` underneath
- `%timeit` & `%%timeit`: Call `timeit` underneath
- `time.time() -> float`
    - Unit is seconds
    - Resolution is reduced from 15.6 ms to 1 us on Windows since v3.13
        - <https://docs.python.org/3/whatsnew/3.13.html#time>
    - `time.time_ns() -> int` can be used to avoid the precision loss caused by the `float`
- `time.perf_counter() -> float`
    - Unit is seconds
    - Monotonic, only difference makes sense
    - The clock is the same for all processes
    - It uses a clock with the highest available resolution to measure a short duration.
        - Use the same clock as `time.monotonic()` since v3.13
- TODO: Check voluntary context switches
    - <https://pythonspeed.com/articles/custom-python-profiler/>



```python
%timeit pass
# 8.26 ns ± 0.12 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)
```

# `timeit.timeit`

```python
timeit('q.append(1)', 'from collections import deque; q = deque()')
# 0.1
```

```bash
# Options must come before the statement.
python -m timeit -s 'from collections import deque; q = deque()' 'q.append(1)'
# 10000000 loops, best of 3: 0.0887 usec per loop

python -m timeit -s 'from collections import deque; q = deque()' -v 'q.append(1)'
# 10 loops -> 2.26e-06 secs
# 100 loops -> 9.59e-06 secs
# 1000 loops -> 8.6e-05 secs
# 10000 loops -> 0.000883 secs
# 100000 loops -> 0.0113 secs
# 1000000 loops -> 0.0899 secs
# 10000000 loops -> 0.89 secs
# raw times: 0.889 0.887 0.889
# 10000000 loops, best of 3: 0.0887 usec per loop
```

- <https://docs.python.org/3/library/timeit.html>
- `timeit` will automatically determine the number of repetitions only when cli is used.
- GC is temporarily turned off during the timing.
- `timeit.default_timer` is `time.perf_counter()`
- `timeit(stmt='pass', setup='pass', number=1_000_000)`
    - Return wall clock time measured in seconds, hence ms per iteration by default number of repetitions.


# cProfile

- Deterministic profiling
- `python -m cProfile foo.py`
    - `-s tottime`
        - `-s cumtime`
    - `-o tmp.perf`
- `%prun` & `%%prun` - IPython magic.

```python
import cProfile
profiler = cProfile.Profile()
profiler.enable()
try:
    main()
finally:
    profiler.disable()
    profiler.dump_stats('tmp.perf')
```


# GreenletProfiler

- Greenlet aware profiler.
    - Normal profiler would get confused when a function A yields to another function B.
- <https://emptysqua.re/blog/greenletprofiler/>


# pyinstrument

- <https://github.com/joerick/pyinstrument/>
- Statistical profiling
- Wall-clock time, instead of CPU time.

```python
from pyinstrument import Profiler
profiler = Profiler()
profiler.start()
...
profiler.stop()
print(profiler.output_text(unicode=True, color=True))
```


# line_profiler

- <https://github.com/rkern/line_profiler>
- `kernprof -lv foo.py`
    - `-v` - Display the result in terminal instead of writing to a file.
    - Add `@profile` to the functions to be profiled.
    - No need to import `profile` function.
- `%load_ext line_profiler`
- `%lprun`
    - `%lprun -f my_fun benchmark()`
    - Need to pass in the functions to be profiled instead of using `@profile`.
    - The functions can be `A.foo` or `a.foo`.
    - Multiple `-f` options may be used.


# memory_profiler

- <https://github.com/fabianp/memory_profiler>
- `conda install memory_profiler`
    - Install psutil to make it faster.
- `python -m memory_profiler foo.py`
    - Add `@profile` to the functions to be profiled.
    - No need to import `profile` function.
- `%load_ext memory_profiler`
- `%mprun` & `%%mprun`
    - `%mprun -f my_fun benchmark()`
    - Need to pass in the functions to be profiled instead of using `@profile`.
    - Multiple `-f` options may be used.
- `%memit` & `%%memit`
    - Output the peak memory during execution (affected by the memory used so far) & overall memory increment after execution.

```python
%memit range(1000000)
# peak memory: 52.10 MiB, increment: 31.08 MiB
```

## `mprof`

- `mprof list` - List all recorded memory usage files.
- `mprof clean` - Remove all recorded memory usage files.
- `mprof run cmd`
    - `--include-children` - Combine memory usage of all the children and the parent.
    - `--multiprocess` - Track each child independently of the main process.
- `mprof run foo.py` - Track functions, `@profile` is required.

```bash
# Get full memory usage reports over time.
mprof run python foo.py
mprof plot

```


# RunSnakeRun

```bash
apt install runsnakerun
/usr/bin/python /usr/bin/runsnake
```


# System Usage

- <https://pythonhosted.org/psutil/>

## `Process`

- `psutil.Process(os.getpid())` - Get a `Process`.
- `.cpu_percent(interval?, percpu=False)`
    - If `interval > 0`, it is blocking & measures the CPU time during the interval.
    - If `interval == 0 or interval is None`, it is non-blocking & measure the CPU time since the last call.
    - If `percpu == False`, the system CPU time is measured so that the return may be greater than 100.
    - If `percpu == True`, a list of CPU usages is returned.
- `.memory_info()` - Return a named tuple with variable fields e.g. `rss` depending on the platform.
    - Unit is byte.
    - `.memory_info().rss / float(2 ** 20)` - Get memory used in MB.

```python
def get_system_usage(pid=None):
    if pid is None:
        pid = os.getpid()
    process = psutil.Process(pid)
    # Unit in MB.
    mem = process.memory_info().rss / float(2 ** 20)
    # Average cpu usage since last call.
    cpu = process.cpu_percent()
    return cpu, mem
```


```python
# Python wrapper for `getrsuage`.
resource.getrusage(resource.RUSAGE_SELF) / 1024
```
