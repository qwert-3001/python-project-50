import argparse
import json

import yaml


def read_file():

    first_file = custom_parse()['first_file']
    second_file = custom_parse()['second_file']

    # Проверка расширения и закгрузка файлов
    try:
        # Загрузка json файлов
        if first_file.endswith('.json') and second_file.endswith('.json'):
            with open(first_file) as file1, open(second_file) as file2:
                
                return {'first_file': json.load(file1),
                        'second_file': json.load(file2)}
        # Загрузка yaml файлов
        elif (first_file.endswith('.yaml') or first_file.endswith('.yml')) \
            and (second_file.endswith('.yaml') or second_file.endswith('.yml')):

            with open(first_file) as file1, open(second_file) as file2:
                
                return {'first_file': yaml.safe_load(file1),
                        'second_file': yaml.safe_load(file2)}
        else:
            raise ValueError('Unsupported format. Expected .json or .yaml/.yml')
            
    except (TypeError) as e:
        print(f'Format not support {e}')


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