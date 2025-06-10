from gendiff.scripts.parser import custom_parse
from gendiff.scripts.gendiff import generate_diff
import json

def main():
    print("Hello from python-project-50!")
    json_read()
    print(generate_diff(json_read()['json_first_file'], json_read()['json_second_file']))

def json_read():
    return {'json_first_file': json.load(open(custom_parse()['first_file'])),
            'json_second_file': json.load(open(custom_parse()['second_file']))}

if __name__ == "__main__":
    main()