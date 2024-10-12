# Install

```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
# Self update
micromamba self-update
micromamba create -n python312 "python=3.12"
# ~/micromamba/envs/python312/bin/python
```


# Mamba

- A conda replacement
    - Fully compatible with conda packages & supports most of conda commands.
    - `mamba` - A Python based CLI as a drop-in replacement for `conda`
    - `micromamba` - A C++ based CLI, self-contained in a single-file executable.
- Like conda, the base environment contains the mamba installation alongside a Python installation.
    - Since mamba require Python to run.
    - [Remark] `micromamba` create empty base environment.
- A prefix is a fully self-contained & portable installation.
    - Target prefix
        - Just an environment
    - `$MAMBA_ROOT_PREFIX`
        - [Example] `~/micromamba`
        - `./pkgs/`
            - Packages cache, shared by all environments
        - `./envs/`
            - Can contain environments too
- The activation of an environment makes all its contents available to the shell.
    - It mainly adds target prefix subdirectories to `$PATH`
