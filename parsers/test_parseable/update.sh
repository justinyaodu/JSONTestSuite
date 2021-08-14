#!/bin/sh
for file in example_json.py parseable.py; do
	curl -O https://raw.githubusercontent.com/justinyaodu/parseable/main/$file
done
