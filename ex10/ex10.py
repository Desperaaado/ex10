import sys
import argparse

def parser_args():
    parser = argparse.ArgumentParser(
        description='Realize sth like "sort" command.0'
    )
    parser.add_argument(
        '-reverse',
        action='store_true',
        help='Invered order.'
    )
    parser.parse_args()

def sorting():
    lines = sys.stdin.readlines()
    pure_lines = []
    for line in lines:
        pure_line = line.strip()
        if pure_line != '':
            file_name = pure_line.split(' ')[-1]
            pure_lines.append(file_name)
    order_lines = pure_lines[3:]
    print('>>>>', pure_lines[3:])
    
    for line in order_lines:
        print(line)

sorting()
