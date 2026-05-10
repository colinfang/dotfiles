# Pytest

```bash
pytest -v tests/test_foo.py::test_bar
```

- `PYTHONPATH=':' pytest ...` is equivalent to `python -m pytest ...`
    - I.e. `pytest` doesn't put current working directory to `PYTHONPATH`, but `python -m pytest` does.
- `--ignore=foo`: Ignore some file.
- `-v`: Verbose, show name for each test.
- `-x`: Exit on first error.


# PDB

- `-s` is required for pdb otherwise "IOError: reading from stdin while output is captured".
- `--pdb` - Start pdb on error.
- `--pdbcls=IPython.terminal.debugger:Pdb`: Use ipdb.
    - <https://stackoverflow.com/questions/16022915/how-to-execute-ipdb-set-trace-at-will-while-running-pytest-tests>


# Output & Logging


- [Default] Any output sent to STDOUT & STDERR & log is captured. If a test fails its captured output will be shown.
    - `--show-capture=no`: Do not show captured output on test failure.
    - `--capture=no`: Do not capture output (i.e. always show)
        - `-s`: Shortcut
    - <https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html#captures>
- `logging.basicConfig` is not necessary.
- `--log-level=debug`: Set logging level
    - Case-insensitive
