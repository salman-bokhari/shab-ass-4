"""Calculation objects and history management."""
from app.operation.base import OperationBase

class Calculation:
    def __init__(self, operation: OperationBase, a: float, b: float):
        self.operation = operation
        self.a = a
        self.b = b

    def execute(self):
        return self.operation.compute(self.a, self.b)

    def __repr__(self):
        return f"{self.operation.name}({self.a}, {self.b}) = {self.execute()}"

class CalculationHistory:
    def __init__(self):
        self._items = []

    def add(self, calc: Calculation):
        self._items.append(calc)

    def items(self):
        return list(self._items)
