#!/bin/bash

if [[ $# -ne 2 ]]; then
	echo "Usage: $0 <record> <record_timing>"
	exit 1
fi

record="$1"
record_timing="$2"

read -r size _ < <(wc -c "$record")
if ((size < 500)); then
	rm -f "$record" "$record_timing"
	exit
fi

name=$(basename "$record")
record_cleaned_txt="$(dirname "$record")/${name%.*}_cleaned.txt"
record_cleaned_html="$(dirname "$record")/${name%.*}_cleaned.html"

ansifilter -i "$record" -o "$record_cleaned_txt"
ansifilter -i "$record" -o "$record_cleaned_html" --html
