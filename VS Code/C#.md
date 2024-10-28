# C# Dev Kit

- <https://github.com/dotnet/vscode-csharp>
- .Net Install Tool is auto installed.
    - .NET runtime is bundled
    - "Command Palette" -> "Install New .Net SDK"
        - [Issue] Not support WSL
    - Local `dotnet` is used if available.
        - Otherwise it would use e.g. `.vscode-server/data/User/globalStorage/ms-dotnettools.vscode-dotnet-runtime/.dotnet/8.0.6~x64/dotnet`
        - [Tip] Check C# extension output
- C# extension is auto installed.
- Formatting
    - `.editorconfig` is ignored for formatting unless EditorConfig extension is installed.
- Lint
    - `.editorconfig` is respected
- Project `.csproj`
    - Click on Solution Explorer under File Explorer to see all recognized projects.
    - `bin/` & `obj/` are auto generated for each `.csproj` found.
- Script `.csx`
    - A lot of `using` are auto imported
        - <https://github.com/filipw/dotnet-script/blob/1.3.1/src/Dotnet.Script.Core/ScriptCompiler.cs#L42>
    - [Issue] Not supported
        - <https://github.com/dotnet/vscode-csharp/issues/6411>
        - Only work if using Omnisharp
            - `"dotnet.server.useOmnisharp": true`
            - `"dotnet.preferCSharpExtension": true`
- Tests
    - Test projects are recognized
        - Run `dotnet test` to see why a test isn't included
    - Click on "Testing" in activity bar (left most) to show test explorer
    - Click on "Test Results" tab next to Terminal to see STDOUT


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
