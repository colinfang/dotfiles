# Python

- [Settings](</Project Template/PythonRepo/.vscode/settings.json>)
    - <https://code.visualstudio.com/docs/python/settings-reference>
- Provide highlighting for pip requirement file
- Notebook in WSL
    - `jupyter.alwaysTrustNotebooks` only works in remote settings.
- Double click on inlay type hint to auto type annotate.
- Interpreter & venv path are stored in extension's internal database.
    - Other extensions (e.g. Pylint) might use this interpreter.
    - It is possible venv is set up correctly, but interpreter is wrong.
        - "Command Palette" ▷ "select interpreter" to fix


# Pylint

- *Pylint* is bundled
    - <https://github.com/microsoft/vscode-pylint/blob/main/requirements.txt>


# Pylance

- *Pyright* is bundled
- *Pyright* config file overrides VS Code settings
    - Check "Python Language Server" output for details
- [Issue] File level diagnostic config only applies to the current cell instead of all cells below for Jupyter notebook
    - <https://github.com/microsoft/pylance-release/issues/4483>


# MyPy

- [Issue] Cannot specify stubs
    - `--mypy-path` is newly added in v1.20
    - Specify `mypy_path` in `[tool.mypy]` in `pyproject.toml` doesn't work
- [Remark] Disable for the moment
    - The most recent extension release was on 2025-03-05 with *MyPy* version v1.15
        - Now *MyPy* is v1.20
        - Might not be actively maintained


# Black Formatter

- *Black* is bundled
- [Tip] Useful for Jupyter
- [Settings](</Project Template/PythonRepo/.vscode/settings.json>)


# isort

- *isort* is bundled
- "Command Palette" ▷ "Organize import"
