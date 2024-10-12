# Download SDK & CLI

```bash
# install package repository & keys
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb
dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb

apt install dotnet-sdk-8.0
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
- `<CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>`
    - This would copy directly imported dll, dll from nuget packages, dll referenced by dependencies to `bins` folder.
    - <https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props#copylocallockfileassemblies>
