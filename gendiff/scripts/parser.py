import argparse


def custom_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file',
                        help='Input your first file',
                        type=str)
    parser.add_argument('second_file',
                        help='Input your second file',
                        type=str)
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        choices=['plan', 'json'])
    args = parser.parse_args()
    return {'first_file': args.first_file, 'second_file': args.second_file}