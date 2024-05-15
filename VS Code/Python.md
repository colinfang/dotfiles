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

# Black Formatter

- [Tip] Useful for Jupyter
- [Settings](</Project Template/PythonRepo/.vscode/settings.json>)
- *Black* package is bundled
