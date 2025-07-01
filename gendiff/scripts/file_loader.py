import json

import yaml


def load_file(file_path):

    # Проверка расширения и загрузка файлов
    try:
        with open(file_path) as f:
            if file_path.endswith('.json'):
                return json.load(f)
            elif file_path.endswith(('.yaml', '.yml')):
                return yaml.safe_load(f)
            else:
                raise ValueError(f'Unsupported file format: {file_path}')
    except Exception as e:
        raise IOError(f'Error reading file {file_path}: {str(e)}')
