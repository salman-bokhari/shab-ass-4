"""Concrete arithmetic operations."""
from .base import OperationBase

class Add(OperationBase):
    name = 'add'
    def compute(self, a, b):
        return a + b

class Sub(OperationBase):
    name = 'sub'
    def compute(self, a, b):
        return a - b

class Mul(OperationBase):
    name = 'mul'
    def compute(self, a, b):
        return a * b

class Div(OperationBase):
    name = 'div'
    def compute(self, a, b):
        # EAFP pattern: try and handle ZeroDivisionError inside
        try:
            return a / b
        except ZeroDivisionError:
            raise ZeroDivisionError('Division by zero is not allowed')
