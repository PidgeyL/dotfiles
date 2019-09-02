export PATH="$PATH:$(du "$HOME/.local/bin" | cut -f2 | tr '\n' ':' | sed 's/:*$//')"
# Auto-update .bashrc unless .bashlock is set
if [ ! -f ~/.bashlock ]; then
    (/usr/bin/git -C $HOME pull origin master >/dev/null 2>&1 &)
fi


iatest=$(expr index "$-" i)



# Enable bash programmable completion features in interactive shells
if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi



# Aliasses
if [ -f ~/.bash_aliasses ]; then
     . ~/.bash_aliasses
fi



# Encrypted .bashrc for api keys etc
if [ -f ~/.bash_private.gpg ]; then
   eval "$(gpg --decrypt ~/.bash_private.gpg 2>/dev/null)"
fi



# Location for exports such as proxy settings etc
if [ -f ~/.bash_exports ]; then
    . ~/.bash_exports
fi



# Colors
# Color for manpages in less makes manpages a little easier to read
export LESS_TERMCAP_mb=$'\E[01;31m'
export LESS_TERMCAP_md=$'\E[01;31m'
export LESS_TERMCAP_me=$'\E[0m'
export LESS_TERMCAP_se=$'\E[0m'
export LESS_TERMCAP_so=$'\E[01;44;33m'
export LESS_TERMCAP_ue=$'\E[0m'
export LESS_TERMCAP_us=$'\E[01;32m'
export CLICOLOR=1
export LS_COLORS='no=00:fi=00:di=01;33:ln=01;36:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arj=01;31:*.taz=01;31:*.lzh=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.gz=01;31:*.bz2=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.avi=01;35:*.fli=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.ogg=01;35:*.mp3=01;35:*.wav=01;35:*.xml=00;31:'



# Settings
# Expand the history size
export HISTFILESIZE=10000
export HISTSIZE=500
# Don't put duplicate lines in the history and do not add lines that start with a space
export HISTCONTROL=erasedups:ignoredups:ignorespace
# Causes bash to append to history instead of overwriting it so if you start a new terminal, you have old session history
shopt -s histappend
PROMPT_COMMAND='history -a'

# Set the default editor
export EDITOR=nano
export VISUAL=nano

# Check the window size after each command and, if necessary, update the values of LINES and COLUMNS
shopt -s checkwinsize
# Allow ctrl-S for history navigation (with ctrl-R)
[[ $- == *i* ]] && stty -ixon

# Ignore case on auto-completion
if [[ $iatest > 0 ]]; then bind "set completion-ignore-case on"; fi
# Show auto-completion list automatically, without double tab
if [[ $iatest > 0 ]]; then bind "set show-all-if-ambiguous On"; fi

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"
# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi
# Add tab completion for SSH hostnames based on ~/.ssh/config, ignoring wildcards
[ -e "$HOME/.ssh/config" ] && complete -o "default" -o "nospace" -W "$(grep "^Host" ~/.ssh/config | grep -v "[?*]" | cut -d " " -f2- | tr ' ' '\n')" scp sftp ssh


