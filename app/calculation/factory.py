"""Factory to produce calculation instances based on operation name."""
from app.operation.registry import get_operation
from app.calculation.calculation import Calculation

class CalculationFactory:
    def create(self, op_name: str, a: float, b: float):
        op_cls = get_operation(op_name)
        if op_cls is None:
            raise ValueError(f'Unknown operation: {op_name}')
        op_instance = op_cls(a, b)
        # Wrap operation instance into Calculation for consistent API
        return Calculation(op_instance, a, b)
