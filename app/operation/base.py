import pytest
from app.operation.base import OperationBase

def test_base_compute_not_implemented():
    class DummyOp(OperationBase):
        pass
    op = DummyOp(1, 2)
    with pytest.raises(NotImplementedError):
        op.compute(1, 2)
