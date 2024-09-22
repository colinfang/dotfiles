# Settings

- User settings are stored in `~/.config/Code/User/` or `%AppData%\Code\User\`
    - `settings.json`
    - `keybindings.json`
- Support `**` (Recursive expansion).
- `files.exclude` sets what appears in the explorer.
    - Files are greyed out based on `.gitignore`
        - Need to be a git repository (`git init`) and have git installed
    - `explorer.excludeGitIgnore` - Ignore files from `.gitignore`
- Search in workspace
    - `search.exclude` inherits `files.exclude`.
    - `search.useIgnoreFiles` - Exclude files from search results based on `.gitignore`.
        - Affect filename search as well.
    - [Issue] Cannot ignore unnecessary stuff from `.ipynb`
-  "Default Dark+" is a more colorful version of "Visual Studio Dark".

# Tips

- Double click on tab to maximize panel.
    - Can config whether to maximize or semi-maximize.
- A cheap way to restart some internal processes
    - "Command Palette" -> "Reload Window"
- Debug frontend stuff
    - "Command Palette" -> "Open webview developer tool"
    - [Tip] Chrome console displays useful errors from extension.
- Click language status bar (curly brackets before language mode) in the status bar to see some extension status.

# Keyboard Shortcut

- Windows & Linux may have different shortcuts.
- Set keyboard shortcut - Left bottom -> Keyboard shortcut
    - Can toggle JSON view `keybindings.json`
- Navigate
    - <kbd>Alt+Left/Right</kbd> - Go back / forward
    - Mouse buttons also work
- Cursor
    - <kbd>Ctrl+Alt+Up/Down</kbd> - Add cursor above / below
    - <kbd>Ctrl+D</kbd> - Add next occurrences to selection
        - <kbd>Ctrl+K</kbd> - Ignore the current occurrence.
- Search
    - <kbd>Ctrl+P</kbd> - Search files by name
        - Append `/` e.g. `lint/` to target folders.
            - Otherwise matching folders are ranked lower than filename fuzzy match.
    - <kbd>Ctrl+Shift+P</kbd> - Search commands in "Command Palette"
- Others
    - <kbd>Ctrl+/</kbd> - Comment / un-comment code
    - <kbd>Ctrl+.</kbd> - Quick fix
    - <kbd>Ctrl+Click</kbd>
        - In C++, jump between declaration & implementation of a function.


# Variables

- <https://code.visualstudio.com/docs/editor/variables-reference>
- Brackets cannot be omitted.
- Works in all sorts of configuration files.
- Predefined variables
    - `${workspaceFolder}` - The path of the folder opened.
        - `${workspaceFolderBasename}`
    - `${file}` - Absolute path to the current file.
            - `${fileBasename}$` - Filename without directory.
            - `${fileBasenameNoExtension}`
    - `${fileDirname}` - Absolute path to the current file's directory.
    - Some might not work in `settings.json`
- Environment variables
    - [Example] `${env:PATH}`
