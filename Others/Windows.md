# %% Environment Variable

- <https://pureinfotech.com/list-environment-variables-windows-10/>
- Case insensitive
- `%ProgramData%` - `C:\ProgramData`
- `%ProgramFiles%` - `C:\Program Files`
- `%ProgramFiles(x86)%` - `	C:\Program Files (x86)`
- `%UserProfile%` - `C:\Users\me`
- `%AppData%` - `C:\Users\me\AppData\Roaming`
- `%LocalAppData%` - `C:\Users\me\AppData\Local`
- `%SystemRoot%` - `C:\Windows`

# PowerShell Frequently Used

- `Get-Command ssh` - Like `which`
- `dir "$env:ProgramFiles\Common Files"`
    - Equivalent to `ls`
- `$env:ProgramData` - Show environment variable
    - `ls "$env:ProgramFiles\Common Files"`
