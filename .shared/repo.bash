__shared_repo_bash_script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
__shared_repo_bash_root="$(
	cd "$__shared_repo_bash_script_dir"
	git rev-parse --show-toplevel
)"

source "$__shared_repo_bash_script_dir/common.bash"

__shared_repo_bash_educator="$__shared_repo_bash_root/.profiles/educator"
__shared_repo_bash_student="$__shared_repo_bash_root/.profiles/student"
__shared_repo_bash_educator_present="$__shared_repo_bash_root/.profiles/educator_present"
__shared_repo_bash_educator_edit="$__shared_repo_bash_root/.profiles/educator_edit"

reset_vscode() {
	rm -rf "$__shared_repo_bash_root/.vscode"
	mkdir -p "$__shared_repo_bash_root/.vscode"
}

__cp() {
	if [[ $# -lt 2 ]]; then
		msg_stderr "Usage: __cp src [ src... ] dst"
		return 1
	fi

	local dst="${!#}"
	dst="${dst%/*}"

	set -- "${@:1:$#-1}"

	local src
	for src in "$@"; do
		local name=$(basename "$src")
		name="${name/#dot_/.}"
		echo -n 'cp '
		rm -rf "$dst/$name"
		cp -v "$src" "$dst/$name"
	done
}

__ln() {
	if [[ $# -lt 2 ]]; then
		msg_stderr "Usage: __ln src [ src... ] dst"
		return 1
	fi

	local dst="${!#}"
	dst="${dst%/*}"

	set -- "${@:1:$#-1}"

	local src
	for src in "$@"; do
		local name=$(basename "$src")
		name="${name/#dot_/.}"
		echo -n 'ln '
		ln -vsrf "$src" "$dst/$name"
	done
}

__ln_hard() {
	if [[ $# -lt 2 ]]; then
		msg_stderr "Usage: __ln_hard src [ src... ] dst"
		return 1
	fi

	local dst="${!#}"
	dst="${dst%/*}"

	set -- "${@:1:$#-1}"

	local src
	for src in "$@"; do
		local name=$(basename "$src")
		name="${name/#dot_/.}"
		echo -n 'ln (hard) '
		ln -vf "$src" "$dst/$name"
	done
}

reset_vscode_profile_student() {
	__cp "$__shared_repo_bash_student/dot_gitignore" "$__shared_repo_bash_root/"
	reset_vscode
	__cp "$__shared_repo_bash_student/dot_vscode/"* "$__shared_repo_bash_root/.vscode/"
}

__reset_vscode_profile_educator() {
	reset_vscode
	__ln "$__shared_repo_bash_educator/dot_vscode/"* "$__shared_repo_bash_root/.vscode/"
	__ln "$__shared_repo_bash_educator/dot_shellcheckrc" "$__shared_repo_bash_root/"
}

reset_vscode_profile_educator_present() {
	__cp "$__shared_repo_bash_educator/dot_gitignore" "$__shared_repo_bash_root/"
	__reset_vscode_profile_educator
	__ln "$__shared_repo_bash_educator_present/dot_vscode/"* "$__shared_repo_bash_root/.vscode/"
}

reset_vscode_profile_educator_edit() {
	__ln_hard "$__shared_repo_bash_educator/dot_gitignore" "$__shared_repo_bash_root/"
	__reset_vscode_profile_educator
	__ln "$__shared_repo_bash_educator_edit/dot_vscode/"* "$__shared_repo_bash_root/.vscode/"
	__cp "$__shared_repo_bash_educator/dot_vscode/tasks.json" "$__shared_repo_bash_root/.vscode/"
	sed -E -i 's_"runOn": "folderOpen"_"runOn": "default"_g' "$__shared_repo_bash_root/.vscode/tasks.json"
}
