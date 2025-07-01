
def stringify(value, indent_level):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, dict):
        indent = ' ' * (indent_level * 4)
        inner_indent = ' ' * ((indent_level + 1) * 4)
        lines = []
        for k, v in value.items():
            lines.append(f'{inner_indent}{k}: {stringify(v, indent_level + 1)}')
        return '{{\n{}\n{}}}'.format('\n'.join(lines), indent)
        
    return str(value)


def format_stylish(diff, indent_level=0):
    base_indent = ' ' * (indent_level * 4)
    lines = []

    for node in diff:
        key = node['key']
        type_ = node['type']

        if type_ == 'nested':
            lines.append(f'{base_indent}    {key}: {{')
            lines.extend(format_stylish(node['children'], indent_level + 1))
            lines.append(f'{base_indent}    }}')
        elif type_ == 'changed':
            old = stringify(node['old_value'], indent_level + 1)
            new = stringify(node['new_value'], indent_level + 1)
            lines.append(f'{base_indent}  - {key}: {old}')
            lines.append(f'{base_indent}  + {key}: {new}')
        elif type_ == 'deleted':
            value = stringify(node['value'], indent_level + 1)
            lines.append(f'{base_indent}  - {key}: {value}')
        elif type_ == 'added':
            value = stringify(node['value'], indent_level + 1)
            lines.append(f'{base_indent}  + {key}: {value}')
        else:  # unchanged
            value = stringify(node['value'], indent_level + 1)
            lines.append(f'{base_indent}    {key}: {value}')

    return lines


def format(diff):
    lines = format_stylish(diff)
    return '{\n' + '\n'.join(lines) + '\n}'