from gendiff.scripts.parser import read_file


def test_parser(file1, file2, expected_output):
    test_file1 = file1
    test_file2 = file2
    
    assert read_file() == expected_output