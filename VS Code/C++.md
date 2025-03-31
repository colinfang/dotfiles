# C++

- Normally it just works if cmake is configured.
- "C/Cpp: Edit Configurations"
- `gcc -E - <<<'#include<stddef.h>' | grep stddef.h` to find the actual headers location.
    - [Example] `/usr/lib/gcc/x86_64-linux-gnu/5/include`
- Put it into the `includePath` or `browse.path`.
- `${workspaceFolder}/**` - Recursively search for headers.
- TODO: `${HOME}` works, why?
    - `${env:HOME}` works as expected.
- [Issue] Cannot get lint work in remote container.
    - [Workaround] Use vscode-clangd
- `c_cpp_properties.json`
    - <https://code.visualstudio.com/docs/cpp/customize-default-settings-cpp>
    ```json
    {
        "configurations": [
            {
                "name": "Linux",
                "includePath": [
                    "${workspaceFolder}/**"
                ],
                "defines": [],
                "cStandard": "c11",
                "cppStandard": "c++17",
                "intelliSenseMode": "${default}",
                // Overrides `includePath` & `defines`
                "compileCommands": "build_home/compile_commands.json"
            }
        ],
        "version": 4
    }
    ```

# vscode-clangd

- Require clangd
- [See also] [clangd](</Lint/C++.md>)
- [Issue] Customize warning level
    - <https://github.com/clangd/vscode-clangd/issues/179>
- [Tip] If something is wrong in clangd and it cannot resolve, delete `.vscode-server`
    - Could be some cache being corrupted.
    - TODO: "Kill VS Code server on host"
        - Remote server doesn't quit when the client is closed.

```json
"clangd.arguments": [
    "-compile-commands-dir=build"
],
```
