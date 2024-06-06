# Roslyn Code Analysis

- <https://docs.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-options>
- [My config](</.editorconfig>)
- Severity level
    - default
    - none
    - silent
        - Grey out
            - TODO: Check if this is correct
        - Not appear in "Problems"
    - suggestion
    - warning
    - error
- [Issue] No concise syntax to ignore a line
- Some options
    - Remove unused parameter (IDE0060)
        - `_` or `_1` does not flag
        - `_a` does
        - <https://docs.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/ide0060>

```c#
// Ignore a warning temporarily
// Remark, "warning" below is a keyword, not a severity level
#pragma warning disable IDE0060
void f(int x) {
#pragma warning restore IDE0060
}
```
