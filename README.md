# quiver-export
Python exporter for Quiver Notebooks.

## Usage

```
usage: quiver-export.py [-h] [-d] [-l] [-L LIBRARY] [-n NOTEBOOK]
                        [-o OUTPUT_DIR]

Quiver Export Script

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Debug mode.
  -l, --list            List all notebooks or notes if -n is used.
  -L LIBRARY, --library LIBRARY
                        Quiver library location (default: /Users/USERNAME/Lib
                        rary/Containers/com.happenapps.Quiver/Data/Library/App
                        lication Support/Quiver/Quiver.qvlibrary/).
  -n NOTEBOOK, --notebook NOTEBOOK
                        Specify the notebook to export.
  -o OUTPUT_DIR, --output OUTPUT_DIR
                        Specify the output directory.
```

## Examples

### List Notebooks

`./quiver-export.py -l`:

```
Notebooks:
  Inbox
  Quiver Tutorial
  Trash
```

### List Notes

`./quiver-export.py -n 'Quiver Tutorial' -l`:

```
Notebook: Quiver Tutorial
Notes:
  1 - Getting Started
  10 - Backup and Recovery
  11 - Import & Export
  12 - Preferences
  2 - Cell Types
  3 - Cell Operations
  4 - Images, Files and Links
  5 - Preview and Presentation
  6 - Full-Text Search
  7 - Tagging
  8 - Cloud Syncing
  9 - Team Collaboration
```

### Export

`mkdir -p ./tutorial && ./quiver-export.py -n 'Quiver Tutorial' -o ./tutorial`

`ls -l ./tutorial`:

```
ls -l ./tutorial
total 224
-rw-r--r--  1 dkerrigan  staff   245 Mar  2 13:43 1 - Getting Started.txt
-rw-r--r--  1 dkerrigan  staff   329 Mar  2 13:43 10 - Backup and Recovery.txt
-rw-r--r--  1 dkerrigan  staff   600 Mar  2 13:43 11 - Import & Export.txt
-rw-r--r--  1 dkerrigan  staff   313 Mar  2 13:43 12 - Preferences.txt
-rw-r--r--  1 dkerrigan  staff  1229 Mar  2 13:43 2 - Cell Types.md
-rw-r--r--  1 dkerrigan  staff   283 Mar  2 13:43 2 - Cell Types.txt
-rw-r--r--  1 dkerrigan  staff   197 Mar  2 13:43 3 - Cell Operations.txt
-rw-r--r--  1 dkerrigan  staff    71 Mar  2 13:43 4 - Images, Files and Links.md
-rw-r--r--  1 dkerrigan  staff    71 Mar  2 13:43 4 - Images, Files and Links.txt
-rw-r--r--  1 dkerrigan  staff   501 Mar  2 13:43 5 - Preview and Presentation.txt
-rw-r--r--  1 dkerrigan  staff   339 Mar  2 13:43 6 - Full-Text Search.txt
-rw-r--r--  1 dkerrigan  staff   220 Mar  2 13:43 7 - Tagging.txt
-rw-r--r--  1 dkerrigan  staff   180 Mar  2 13:43 8 - Cloud Syncing.txt
-rw-r--r--  1 dkerrigan  staff   810 Mar  2 13:43 9 - Team Collaboration.txt
```

#### Notes

Currently only supports txt and markdown formats.
