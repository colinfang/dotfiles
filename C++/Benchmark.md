# `gprof`

- Compile & link with `-pg` in `gcc`.
- [Issue] Need to static link with `-no-pie`
    - Perhaps doesn't need `-fno-pie` for compiling
    - <https://stackoverflow.com/questions/42620074/gprof-produces-empty-output>

```bash
# Run it once to generate `gmon.out`
./main
# Read result
gprof ./main
```


# `perf`

```bash
apt install linux-tools-$(uname -r)
perf stats ./benchmark.out
```

- Useful to see "branch-misses", "page-faults"
- For WSL2
    - `apt install linux-tools-generic`
    - `/usr/lib/linux-tools/5.15.0-136-generic/perf stats ...`
        - Because `/usr/bin/perf` script doesn't work for WSL2 kernel name
    - <https://stackoverflow.com/questions/60237123/is-there-any-method-to-run-perf-under-wsl>
- Reference
    - <https://www.youtube.com/watch?v=nXaxk27zwlk>
        - CppCon 2015: Chandler Carruth "Tuning C++"
