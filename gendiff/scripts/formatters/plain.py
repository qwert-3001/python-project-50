

def format_plain(diff, path=''):
    lines = []

    for node in diff:
        key = node['key']
        type_ = node['type']
        current_path = f'{path}.{key}' if path else key  # if - del point start

        if type_ == 'nested':
            lines.extend(format_plain(node['children'], current_path))
        elif type_ == 'changed':
            if (isinstance(node['old_value'], dict)):
                lines.append(f"Property '{current_path}' was updated."
                             f"From [complex value]"
                             f"to '{node['new_value']}'")
            elif (isinstance(node['new_value'], dict)):
                lines.append(f"Property '{current_path}' was updated."
                             f"From '{node['old_value']}'"
                             f"to [complex value]")
            else:
                lines.append(f"Property '{current_path}' was updated."
                             f"From '{node['old_value']}'"
                             f"to '{node['new_value']}'")
        elif type_ == 'deleted':
            lines.append(f"Property '{current_path}' was removed")
        elif type_ == 'added':
            if (isinstance(node['value'], dict)):
                lines.append(f"Property '{current_path}' was added "
                             f"with value: [complex value]")
            else:
                lines.append(f"Property '{current_path}' was added "
                             f"with value: '{node['value']}'")
        
    return lines
    

def format(diff):
    lines = format_plain(diff)
    return '\n'.join(lines) + '\n'