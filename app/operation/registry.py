"""Registry for operations and helpers."""
from .operations import Add, Sub, Mul, Div

_MAP = {
    'add': Add,
    '+': Add,
    'sub': Sub,
    '-': Sub,
    'mul': Mul,
    '*': Mul,
    'div': Div,
    '/': Div,
}

OPERATIONS_HELP = ', '.join(sorted(set(k for k in _MAP.keys() if len(k)>0)))

def get_operation(name: str):
    return _MAP.get(name.lower())
