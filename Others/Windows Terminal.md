# Overview

- <https://docs.microsoft.com/en-us/windows/terminal/>


# Configs

- GUI settings display some interesting options.
    - Click on the profile on the left bar to see the details.
        - Reveal the command associated to particular `source`
- Cannot have `"source": "Windows.Terminal.Wsl"` for the non-default one.
- [Issue] - Cannot add startup command under `wsl`.
    - `wsl conda` error with "Cannot find conda"
- Copy paste
    - <https://docs.microsoft.com/en-us/windows/terminal/customize-settings/interaction#automatically-copy-selection-to-clipboard>
    - `copyOnSelect` - Selections are automatically copied to your clipboard
    - `copyFormatting` - Formatted data is also copied to your clipboard


# Others

- <kbd>Shift+Ctrl+w</kbd> - Close a panel
    - <kbd>Ctrl+d</kbd> would cause "[process exited with code 130]" if <kbd>Ctrl+c</kbd> too much.
    - Close panel would fix it.
- Cascadia Code font is bundled. If it is prompted missing, can install the font via GitHub which would introduce an additional copy.


# My Settings

- In UI, modify the default profile to be Ubuntu.

```json
// https://docs.microsoft.com/en-us/windows/terminal/customize-settings/key-bindings
// My Additional Keybindings
{
    "command": "togglePaneZoom",
    "keys": "ctrl+shift+x"
},
{
    "command": "scrollDownPage",
    "keys": "pgdn"
},
{
    "command": "scrollUpPage",
    "keys": "pgup"
},
{
    "command":
    {
        "action": "splitPane",
        "split": "auto",
        "splitMode": "duplicate"
    },
    "keys": "ctrl+shift+e"
},
```
