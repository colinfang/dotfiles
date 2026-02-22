# Built-in Syntax Highlight (TextMate)

- JSON
    - <https://code.visualstudio.com/docs/languages/json>
    - [Default] Filenames with suffix `jsonc` or `settings.json` & `tasks.json` & `launch.json` are considered "JSON with Comments" mode.
- C++
    - <https://github.com/microsoft/vscode/blob/master/extensions/cpp/cgmanifest.json>
        - VS Code built-in version
    - <https://github.com/jeff-hykin/cpp-textmate-grammar>
        - "Better C++ Syntax" extension
    - Tag for the repository is not the version for the extension.
        - <https://github.com/jeff-hykin/better-cpp-syntax/blob/master/package.json>
- C#
    - <https://github.com/microsoft/vscode/blob/main/extensions/csharp/cgmanifest.json>
        - VS Code built-in version
    - <https://github.com/dotnet/csharp-tmLanguage>

# Semantic Highlight

- Config
    - `editor.semanticHighlighting.enabled`
    - Check "semantic token type" in "Developer: Inspect Editor Token and Scopes"
- C#
    - [Issue] Bracket pair colorization incorrectly renders `>` in C# markdown code fence
        - <https://github.com/microsoft/vscode/issues/279576>
        - [Workaround] Customize brackets in `editor.language.colorizedBracketPairs`
- vscode-clangd
    - [Issue] Semantic highlighting is missing some tokens
        - <https://github.com/clangd/vscode-clangd/issues/326>
        - <https://github.com/clangd/clangd/issues/1115>
- Python
- Syntax Highlighter
    - A few languages
    - Based on Tree-Sitter

# Inlay Hints

- Features
    - Display inline type hints
    - Display inline parameter name hints
        - Suppress hints for parameters that match argument name.
            - [Feature request] Pylance
- vscode-clangd
    - <https://clangd.llvm.org/config#inlayhints>
    - Added in v0.1.12 & clangd-14
- C#
    - `csharp.inlayHints`
    - `dotnet.inlayHints`
- Python via Pylance
    - `python.analysis.inlayHints`
- TypeScript
    - `typescript.inlayHints`
    - `javascript.inlayHints`
- Visual Studio
    - Options -> Text Editor -> C# -> Advanced
