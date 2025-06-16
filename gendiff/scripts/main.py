from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parser import read_file


def main():
    print("Starting diff two file")
    print(generate_diff(read_file()['first_file'],
                        read_file()['second_file']))


if __name__ == "__main__":
    main()