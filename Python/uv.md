# Install

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv self update
# shell auto complete
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc

uv python install 3.13
# see all available & installed python versions with symbol links
uv python list
# upgrade all installed python to latest patch version.
# e.g. 3.12.0 to 3.12.1
uv python upgrade

cd hello-world
uv init

# Use a specific python version for the project
# This modify `.python-version`
uv python pin 3.13

uv add "httpx>=0.20" # --dev
uv remove httpx # --dev
# update a single package & `uv.lock` w.r.t. version constraints in `pyproject.toml`
uv lock --upgrade-package httpx
# update all packages & `uv.lock` w.r.t. version constraints in `pyproject.tom
uv lock --upgrade

# install according to `uv.lock`
un sync
# view dependency tree
uv tree
# only show top level
uv tree -d1

# run under virtual environment
uv run python
```

- <https://docs.astral.sh/uv/getting-started/installation/>


# Uninstall *uv*

```bash
# Clean up stored data
uv cache clean
rm -r "$(uv python dir)"
rm -r "$(uv tool dir)"
# remove binaries
rm ~/.local/bin/uv ~/.local/bin/uvx
```

- <https://docs.astral.sh/uv/getting-started/installation/#uninstallation>

# *uv*

- Project structure
    - `.venv`
    - `.python-version`
        - Contain a string e.g. `3.13`
    - `uv.lock`
    - `pyproject.toml`

# Manage Dependencies

- Dependencies are specified in `pyproject.toml`
    - Under `project.dependencies` sections
    - Under `[dependency-groups]` sections
        - For development dependencies, e.g. `dev` group
    - [Convention] Just use `dev` group for notes
        - [Example] `uv add --dev pytest`
    - [Issue] No command to upgrade version in `pyproject.toml`
- [Default] *uv* includes `dev` dependency group in the environments
    - I.e. `uv sync` works with `dev` group
- [Convention] No need to specify version in `uv add numpy`
    - It will automatically add an entry e.g. `numpy>=2.3`
