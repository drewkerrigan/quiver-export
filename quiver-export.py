#!/usr/bin/python

"""
Quiver Export Script
Provides manipulation of Quiver.qvlibrary based Notebooks.
"""

import json
import argparse
from getpass import getuser
from os import listdir
from os.path import isfile, join

DEFAULT_LIBRARY = '/Users/' + getuser() + '/Library/Containers/com.happenapps.Quiver/\
Data/Library/Application Support/Quiver/Quiver.qvlibrary/'
DEFAULT_OUTPUT = './output'


def debug(args, val):
    if(args.debug):
        print(val)


def parseArgs():
    parser = argparse.ArgumentParser(description='Quiver Export Script')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Debug mode.')
    parser.add_argument('-l', '--list', dest='list_items',
                        action='store_true',
                        help='List all notebooks or notes if -n is used.')
    parser.add_argument('-L', '--library', dest='library',
                        help='Quiver library location (default: ' +
                        DEFAULT_LIBRARY + ').')
    parser.add_argument('-n', '--notebook', dest='notebook',
                        help='Specify the notebook to export.')
    parser.add_argument('-o', '--output', dest='output_dir',
                        help='Specify the output directory.')
    return parser.parse_args()


def ls(path):
    f = []
    d = []
    for des in listdir(path):
        if isfile(join(path, des)):
            f.append(des)
        else:
            d.append(des)
    f.sort()
    d.sort()
    return f, d


def list_notes(args, notebook):
    n = []
    _, d = ls(join(args.library, notebook['path']))
    for note in d:
        file_path = join(args.library, notebook['path'], note)
        with open(join(file_path, 'meta.json')) as data_file:
            data = json.load(data_file)
            n.append({'name': data['title'], 'path': file_path})
    return n


def list_notebooks(args):
    n = []
    _, d = ls(args.library)
    for notebook in d:
        file_path = join(args.library, notebook)
        with open(join(file_path, 'meta.json')) as data_file:
            data = json.load(data_file)
            n.append({'name': data['name'], 'path': file_path})
    return n


def get_notebook(args):
    nb = None
    n = list_notebooks(args)
    n.sort()
    for notebook in n:
        if notebook['name'] == args.notebook:
            nb = notebook
    return nb


def export(args, notebook, notes):
    c = []
    for note in notes:
        file_path = join(args.library, notebook['path'], note['path'])
        with open(join(file_path, 'content.json')) as data_file:
            data = json.load(data_file)
            c.append(data)
            for cell in data['cells']:
                ext = 'txt'
                if cell['type'] == 'markdown':
                    ext = 'md'
                export_filename = join(args.output_dir,
                                       note['name'] + '.' + ext)
                debug(args, 'Writing to file: ' + export_filename)
                target = open(export_filename, 'w')
                target.write(cell['data'].encode('utf-8'))


if __name__ == "__main__":
    args = parseArgs()
    if args.library is None:
        args.library = DEFAULT_LIBRARY
    if args.output_dir is None:
        args.output_dir = DEFAULT_OUTPUT
    debug(args, 'Args: ' + str(args))
    if args.notebook is None:
        if args.list_items:
            n = list_notebooks(args)
            n.sort()
            print 'Notebooks: '
            for notebook in n:
                print '  ' + notebook['name']
            exit(0)
    else:
        notebook = get_notebook(args)
        notes = list_notes(args, notebook)
        notes.sort()
        if args.list_items:
            print 'Notebook: ' + notebook['name']
            print 'Notes:'
            for note in notes:
                print '  ' + str(note['name'])
            exit(0)

        export(args, notebook, notes)
    exit(0)
