# `wsl`

- PowerShell
- Install
    - <https://docs.microsoft.com/en-us/windows/wsl/install>
    - `wsl --install`
        - Install WSL 2 & Ubuntu
- `wsl --set-default Ubuntu-22.04`
- `wsl -d Ubuntu-22.04` - Run the specific distribution
- `wsl --list --online`
    - Show available Linux distributions
- `wsl --status`
    - If "Updates For Other Microsoft Products When Updating Windows" is enabled, WSL automatic updates are on.
        - [Ref](<../Others/Windows.md#my-config>)
- `wsl --update`
    - Update kernel manually.

# Call WSL Command From Windows

- [Example] `wsl ~/miniconda3/envs/scratch/bin/python`
    - The path after `wsl` is w.r.t. Linux.
- In windows shell, `wsl cmd` would not run `.bashrc`, so it is likely "command not found"
- `wsl; ls; ls`
    - All subsequent commands are from Linux.
    - In `Cmd.exe` only

# Call Windows Command From WSL

- Just append `.exe`
    - [Example] `dotnet.exe`

# Overview

- Access Linux from Windows
    - Explorer
        - [Convention] `\\wsl.localhost\Ubuntu-22.04`
            - Resolve to "This PC" -> "Linux"
        - `\\wsl$\Ubuntu-22.04`
            - Resolve to "This PC" -> "Network"
    - Chrome
        - `file://wsl$/Ubuntu-20.04/`
        - `file://wsl.localhost/Ubuntu-20.04/`
- [Issue] IPython paste seem to add auto indentation. `%paste` doesn't work.
    - [Workaround] Use `%cpaste`
- `wslpath` - Switch between WSL & Windows path.
    - `-a` - Force absolute path.
    - `"$(wslpath -a "%1")"` in place of `%1`
    ```bash
    wslpath "C:\Users\me"
    # /mnt/c/Users/me
    wslpath $'C:\Users\me'
    # C:
    wslpath C:\Users\me
    # wslpath: C:Usersme
    ```

- Set "Language for non-Unicode program"
    - {:Windows.md} - System Font
- Port forwarding
    - A service listens to 127.0.0.1:port works for a request on the host with the same ip & port.
    - [Issue] Not working after Windows fast startup
        - E.g. `syncthing` web UI doesn't work
        - E.g. VS Code live previewer doesn't work
        - <https://github.com/microsoft/WSL/issues/4636>
        - <https://github.com/microsoft/WSL/issues/5298>
        - <https://superuser.com/questions/1696797/my-script-to-set-up-port-forwarding-to-wsl-2-ssh-fails>
        - [Workaround] `wsl --shutdown`
- [Issue] High memory usage
    - <https://github.com/microsoft/WSL/issues/4166>
        - `free -h` to check.
    - [Workaround] Set memory & swap in `.wslconfig`
- `/bin` is a symlink to `/usr/bin`
- [Issue] "Failed to retrieve available kernel versions." in Ubuntu 22.04 after `apt` install new packages.
    - Caused by `needrestart -k`
    - <https://askubuntu.com/questions/1404129/ubuntu-22-04-lts-on-wsl-failed-to-retrieve-available-kernel-versions-failed>
    - [Workaround] `apt remove needrestart`


# Config

- <https://docs.microsoft.com/en-us/windows/wsl/wsl-config>
- `wsl.conf`
    - Store in `/etc/wsl.conf` in the distribution.
    - `boot` is available only on Windows 11
        - TODO: Doesn't seem to work?
- `.wslconfig`
    - Store in `%UserProfile%\.wslconfig` in Windows
    - Config settings globally across all distributions in WSL2
    - [My config](<.wslconfig>)
    - WSL Settings app is the GUI for it.
