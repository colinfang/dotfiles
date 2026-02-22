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
- Use custom CLI path
    - [Example] `dotnet run -c Release -- --cli "C:\Tools\dotnet.exe"`
