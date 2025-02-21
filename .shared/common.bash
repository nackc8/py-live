msg() {
	echo # newline

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

	echo "$message" | tr $'\n' ' ' | sed -E 's/ +/ /g' | fold -s -w "$width"
	echo # newline
}

msg_stderr() {
	msg "$@" >&2
}

# usage: ask  [--validate regexp] [--default answer] "prompt" ["answer_group" ...]
ask() {
	local answer_group
	local args=("$@")
	local default
	local validate

	while ((${#args[@]} > 0)); do
		local current="${args[0]}"
		args=("${args[@]:1}")

		case "$current" in
		--validate)
			if (($# > 0)); then
				validate="${args[0]}"
				args=("${args[@]:1}")
			else
				msg_stderr "Missing argument for --validate"
				return 1
			fi
			;;
		--default)
			if (($# > 0)); then
				default="${args[0]}"
				args=("${args[@]:1}")
			else
				msg_stderr "Missing argument for --default"
				return 1
			fi
			;;
		--)
			break
			;;
		*)
			args=("$current" "${args[@]}")
			break
			;;
		esac
	done

	local prompt="${args[0]}"
	args=("${args[@]:1}")

	if ((${#args[@]} > 0)) && [[ -n "${validate-}" ]]; then
		msg_stderr "Cannot use both answer_group and --validate"
		return 1
	fi

	local wrapped_prompt=$(msg "$prompt")

	local answer

	while read -r -p "$wrapped_prompt " answer; do
		for answer_group in "${args[@]}"; do
			if [[ $answer =~ ^[$answer_group]$ ]]; then
				echo "${answer_group:0:1}"
				return
			fi
		done

		if [[ $answer =~ ^[[:space:]]*$ && "$default" != "" ]]; then
			echo "$default"
			return
		fi

		if [[ ${validate:-empty} != empty ]]; then
			if [[ $answer =~ $validate ]]; then
				echo "$answer"
				return
			fi
		fi
	done
}

# shellcheck disable=SC2120
get_git_branch() (
	local git_dir=${1:-""}
	if [[ $git_dir != "" ]]; then
		cd "$git_dir" || return 1
	fi
	git rev-parse --abbrev-ref HEAD
)

# shellcheck disable=SC2120,SC2086
get_git_remote() (
	if [[ $1 != "" ]]; then
		cd "$1" || return 1
	fi
	local branch="$(get_git_branch $1)"
	git config --get "branch.$branch.remote"
)

# shellcheck disable=SC2120,SC2086
get_git_url() (
	local git_dir=${1:-""}
	if [[ $git_dir != "" ]]; then
		cd "$git_dir" || return 1
	fi
	local remote=$(get_git_remote "$git_dir")
	git config --get "remote.$remote.url"
)

sanitize() {
	echo "$1" | sed -E 's#[^a-zA-Z0-9]#_#g'
}

exit_if_script_is_already_running() {
	local msg=$1
	local exit_code=$2

	local url="$(get_git_url)"
	local script_id="$(sanitize "$url")"
	local id_file=${XDG_RUNTIME_DIR:-/tmp}/"$script_id"

	if [ -f "$id_file" ]; then
		if [ "$msg" != "" ]; then
			msg_stderr "$msg"
		fi

		if [ "$exit_code" != "" ]; then
			exit "$exit_code"
		else
			exit
		fi
	fi

	# shellcheck disable=SC2064
	trap "rm -f $id_file" EXIT
	touch "$id_file"
}
