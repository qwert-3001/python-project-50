
def build_diff(file1, file2):

    if not file1 and not file2:
        return []
    
    diff = []
    keys = sorted(set(file1.keys() | set(file2.keys())))

    for key in keys:
        value1 = file1.get(key)
        value2 = file2.get(key)

        if key not in file2:
            diff.append({
                'key': key,
                'type': 'deleted',
                'value': value1
            })
        elif key not in file1:
            diff.append({
                'key': key,
                'type': 'added',
                'value': value2
            })
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(value1, value2)
            })
        elif value1 == value2:
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': value1
            })
        else:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': value1,
                'new_value': value2
            })
    return diff