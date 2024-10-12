# Install

```bash
wget -O miniconda3.sh "https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh"
bash miniconda3.sh
# conda init # This step is included in the previous .sh
conda create -n python312 "python=3.12"
# ~/miniconda3/envs/python312/bin/python
```

# [Issue]

- Bundled `curl` causes error setting certificate verify locations.
    - `/usr/bin/curl` is masked.
    - Fail to pick up `apt` installed `ca-certificates`.
    - [Workaround] `export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`
        - <https://stackoverflow.com/questions/3160909/how-do-i-deal-with-certificates-using-curl-while-trying-to-access-an-https-url>
    - [Workaround] `conda install ca-certificates`
    - TODO: It is possibly fixed.
- TODO: If `.local` contains a package installed py `pip`, conda doesn't know it, but some how that is used for Python.


# Config

- <https://conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html>
- <https://conda.io/docs/user-guide/tasks/manage-channels.html>
- `conda config ...` can be used to modify the config.
    - Config is stored in `~/.condarc` by default.
        - Can be edited manually.
    - `--env` - Write config to the current environment.
- `--set key value`
- `--add key value` - Put `value` at the top of the list.
- `--append key value` - Put `value` at the bottom of the list.
- `--describe [key]`
- `--show [key]`

## Keys

- `channel_alias = https://conda.anaconda.org`
    - `foo` is equivalent to `https://conda.anaconda.org/foo`.
- `default_channels`
    - If set, expands `defaults` channel to those.
    - [Default] `defaults` expands to all channels in `https://repo.anaconda.com/pkgs`.
    - `pkgs/main`, `pkgs/r` in v4.12
- `channels`
    - A higher priority channel (top of the list) over any version is preferred to a lower priority channel.
    - [Default] `defaults` channel is added.

# Solve Performance & Channel Mixing

- <https://github.com/conda/conda/issues/7690>
- <https://www.anaconda.com/understanding-and-improving-condas-performance/>
- `conda config --set channel_priority strict`
     - Speed up by eliminating mixed solutions.
    - <https://conda-forge.org/docs/user/tipsandtricks.html>
    - TODO: `strict` will be activated by default in v5.0.
    - `conda install -c conda-forge foo` would cause all dependencies of `foo` to be replaced by the version from `conda-forge`.
    - Append `conda-forge` to `channels` & do not use `conda install -c conda-forge`.


# Frequently Used

```bash
conda config --set channel_priority strict
conda config --add channels conda-forge

# Self update
# Do not install stuff from `conda-forge` into base
conda update -n base -c defaults conda
```


# Packages

- `conda search / install pattern`
    - `pattern` is `name=version=build`
        - E.g. `*foo`, `foo>=1.2` (quote if shell complains).
    - `--channel c` - Specify a channel `c`.
        - `--override-channels` - Do not include the channels in `.condarc`.
- `conda search`
    - `--info` - Show details of a package.
    - ` conda search 'pytorch>1.0=py2.7*' --info`
- `conda install`
    - TODO: Many options to skip slow dependencies check.
    - `--revision revision` - Revert to the specified `revision`
    - `--freeze-installed` - Do not update existing packages.
    - `--file requirements.txt` - Instal from `requirements.txt`
- `conda update --all` - Update all packages, useful when some packages pin each other.
- `conda list pattern`
    - `-n environment`
    - `-r` - List the revisions.
- `conda uninstall`
    - `--force`
- `conda clean -a` - Remove index cache, unused cache packages.

# Environment Variable

- `$CONDA_PREFIX`
    - [Example] `~/miniconda3/envs/vscode_snippet`
    - [Example] `~/miniconda3` if `base`
- `$CONDA_EXE`
    - [Example] `~/miniconda3/bin/conda`
- `$CONDA_PYTHON_EXE`
    - [Example] `~/miniconda3/bin/python`
- `$CONDA_DEFAULT_ENV`
    - [Example] `vscode_snippet`
- `$CONDA_PREFIX_1`
    - [Example] `~/miniconda3`
    - Only set if current environment is not `base`


# Virtual Environment

- <https://conda.io/docs/user-guide/tasks/manage-environments.html>
- The base environment contains the conda installation alongside a Python installation.
    - Since conda require Python to run.
- `conda create --name foo "python=3.12"`
    - Need to specify `python` otherwise it is empty.
- `conda env list`
    - Read from ` ~/.conda/environments.txt`
- `source activate foo` / `conda activate foo`
    - [Issue] `tmux` sometimes doesn't work with environment. The prompt shows correctly but `which python` is wrong.
        - <https://github.com/conda/conda/issues/6826>
        - <https://stackoverflow.com/questions/57660263/tmux-recognised-conda-env-but-still-use-the-default-python>
        - [Workaround] Deactivate & activate again.
- `source deactivate` / `conda deactivate`
- `conda create --name foo --clone base`
- `conda remove --name foo --all`
- `base` is the default environment.
    - Content is under e.g. `.`.
- `foo` environment is under `./envs/foo`.
- `conda env create -f environment.yml`
    - Create an environment from file.
    - [Tip] Useful if it depends on `pip` packages.
- `conda env export > environment.yml`

```yaml
name: foo
# Can be omitted
channels:
  - javascript
dependencies:
  - python=3.6
  - numpy=1.9.*
  - nodejs=0.10.*
  - flask
  - pip:
    # Things to be installed via pip.
    - Flask-Testing
```


# Docker

- <https://pythonspeed.com/articles/activate-conda-dockerfile/>
- `conda init` doesn't bring `conda` & `python` in scope in Docker while building.
    - `SHELL ["/bin/bash", "--login", "-c"]` doesn't work.
- [Issue] Cannot activate an environment in Docker while building.
    - <https://github.com/ContinuumIO/docker-images/issues/89>
    - Workaround: Use `conda run`
- `conda run -n my_env ...` - Run a command in conda environment.
- Smaller image
    - `conda install -y --freeze-installed ... && conda clean -afy`
    - <https://jcristharif.com/conda-docker-tips.html>
