msg() {
    local message
    local width
    local min_width=20
    local max_width=110

    width=$(($(tput cols)))
    width=$((width < min_width ? min_width : width))
    width=$((width > max_width ? max_width : width))

    if [ $# -gt 0 ]; then
        message="$*"
    else
        message=$(cat)
    fi

    echo "$message" | tr $'\n' ' ' | sed -E 's/ +/ /g' | fold -s -w $width
}

ask() {
    local prompt="$1"
    shift
    local wrapped_prompt=$(msg "$prompt")

    local answer

    while read -r -p "$wrapped_prompt " answer; do
        for answer_group in "$@"; do
            if [[ $answer =~ [$answer_group] ]]; then
                echo "${answer_group:0:1}"
                return
            fi
        done
    done
}
