source ~/antigen.zsh

antigen use oh-my-zsh

antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-autosuggestions
antigen bundle zsh-users/zsh-completions

antigen theme robbyrussell
antigen apply


[ -z "$SSH_AUTH_SOCK" ] && eval "$(ssh-agent -s)"

export PATH=$PATH:$HOME/.local/bin
export PATH=$PATH:$HOME/julia_binary/julia-1.9.0/bin/
