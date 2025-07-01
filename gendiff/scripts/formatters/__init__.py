

def get_formatter(name):
    if name == 'stylish':
        from .stylish import format
        return format
    if name == 'plain':
        from .plain import format
        return format
    if name == 'json':
        from .json import format
        return format
    raise ValueError(f'Unknow format: {name}')