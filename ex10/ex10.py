import sys
import argparse

def parser_args():
    parser = argparse.ArgumentParser(
        description='Realize sth like "sort" command.'
    )
    parser.add_argument(
        'files_name',
        nargs='+',
        help='Filesname.'
    )
    parser.add_argument(
        '-f',
        '--case_unsensitive',
        action='store_true',
        help="Case unsensitive, I don't kown why it's called 'f'."
    )
    parser.add_argument(
        '-g',
        '--value',
        action='store_true',
        help="Compare the number,  I don't kown why it's called 'g'."
    )
    parser.add_argument(
        '-reverse',
        action='store_true',
        help='Invered order.'
    )
    return parser.parse_args()

def sorting(lines, settings):
    dict_lines = {}
    index = 0
    
    for line in lines:
        a_line = line
        
        if '-f' in settings:
            a_line = line.lower()
        if '-g' in settings:
            a_line = float(line)

        dict_lines.update({a_line: index})
        index += 1

    the_lines = list(dict_lines.keys())
    the_lines.sort()

    sorted_lines_keys = []
    for line_content in the_lines:
        sorted_lines_keys.append(dict_lines[line_content])

    sorted_lines = []
    for index in sorted_lines_keys:
        sorted_lines.append(lines[index])

    if '-r' in settings:
        final_lines = sorted_lines[::-1]
    else:
        final_lines = sorted_lines[:]

    for line in final_lines:
        print(line.strip())

def mode_set(reverse, case_unsensitive, value):
    settings = []

    if reverse:
        settings.append('-r')
    if case_unsensitive:
        settings.append('-f')
    if value:
        settings.append('-g')

    return settings

def sort_files_content(files_name, setting):
    for file in files_name:
        print('>>file: ', file)
        lines = open(file).readlines()
        sorting(lines, setting)

args = parser_args()
setting = mode_set(args.reverse, args.case_unsensitive, args.value)
sort_files_content(args.files_name, setting)
