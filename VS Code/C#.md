
- <https://github.com/OmniSharp/omnisharp-vscode>
- Require .NET SDK
    - {C#/Install.md}
    - No need to install `dotnet-script`
- Enable `omnisharp.enableRoslynAnalyzers` for code analysis
    - {:Lint/C#.md}

# Project Mode

- Generate `bin/` & `obj/` for each `.csproj` found, resulting with duplicate attribute potentially.
- `omnisharp.json` is not needed

# Script Mode

- Require `omnisharp.json`
- `.csproj` is not needed
- A lot of `using` are auto imported
    - <https://github.com/filipw/dotnet-script/blob/1.3.1/src/Dotnet.Script.Core/ScriptCompiler.cs#L42>

# `launch.json`

```json
{
    "name": ".NET Script WSL",
    "type": "coreclr",
    "request": "launch",
    "program": "dotnet",
    "args": [
        "exec",
        // Use WSL dotnet to load Windows dll
        "/mnt/c/Users/colin/.dotnet/tools/.store/dotnet-script/1.3.1/dotnet-script/1.3.1/tools/net6.0/any/dotnet-script.dll",
        "${file}"
    ],
    "cwd": "${workspaceFolder}",
    "stopAtEntry": false
}
```