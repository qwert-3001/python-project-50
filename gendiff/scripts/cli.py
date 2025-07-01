import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Shows difference between files'
    )
    parser.add_argument('first_file',
                        help='Path to your first file',
                        type=str)
    parser.add_argument('second_file',
                        help='Path to your second file',
                        type=str)
    parser.add_argument('-f', '--format',
                        type=str,
                        default='stylish',
                        choices=['plan', 'json', 'stylish'],
                        help='Set format of output')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    print(args)