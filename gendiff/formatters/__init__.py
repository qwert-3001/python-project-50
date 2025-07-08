

def get_formatter(name):
    if name == 'stylish':
        from .stylish import format
        return format
    if name == 'plain':
        from .plain import format
        return format
    if name == 'json':
        from .json import format_json
        return format_json
    raise ValueError(f'Unknow format: {name}')