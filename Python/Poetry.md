
```bash
micromamba create -n python313 "python=3.13"
micromamba activate python313
curl -sSL https://install.python-poetry.org | python -
# Install into ~/.local/bin
# export PATH=$PATH:$HOME/.local/bin

# Uninstall
# curl -sSL https://install.python-poetry.org | python3 - --uninstall

poetry --version
poetry self update

# By default environments are install in
# cache-dir = "/home/colin/.cache/pypoetry"
# This would create `.venv` under the repository.
poetry config virtualenvs.in-project true

###################################
# In a repository
# Make sure we are not in a conda / mamba environment
micromamba deactivate
poetry init
# See which python is used
poetry env info
ls -alh .venv/bin/python
poetry env use ~/micromamba/envs/python313/bin/python
# Install according to `poetry.lock`
poetry install
# Update packages and `poetry.lock`
poetry update
# See installed packages
poetry show
# Only show those are included in pyproject.toml
poetry show --top-level
source .venv/bin/activate
deactivate
```


- Dependencies are specified in `pyproject.toml`
    - 2 modes
        - [Default] Package mode
            - Intend to package the project into a wheel
            - `name` & `version` are mandatory.
        - Non-package mode
            - `package-mode = false`
- Can modify virtual environment prompt name e.g. `non-package-mode-py3.13` in `.venv/bin/activate` script.
- [Remark] Do not activate Conda / Mamba environment before doing poetry operation, otherwise
    - `poetry env info` shows Conda / Mamba environnement
    - `poetry install` install `pyproject.toml` dependencies into Conda / Mamba environment.
- [Issue] It cannot manage Python version. So Conda / Mamba is still needed.
- [Issue] Don't know how to set auto complete for antigen zsh
- Configuration
    - <https://python-poetry.org/docs/configuration/>
    - `~/.config/pypoetry/config.toml`
    - `poetry config --list`
- Can only have 1 environnement per folder.
- Dependency specification
    - <https://python-poetry.org/docs/dependency-specification/>
    - [Convention] Use `*`, `>= 1.2`
    - [Remark] `1.2` would not update to `1.2.3`
    - [Remark] Python version is dependencies as well
        - Better to fix Python version e.g. `python = "3.9.*"`
        - Because *poetry* looks for a package version that works for all possible variants of Python rather than the current version.
- [Tip] Use `poetry add "pandas-stubs"` to install, as it would handle the package name capital & fill in the versions.
    - Sometimes quotes are needed
        - [Example] `poetry add "numpyro[cpu]"`
- `poetry update [--dry-run]`
    - Respect the version constraints in `pyproject.toml`
