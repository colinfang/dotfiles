# Download SDK & CLI

```bash
# install package repository & keys
# ppa is needed only for new sdk on old ubuntu
add-apt-repository ppa:dotnet/backports
apt install dotnet-sdk-9.0
dotnet --info
```

- <https://dotnet.microsoft.com/en-us/download/dotnet/sdk-for-vs-code>
- Built-in with VS, required by VS Code
- Installed into `~/.dotnet`


# Run Script From .NET CLI

```bash
# Install script tool in order to run script using CLI
dotnet tool install -g dotnet-script
# See installed tools
dotnet tool list -g

# This is only needed for Linux
# Add the following to to .bashrc in order to use script
export PATH=$PATH:$HOME/.dotnet/tools/

dotnet script my_script.csx
# Release build
dotnet script my_script.csx -c release
```

- <https://github.com/filipw/dotnet-script>
- Windows native SDK is faster than WSL SDK for release build
    - [Convention] Use `dotnet.exe` instead of WSL `dotnet`

# CLI Quick Start

```bash
mkdir repo
# Create a console application
dotnet new console
# `Program.cs`, `obj/`, `repo.csproj` are generated
dotnet run -c release
# `bin/` is generated
```


- <https://code.visualstudio.com/docs/languages/dotnet>
- `obj/` is like cache, not important
- Generated `.csproj` is minimal
    - Can be renamed anything except for empty.
    - [Example](<csproj>)

# MSTest

- [Example](<test_csproj>)
- `dotnet test` to run all tests
- A test project can appear as a normal executable.
    - Add `<OutputType>Exe</OutputType>` & `<GenerateProgramFile>false</GenerateProgramFile>` to `<PropertyGroup>`
    - Add `public static void Main(string[] args)` to code
    - Run tests doesn't trigger `Main`


# Working Environment

- [VS Code](</VS Code/C%23.md>)
- [Lint](</Lint/C%23.md>)


# Visual Studio

- Start without debugging <kbd>Ctrl + F5</kbd> would prompt "press any key to continue" before quit console.
- Config
    - Debug -> Options -> Text Editor -> C# -> Advanced
        - Check "Underline reassigned variables"
        - Check everything in "Inline Hints"
    - Debug -> Options -> Projects & Solutions -> General
        - Check "Track active item in solution explorer"
            - So that clicking on a file tab auto selects the file in solution explorer
- If breakpoint doesn't work
    - Debug -> Options -> Debugging -> General
        - Uncheck "Enable just my code"
        - Uncheck "Require source files to exactly match the original version"

# `.csproj`

- [Example]
    - [Project](<csproj>)
    - [Test project](<test_csproj>)
- `PropertyGroup`
    - `<CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>`
        - This would copy directly imported dll, dll from nuget packages, dll referenced by dependencies to `bins` folder.
        - <https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props#copylocallockfileassemblies>
    - C# language version
        - [Example] Build a project that targets .NET 6 from the current version of VS 2022
            - C# 12 if `LangVersion` is set to `default`
            - C# 10 if `LangVersion` is unspecified
        - <https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning>
