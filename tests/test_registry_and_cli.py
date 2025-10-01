from app.operation.registry import get_operation, OPERATIONS_HELP
from app.calculator.cli import parse_input, is_number

def test_get_operation_mapping():
    assert get_operation('add') is not None
    assert get_operation('+') is not None
    assert 'add' in OPERATIONS_HELP

def test_parse_input_commands():
    assert parse_input('help') == ('help', [])
    assert parse_input('history extra') == ('history', ['extra'])
    assert parse_input('add 1 2 3') == ('calc', ['add','1','2','3'])
    assert parse_input('   ') is None

def test_is_number_true_and_false():
    assert is_number('3.14')
    assert not is_number('three')
