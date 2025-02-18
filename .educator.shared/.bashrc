#!/bin/bash

# shellcheck source=/dev/null
# shellcheck disable=SC1007
# shellcheck disable=SC2097
# shellcheck disable=SC2098
# shellcheck disable=SC2317

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

source ~/.bashrc
source "$script_dir/shshared"

cd "$(git rev-parse --show-toplevel 2>/dev/null)" || exit 1

_rel_path() {
    local prompt
    local root

    root="$(git rev-parse --show-toplevel 2>/dev/null)"

    # shellcheck disable=SC2181
    if [[ $? == 0 ]]; then
        prompt="${PWD#"$root"}"
        prompt="${prompt#/}"
    else
        prompt="${PWD/"$HOME"/\~}"
    fi

    echo -n "$prompt"
}

_set_bash_prompt() {
    local prompt
    prompt=$(_rel_path)

    if ((${#prompt} > 13)); then
        prompt+="\n"
    elif ((${#prompt} > 0)); then
        prompt+=" "
    fi

    prompt="$(tput setaf 12)${prompt# }$(tput sgr0)$ "
    PS1=$prompt
}

pwd
ls --color

IFS=, read -r datepart timepart < <(date +"%y%m%d,%H%M%S")
date_directory="date/d$datepart"

source .state

export -f _rel_path
export -f _set_bash_prompt
export PROMPT_COMMAND=_set_bash_prompt
export SHELL="$script_dir/bash_noprofile_norc"

if [ ! -e "$date_directory" ]; then
    class="$(_ask 'Ange klass' '[A-Z]+2[3-9]' "$class")"
    lession_number="$(_ask 'Ange lektion' '[1-9][0-9]?' "$((lession_number + 1))")"
    echo -e "class='$class'\nlession_number='$lession_number'" >.state
    git fetch
    git stash
    if ! git checkout "$datepart" 2>/dev/null; then
        git checkout -b "$datepart"
        git push
    fi
    git stash pop
fi

mkdir -p "$date_directory/recordings"
mkdir -p "$class"

lession="lektion${lession_number}"

[ ! -e "$class/$lession" ] && ln -rs "$date_directory" "$class/$lession"

cd "$date_directory" || true

record_timing="recordings/${timepart}_timing.txt"
record="recordings/${timepart}.txt"

trap 'read -r size _ < <(wc -c "$record"); if ((size < 500)); then rm "$record" "$record_timing"; fi' EXIT

script -e -q "--t=$record_timing" -q "$record"

exit $?
