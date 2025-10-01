import pytest
from app.calculation.calculation import Calculation, CalculationHistory
from app.operation.operations import Add, Div
from app.calculation.factory import CalculationFactory

def test_calculation_execute_and_repr():
    op = Add(2,3)
    calc = Calculation(op, 2, 3)
    assert calc.execute() == 5
    assert 'add' in repr(calc).lower()

def test_history_add_and_items():
    history = CalculationHistory()
    op = Add(1,1)
    calc = Calculation(op,1,1)
    history.add(calc)
    assert history.items() == [calc]

def test_factory_create_known():
    factory = CalculationFactory()
    calc = factory.create('add', 4, 5)
    assert calc.execute() == 9

def test_factory_unknown():
    factory = CalculationFactory()
    with pytest.raises(ValueError):
        factory.create('unknown_op', 1, 2)

def test_division_by_zero_via_factory():
    factory = CalculationFactory()
    calc = factory.create('div', 1, 0)
    with pytest.raises(ZeroDivisionError):
        calc.execute()
