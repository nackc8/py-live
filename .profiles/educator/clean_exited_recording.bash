#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
	echo "Usage: $0 <record.cast>"
	exit 1
fi

record="$1"

# If the recording is tiny (e.g. cancelled session), delete it and bail
if [[ ! -f "$record" ]] || (($(wc -c <"$record") < 500)); then
	rm -f "$record"
	exit 0
fi

name="$(basename "$record")"
dir="$(dirname "$record")"
base="${name%.*}"

record_txt="$dir/${base}.txt"
record_html="$dir/${base}.html"

# Extract terminal output from the cast (JSON lines: [time, "o", text])
# then strip ANSI codes via ansifilter
python3 -c "
import sys, json
for line in open(sys.argv[1]):
    try:
        e = json.loads(line)
        if isinstance(e, list) and e[1] == 'o':
            sys.stdout.write(e[2])
    except Exception:
        pass
" "$record" | ansifilter -o "$record_txt"

python3 -c "
import sys, json
for line in open(sys.argv[1]):
    try:
        e = json.loads(line)
        if isinstance(e, list) and e[1] == 'o':
            sys.stdout.write(e[2])
    except Exception:
        pass
" "$record" | ansifilter -o "$record_html" --html
