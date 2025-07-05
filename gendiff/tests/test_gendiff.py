import os

import pytest

from gendiff.scripts.gendiff import generate_diff

FIXTURE_PATH = 'gendiff/tests'
DATA_DIR = os.path.join(FIXTURE_PATH, 'test_data')
EXPECTED_DIR = os.path.join(FIXTURE_PATH, 'test_data/test_expected')

TEST_CASES = [
    # flat stylish
    ('flat_1.json', 'flat_2.json', 'flat_stylish.txt', 'stylish'),
    ('flat_1.yaml', 'flat_2.yaml', 'flat_stylish.txt', 'stylish'),
    # flat plain
    ('flat_1.json', 'flat_2.json', 'flat_plain.txt', 'plain'),
    ('flat_1.yaml', 'flat_2.yaml', 'flat_plain.txt', 'plain'),

    # nested stylish
    ('nested_1.json', 'nested_2.json', 'nested_stylish.txt', 'stylish'),
    ('nested_1.yaml', 'nested_2.yaml', 'nested_stylish.txt', 'stylish'),

    # nested plain
    ('nested_1.json', 'nested_2.json', 'nested_plain.txt', 'plain'),
    ('nested_1.yaml', 'nested_2.yaml', 'nested_plain.txt', 'plain')
]


def read_file(file_path):
    with open(file_path) as f:
        return f.read().strip()
    

@pytest.mark.parametrize('file1, file2, expected_file, format_name', TEST_CASES)
def test_gendiff(file1, file2, expected_file, format_name):
    file1_path = os.path.join(DATA_DIR, file1)
    file2_path = os.path.join(DATA_DIR, file2)
    expected_path = os.path.join(EXPECTED_DIR, expected_file)

    result = generate_diff(file1_path,
                           file2_path,
                           format_name=format_name).strip()

    expected = read_file(expected_path)

    assert result == expected