# Prompt
function __setprompt
{	
    local LAST_COMMAND=$? # Must come first!

    # Define colors
    local LIGHTGRAY="\033[0;37m"
    local WHITE="\033[1;37m"
    local BLACK="\033[0;30m"
    local DARKGRAY="\033[1;30m"
    local RED="\033[0;31m"
    local LIGHTRED="\033[1;31m"
    local GREEN="\033[0;32m"
    local LIGHTGREEN="\033[1;32m"
    local BROWN="\033[0;33m"
    local YELLOW="\033[1;33m"
    local BLUE="\033[0;34m"
    local LIGHTBLUE="\033[1;34m"
    local MAGENTA="\033[0;35m"
    local LIGHTMAGENTA="\033[1;35m"
    local CYAN="\033[0;36m"
    local LIGHTCYAN="\033[1;36m"
    local BOLD="\033[1m";
    local ITALIC="\033[3m";
    local UNDERLINE="\033[4m";
    local BLINK="\033[5m";
    local REVERSE="\033[7m";
    local STRIKETHROUGH="\033[9m";
    local NOCOLOR="\033[0m"

    local USER="${CYAN}"
    local ROOT="${MAGENTA}"
    local HOST="${LIGHTBLUE}"
    local SSH="${LIGHTGREEN}"
    local PATH="${LIGHTCYAN}"
    local ERROR="${LIGHTRED}"
    local STATUS="${YELLOW}"
    local MESSAGE="${LIGHTGRAY}"
    local GITCHANGE="${LIGHTRED}"
    local GITCOMMIT="${YELLOW}"
    local GITSYNC="${LIGHTGREEN}"

    # Show error exit code if there is one
    if [[ $LAST_COMMAND != 0 ]]; then
        PS1="\[${ERROR}\][EXIT \[${STATUS}\]${LAST_COMMAND}\[${ERROR}\]] \[${MESSAGE}\]("
        if [[ $LAST_COMMAND == 1 ]]; then
            PS1+="General error"
        elif [ $LAST_COMMAND == 2 ]; then
            PS1+="Missing keyword, command, or permission problem"
        elif [ $LAST_COMMAND == 126 ]; then
            PS1+="Permission problem or command is not an executable"
        elif [ $LAST_COMMAND == 127 ]; then
            PS1+="Command not found"
        elif [ $LAST_COMMAND == 128 ]; then
            PS1+="Invalid argument to exit"
        elif [ $LAST_COMMAND == 129 ]; then
            PS1+="Fatal error signal 1"
#        elif [ $LAST_COMMAND == 130 ]; then
#            PS1+="Script terminated by Control-C"
        elif [ $LAST_COMMAND == 131 ]; then
            PS1+="Fatal error signal 3"
        elif [ $LAST_COMMAND == 132 ]; then
            PS1+="Fatal error signal 4"
        elif [ $LAST_COMMAND == 133 ]; then
            PS1+="Fatal error signal 5"
        elif [ $LAST_COMMAND == 134 ]; then
            PS1+="Fatal error signal 6"
        elif [ $LAST_COMMAND == 135 ]; then
            PS1+="Fatal error signal 7"
        elif [ $LAST_COMMAND == 136 ]; then
            PS1+="Fatal error signal 8"
        elif [ $LAST_COMMAND == 137 ]; then
            PS1+="Fatal error signal 9"
        elif [ $LAST_COMMAND -gt 255 ]; then
            PS1+="Exit status out of range"
        else
            PS1+="Unknown error code"
        fi
        PS1+=")\[${NOCOLOR}\]\n"
    else
        PS1=""
    fi

    # Add user
    if [[ "${USER}" == "root" ]]; then
        PS1+="\[${ROOT}\]\u"
    else
        PS1+="\[${USER}\]\u"
    fi;
    PS1+="\[${NOCOLOR}\]@"

    # Host if SSH, else '-'
    if [[ "${SSH_TTY}" ]]; then
        PS1+="\[${UNDERLINE}\]"
        PS1+="\[${SSH}\]\h"
    else
        PS1+="\[${HOST}\]\h"
    fi;


    # Current directory
    PS1+="\[${NOCOLOR}\]:"
    PS1+="\[${PATH}\]\w"


    # Git 
    local BRANCH=$(/usr/bin/git rev-parse --abbrev-ref HEAD 2> /dev/null)
    if [[ $BRANCH ]]; then
        GITCOLOR="${GITSYNC}"
        # Check if there are local commits
        if [[ $(/usr/bin/git log --branches --not --remotes) ]]; then
            GITCOLOR="${GITCOMMIT}"
        fi
        # Check if there are uncomitted changes
        if [[ $(/usr/bin/git status | /bin/grep modified) ]]; then
            GITCOLOR="${GITCHANGE}"
        fi
        # Ignore home if it is in sync
        REPOLOCATION=$(/usr/bin/git rev-parse --show-toplevel)
        if [[ $GITCOLOR != "$GITSYNC" ]] || [[ "$REPOLOCATION" != "$HOME" ]]; then
            PS1+=" \[${GITCOLOR}\](${BRANCH})"
        fi
    fi

    # Set prompt
    PS1+="\[${NOCOLOR}\]\$ "
    local GITCOMMIT="${YELLOW}"




}
PROMPT_COMMAND='__setprompt'
