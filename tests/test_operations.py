import pytest
from app.operation.operations import Add, Sub, Mul, Div

@pytest.mark.parametrize('a,b,expected', [
    (1,2,3),(2.5,0.5,3.0),(-1,1,0)
])
def test_add(a,b,expected):
    op = Add(a,b)
    assert op.compute(a,b) == expected

@pytest.mark.parametrize('a,b,expected', [
    (5,3,2),(0,0,0),(2.5,1.5,1.0)
])
def test_sub(a,b,expected):
    op = Sub(a,b)
    assert op.compute(a,b) == expected

@pytest.mark.parametrize('a,b,expected', [
    (2,3,6),(0,5,0),(2.5,4,10)
])
def test_mul(a,b,expected):
    op = Mul(a,b)
    assert op.compute(a,b) == expected

def test_div_normal():
    op = Div(6,3)
    assert op.compute(6,3) == 2

def test_div_by_zero():
    op = Div(1,0)
    with pytest.raises(ZeroDivisionError):
        op.compute(1,0)
