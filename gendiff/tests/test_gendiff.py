import json

import pytest

import gendiff.tests.data
from gendiff.scripts.gendiff import generate_diff


def json_read(file_name):
    with open(f'gendiff/tests/data/{file_name}') as f:
        return json.load(f)
    

@pytest.mark.parametrize('file1, file2, expected_output', [
    (
    'file1.json',
    'file2.json',
    '''{
 - follow: False
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: True
}'''
    ),
    (
        'file1_v2.json',
        'file2_v2.json',
        '''{
 + cache: {'enabled': True, 'size': '500MB'}
 - follow: False
   host: hexlet.io
 - max_connections: 100
 - proxy: 123.234.53.22
 + proxy: 185.204.11.17
 - ssl: {'enabled': True, 'protocols': ['TLSv1.2', 'TLSv1.3']}
 + ssl: {'enabled': False, 'protocols': ['TLSv1.3']}
 - timeout: 50
 + timeout: 30
}'''
    )
])
def test_gendiff(file1, file2, expected_output):
    test_data1 = json_read(file1)
    test_data2 = json_read(file2)
    assert generate_diff(test_data1, test_data2) == expected_output