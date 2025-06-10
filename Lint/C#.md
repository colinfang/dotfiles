# Roslyn Code Analysis

- <https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-options>
- Respected by Visual Studio & VS Code C# Dev Kit
- [My config](</.editorconfig>)
- Severity level
    - default
    - none
        - Cursor hover no display
        - No special syntax highlighting
    - silent
        - No IDE suggestions (e.g. 3 gray dots under the first 2 characters)
        - Not appear in error lists / problems
        - Grey out in syntax highlighting
        - Cursor hover display the issues & suggestions
    - suggestion
        - Has IDE suggestions
        - Appear in error lists / problems
    - warning
    - error
- [Issue] No concise syntax to ignore a line
- Some options
    - Remove unused parameter (IDE0060)
        - `_` or `_1` does not flag
        - `_a` does
        - <https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/ide0060>

```c#
// Ignore a warning temporarily
// Remark, "warning" below is a keyword, not a severity level
#pragma warning disable IDE0060
void f(int x) {
#pragma warning restore IDE0060
}
```
