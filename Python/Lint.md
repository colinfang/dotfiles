# Lint in Python

- [Convention] `_some_unused` to bypass unused-variable warning.
- [My config](</pyproject.toml>)
    - *PyLint* - `[tool.pylint]`
    - *Pyright* - `[tool.pyright]`
    - *MyPy* - `[tool.mypy]`
- Placeholder function body `...` ellipsis
    - *Pyright* & *MyPy* - Ignore return type check


# Inline Configuration Via Comments

- Ignore a file
    - *PyLint* - `# pylint: skip-file` at the top of a file.
    - *MyPy* & *Pyright* - `# type: ignore` at the top of a file.
- Per file configuration
    - *Pyright*
        - [Example] `# pyright: reportUnknownMemberType=none`
        - [Issue] Only work for the current cell now if it is on a notebook
    - *MyPy*
        - [Example] `# mypy: disallow-any-generics=False`
        - [Example] `# mypy: allow-any-generics`
            - `=True` can be omitted
- Per line configuration
    - *PyLint* - `... # pylint: disable=not-an-iterable`
    - *MyPy* & *Pyright* - `... # type: ignore`
    - *MyPy* - `... # type: ignore[code1, code2]`
        - [Issue] This would make *Pyright* to ignore the line
            - <https://github.com/python/mypy/issues/12358>
            - [Workaround] Do not use it
    - *Pyright*
        - `... # pyright: ignore`
        - `... # pyright: ignore[code1, code2]`
    - For both *PyLint* & *MyPy*
        - `... # type: ignore[override] # pylint: disable=arguments-differ`
- Next line
    - *PyLint* - `# pylint: disable-next=not-an-iterable`
- Block level configuration
    - *PyLint*
        ```python
        if True:
            # pylint: enable=no-member
        ```
- Detect unnecessary ignore
    - *Pyright* - `reportUnnecessaryTypeIgnoreComment`
    - *MyPy* - `warn_unused_configs`
    - *PyLint* - `useless-suppression`
- References
    - *Pyright*
        - <https://github.com/microsoft/pyright/blob/main/docs/comments.md>
    - *MyPy*
        - <https://mypy.readthedocs.io/en/stable/inline_config.html>


# PyLint

- All checks with code & name
    - <https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html>
    - <https://pylint.pycqa.org/en/latest/user_guide/messages/messages_overview.html>
- <https://pylint.pycqa.org/en/latest/user_guide/configuration/all-options.html>
    - Rich customization of each checker that performs lint.
- [Issue] Doesn't work well with `dataclasses` fields.
    - <https://github.com/PyCQA/pylint/issues/2605>
    - TODO: It should have be fixed
- `pylint --generate-toml-config`
    - Generate a demo `pyproject.toml`


# MyPy

- <https://mypy.readthedocs.io/en/latest/command_line.html>
- Config
    - <https://mypy.readthedocs.io/en/stable/config_file.html>
    - Check help on `--strict` to see some useful options.
        - <http://manpages.ubuntu.com/manpages/disco/man1/mypy.1.html>
    - [Default] Python extension passes the following unless `python.linting.mypyArgs` is set
        - `--follow-imports=silent --ignore-missing-imports --show-column-numbers --no-pretty`
- Options may be inverted by adding `no-` to their name or by swapping their prefix from `disallow` to `allow`
- `--show-error-codes`
    - [Tip] Useful to know what to silence.
    - <https://mypy.readthedocs.io/en/latest/error_codes.html>
- Functions without annotations are ignored by default.
    - <https://mypy.readthedocs.io/en/latest/common_issues.html#no-errors-reported-for-obviously-wrong-code>
    - Even when the body contains type annotation
    - `--check-untyped-defs` to force check.
    - `__init__` is special cased to opt in type checking
- `--show-column-numbers`
    - [Remark] Help Python extension to align intellisense to the correct place.
        - <https://github.com/microsoft/vscode-python/issues/18983>


# Pyright

- References
    - <https://github.com/microsoft/pyright>
    - <https://github.com/microsoft/pyright/blob/main/docs/type-concepts.md>
- Config
    - <https://github.com/microsoft/pyright/blob/main/docs/configuration.md>
    - <https://github.com/microsoft/pyright/blob/main/docs/getting-started.md>
- Severity level
    - `none`
        - Grey out
        - Not appear in "Problems"
    - `information`
        - Blue underline
    - `warning`
        - Yellow underline
    - `error`
        - Red underline
    - `false` & `true` are also valid, which toggle the check using the default severity
- Different type rules from MyPy
    - Especially in {:Literal Type.md}
- [Convention] Better than MyPy
- [Issue] `reportMissingSuperCall` is useless because it shouts at almost every class.
    - <https://github.com/microsoft/pyright/commit/846cee35dbe7a040f25e5fb373e3df560dcc79e5>
- "Type of xxx is partially unknown"
    - Triggered by checks e.g. `reportUnknownMemberType`, `reportUnknownVariableType`, `reportUnknownArgumentType`
    - It is because the type annotation is a generic e.g. `np.array` rather than a full type `np.array[Any, Any]`
    - [Convention] Turn off those for now.
- TODO:
    - <https://github.com/microsoft/pyright/blob/main/docs/type-inference.md>
