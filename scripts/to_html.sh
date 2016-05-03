#!/bin/bash

# Usage: ./scripts/to_html.sh path/to/notebook.qvnotebook path/to/output

CWD=$PWD
rm -rf "$2"
mkdir -p "$2" && cd "$2"
PROJECT=$PWD
NAME=$(basename "$PROJECT")
cd "$CWD" && cd "$1"
NOTEBOOK=$PWD
cd "$CWD" && cd $(dirname $0)/../
ROOT=$PWD
DOCROOT=$PWD/doc

$($ROOT/quiver-export.py -N "$NOTEBOOK" -o "$PROJECT")
cd "$PROJECT"
cp -R $DOCROOT/* ./

$(pandoc -s -S --toc -c "css/bootstrap.css" *.md -o "$NAME.html" --template "pandoc-template.html5" --toc-depth=5 --self-contained)
