# clangd

- <https://clangd.llvm.org/>
    - <https://clangd.llvm.org/config>
- clang-tidy & clang-format are bundled.
    - Contain include cleaner
        - Similar to iwyu
        - <https://clangd.llvm.org/config#unusedincludes>
- `compile_commands.json` is needed for compiler options
    - [Default] Search in workspace root folder if `-compile-commands-dir` is unspecified
    - [Tip] Check clangd output to see how `compile_commands.json` is used
    - Commands are inferred from other entry if the current file is missing from `compile_commands.json`.
        - Hence filename can be arbitrary
    - <https://clangd.llvm.org/design/compile-commands>
- [Issue] No concise syntax to ignore a line
    - {:compile.md} - Modify warning levels
- [My config](</.clangd>)
    - Add `-std=c++20` because cmake omits the standard if it is the compiler default
    - <https://discourse.cmake.org/t/cmake-does-not-set-the-compiler-option-std-to-gnu17-or-c-17-although-i-set-the-target-compile-features-to-cxx-std-17/3299/>
- {:compile_commands.json}
- [Fixed] Allow type deduction on hover over type alias for some type traits
    - <https://github.com/clangd/clangd/issues/1134>
    - [Workaround] `ShowAKA: Yes`
        - <https://clangd.llvm.org/config#showaka>


# clang-tidy

- All checks
    - <https://clang.llvm.org/extra/clang-tidy/checks/list.html>
    - <https://github.com/llvm-mirror/clang-tools-extra/tree/master/docs/clang-tidy/checks>
- `-checks=...`
    - [Example] `-checks=-*,clang-analyzer-*,-clang-analyzer-cplusplus*`
    - Glob pattern is used.
    - `-` means disable.
- <https://clang.llvm.org/extra/clang-tidy/>
- CLion default configs
    - <https://confluence.jetbrains.com/display/CLION/Clang-Tidy+in+CLion%3A+default+configuration>
- [My config](</.clang-tidy>)
    - Require `Checks: '*'`
    - YAML


# clang-format

- Google style
    - Inherit from LLVM style
    - <https://github.com/llvm/llvm-project/blob/release/14.x/clang/lib/Format/Format.cpp#L1280>
- Options
    - <https://clang.llvm.org/docs/ClangFormatStyleOptions.html>
- [My config](</.clang-format>)
    - YAML
