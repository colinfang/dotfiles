- `apt install zsh`
- `~/.zshrc` is an equivalent of `.bashrc`.
- `chsh` - Change login shell for the current user.
    - [Remark] Do not `sudo` otherwise it changes for `root`
    - `/bin/zsh`
    - Need to set environment variables in `.zshrc` as `.bashrc` is no longer executed.


# Package Manager `antigen`

- <https://github.com/zsh-users/antigen/wiki/Commands>
- <https://github.com/zsh-users/antigen>
- `curl -L git.io/antigen > ~/antigen.zsh`
- Do it regularly to update.
- `antigen list` - Show loaded plugins.
- `antigen update [bundle_name]`
    - If `bundle_name` is not specified, update all the loaded plugins.

# Plugins

- `zsh-autosuggestions` - <kbd>Ctrl+f</kbd> to auto complete.
- If the suggestion colors are not grey
    - <https://github.com/zsh-users/zsh-autosuggestions/issues/12>
    - Perhaps the terminal doesn't support 256 color
        - E.g. `tmux` might set it to be `screen`
    - [Workaround] Add `export TERM="xterm-256color"` to `.zshrc`
    - Alternatively, set `AUTOSUGGESTION_HIGHLIGHT_COLOR='fg=cyan'`
        - [Default] `fg=8`
    ```bash
    echo $TERM
    # xterm-256color
    ```
- [Issue] `zsh` paste is slow.
    - <https://github.com/robbyrussell/oh-my-zsh/issues/5569>
    - <https://apple.stackexchange.com/questions/312795/zsh-paste-from-the-clipboard-a-command-takes-a-few-second-to-be-write-in-the-ter>
    - Workaround affects `antigen update` as it is no longer `git pull` free.
    - `vim $ZSH/lib/misc.zsh`
- Avoid checking git status
    - `git config --global oh-my-zsh.hide-status 1`
    - TODO: Doesn't seem to work any more?