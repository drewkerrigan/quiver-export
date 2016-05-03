#!/bin/bash

# Usage: ./scripts/to_html.sh path/to/notebook.qvnotebook path/to/output

CWD=$PWD
cd "$2"
PROJECT=$PWD
NAME=$(basename "$PROJECT")
cd "$CWD" && cd "$1"
NOTEBOOK=$PWD
cd "$CWD" && cd $(dirname $0)/../
ROOT=$PWD
DOCROOT=$PWD/doc
$($ROOT/quiver-export.py -N "$NOTEBOOK" -o "$PROJECT")
cd "$PROJECT"
$(pandoc -s -S --toc -c "$DOCROOT/css/bootstrap.css" *.md -o "$NAME.html" --template "$DOCROOT/pandoc-template.html5" --toc-depth=5 --self-contained)
