# Python

- [Settings](</Project Template/PythonRepo/.vscode/settings.json>)
    - <https://code.visualstudio.com/docs/python/settings-reference>
- Provide highlighting for pip requirement file
- Notebook in WSL
    - `jupyter.alwaysTrustNotebooks` only works in remote settings.
- Double click on inlay type hint to auto type annotate.

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

```json
// Expose Pylance's bundled stubs to MyPy
"mypy-type-checker.args": [
    "--mypy-path",
    "~/.vscode/extensions/ms-python.vscode-pylance-2025.10.4/dist/bundled/stubs"
],
```


# Black Formatter

- *Black* is bundled
- [Tip] Useful for Jupyter
- [Settings](</Project Template/PythonRepo/.vscode/settings.json>)


# isort

- *isort* is bundled
- "Command Palette" -> "Organize import"
