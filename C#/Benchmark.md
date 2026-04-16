# *BenchmarkDotNet*

- It prevents from inlining of the benchmark by wrapping it with a delegate.
- [Issue] Display a benchmark target return value in a column
    - <https://github.com/dotnet/BenchmarkDotNet/issues/784>
- `[InliningDiagnoser]`
    - JIT is capable of emitting events for much of its activity, including reporting on any successful or failed inlining operations
    - `[InliningDiagnoser]` listens to those events and reports them as part of the benchmarking results.
    - [Issue] Only works on Windows, because it relies on ETW
    - <https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-9/>
    - [Example] `[InliningDiagnoser(allowedNamespaces: ["Benchmarks"])]`
- `[DisassemblyDiagnoser]`
    - Output in `BenchmarkDotNet.Artifacts/results/xxx-asm.md`
- `[HardwareCounters(HardwareCounter.BranchMispredictions, HardwareCounter.BranchInstructions)]`


# CLI

```c#
public static void Main(string[] args) {
    BenchmarkRunner.Run<MyBenchmark>(args: args);
    // This allows to switch different benchmark class from CLI
    // BenchmarkSwitcher.FromAssembly(typeof(Program).Assembly).Run(args);
}
```

- [Example] `dotnet run -c Release -- --list tree`
    - `--list tree|flat`
        - List all available benchmarks
    - `--filter *MyBenchmark.Method1*`
        - Only run the filtered classes / methods
        - Match full namespace as displayed via `--list`
    - `--runtimes net9.0 net10.0`
        - If multiple runtimes are specified, they also need to appear in `TargetFrameworks` from `PropertyGroup` of `.csproj`
    - `--cli "C:\Tools\dotnet.exe"`
        - Use custom CLI path
