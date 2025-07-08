
from gendiff.formatters import get_formatter

from .diff_builder import build_diff
from .file_loader import load_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    diff = build_diff(data1, data2)
    formatter = get_formatter(format_name)
    return formatter(diff)
    