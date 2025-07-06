### Hexlet tests and linter status:
[![Actions Status](https://github.com/qwert-3001/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/qwert-3001/python-project-50/actions) [![Gendiff CI](https://github.com/qwert-3001/python-project-50/actions/workflows/makefile.yml/badge.svg)](https://github.com/qwert-3001/python-project-50/actions/workflows/makefile.yml) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=qwert-3001_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=qwert-3001_python-project-50)

Утилита для поиска отличий в конфигурационных файлах.

[![asciicast](https://asciinema.org/a/CIad8CL18YUhrE5O3KK90yvY9.svg)](https://asciinema.org/a/CIad8CL18YUhrE5O3KK90yvY9)

## Описание

Difference Calculator (gendiff) - это консольная утилита для определения различий между двумя структурами данных. Популярная задача, для которой существует множество онлайн сервисов. Подобный механизм используется при выводе тестов или при автоматическом отслеживании изменений в конфигурационных файлах.

### Возможности:
- Поддержка форматов: JSON, YAML
- Различные форматы вывода: stylish, plain, json
- Работа с вложенными структурами данных
- Консольный интерфейс

## Установка

### Системные требования
- Python 3.8+
- UV (https://docs.astral.sh/uv/)

### Установка из исходного кода

```bash
git clone https://github.com/qwert-3001/python-project-50.git
cd python-project-50
make install
```

## Использование

### Командная строка

```bash
source .venv/bin/activate
gendiff [--format FORMAT] first_file second_file
```

### Параметры

- `first_file` - путь к первому файлу
- `second_file` - путь ко второму файлу  
- `--format` - формат вывода (stylish, plain, json). По умолчанию: stylish

### Примеры использования

#### Сравнение JSON файлов
```bash
gendiff file1.json file2.json
```

#### Сравнение YAML файлов
```bash
gendiff file1.yaml file2.yaml
```

#### Вывод в формате plain
```bash
gendiff --format plain file1.json file2.json
```

#### Вывод в формате json
```bash
gendiff --format json file1.json file2.json
```

### Пример вывода

#### Stylish формат (по умолчанию)
```
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

#### Plain формат
```
Property 'follow' was removed
Property 'proxy' was removed  
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```

#### JSON формат
```json
[
  {
    "key": "follow",
    "type": "removed",
    "value": false
  },
  {
    "key": "timeout", 
    "type": "changed",
    "oldValue": 50,
    "newValue": 20
  }
]
```

## Использование как библиотека

```python
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2)
print(diff)

# С указанием формата
diff = generate_diff(file_path1, file_path2, format_name='plain')
print(diff)
```

## Разработка

### Запуск тестов

```bash
make test
```

### Проверка линтером

```bash
make lint
```

### Проверка покрытия тестами

```bash
make test-coverage
```

### Доступные команды Make

- `make install` - установка зависимостей
- `make test` - запуск тестов
- `make lint` - проверка кода линтером
- `make test-coverage` - проверка покрытия тестами  
- `make check` - полная проверка (линтер + тесты)
- `make build` - сборка пакета
- `make package-install` - установка пакета

## Технологии

- Python 3.8+
- UV - Python package
- PyYAML - работа с YAML файлами
- Pytest - тестирование
- Flake8 - линтинг
- GitHub Actions - CI/CD
- CodeClimate - анализ качества кода
