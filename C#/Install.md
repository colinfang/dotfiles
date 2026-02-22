# Download SDK & CLI

```bash
# install package repository & keys
# ppa is needed only for new sdk on old ubuntu
add-apt-repository ppa:dotnet/backports
apt install dotnet-sdk-10.0
dotnet --info
```

- <https://dotnet.microsoft.com/en-us/download/dotnet/sdk-for-vs-code>
- Built-in with VS, required by VS Code
- Installed into `~/.dotnet`


# Run Script From .NET CLI via `dotnet-script`

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
- This is no longer needed as we can run single `.cs` file directly.


# Run Single `.cs` File From .NET CLI


- <https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/>
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
# Remove relevant files in `bin/` for the particular target w.r.t. .csproj
dotnet clean

```


- <https://code.visualstudio.com/docs/languages/dotnet>
- `obj/` is like cache, not important
    - Delete it manually if there is weird errors e.g. "GlobalUsings.g.cs specified multiple times"
- Generated `.csproj` is minimal
    - Can be renamed anything except for empty.
    - [Example](<csproj>)
- `dotnet run`
    - `--project my_project.csproj`
        - Need to specify project path if there are more than 1
    - `--file hello.cs`
        - For single file script


# MSTest

- [Example](<test_csproj>)
- `dotnet test` to run all tests
- A test project can appear as a normal executable.
    - Add `<OutputType>Exe</OutputType>` & `<GenerateProgramFile>false</GenerateProgramFile>` to `<PropertyGroup>`
    - Add `public static void Main(string[] args)` to code
    - Run tests doesn't trigger `Main`
- Test class & methods need to be `public`



# Working Environment

- [VS Code](</VS Code/C%23.md>)
- [Lint](Lint.md)


# Visual Studio

- "Start without debugging" <kbd>Ctrl + F5</kbd> would prompt "press any key to continue" before quit console.
- "Start debugging" & "Start without debugging" would trigger build
    - [Default] Debug -> Projects and Solutions -> Build and Run -> "On Run, when projects are out of date" is set to "Always Build"
- Config
    - Debug -> Options -> Text Editor -> C# -> Advanced
        - ☑️ "Underline reassigned variables"
        - ☑️ everything in "Inline Hints"
    - Debug -> Options -> Projects & Solutions -> General
        - ☑️ "Track active item in solution explorer"
            - So that clicking on a file tab auto selects the file in solution explorer
- If breakpoint doesn't work
    - Debug -> Options -> Debugging -> General
        - ❌ "Enable just my code"
        - ❌ "Require source files to exactly match the original version"


# `.csproj`

- [Example]
    - [Project](<csproj>)
    - [Test project](<test_csproj>)
- `PropertyGroup`
    - `<CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>`
        - Copy directly imported dll, dll from nuget packages, dll referenced by dependencies to `bins` folder.
        - <https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props#copylocallockfileassemblies>
    - C# language version
        - If unspecified, it is the latest version that the compiler supports & compatible with the specified runtime framework.
        - `preview` or `latest` would ignore runtime compatibility.
        - <https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning>
- `ItemGroup`
    - <https://learn.microsoft.com/en-us/visualstudio/msbuild/common-msbuild-project-items>
    - `<Content Include="ExtraData\**"><CopyToOutputDirectory>Always</CopyToOutputDirectory></Content>`
        - Copy any files under `ExtraData` folder to output folder.
    - `<InternalsVisibleTo Include="ProjectName.Tests" />`
        - The specified friendly assembly would gain access to all internal members of this project.
        - [Tip] Useful to declare the test project as a friend.
        - It doesn't require the friendly assembly in the solution.
            - E.g. Can publish as a nuget package and any assembly that has name matching the specified string would be able to visit its internal members.
    - To include or exclude files
        - `<Compile Remove="ToIgnore/**" />`
        - `<Compile Include="**/test*.cs" />`
            - Need to also set `<EnableDefaultItems>false</EnableDefaultItems>` in `PropertyGroup`
            - Otherwise could hit "Duplicate items were included" because by default all files in the folders are already included
                - <https://learn.microsoft.com/en-us/dotnet/core/tools/sdk-errors/netsdk1022>


# Good Online Tools

- <https://sharplab.io/>
    - See IL & assembly & de-compiled C# from IL
    - [Issue] Not many choices of .NET versions
- <https://dotnetfiddle.net/>
    - Online code playground & IL
- <https://www.godbolt.org/>
    - See assembly & output in various compilers
    - [Issue] No IL
    - <https://github.com/compiler-explorer/compiler-explorer/pull/3168>
        - Compiler options
