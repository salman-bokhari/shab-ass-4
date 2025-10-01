"""Base operation definitions."""
from abc import ABC, abstractmethod

class OperationBase(ABC):
    name = 'base'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def compute(self, a, b):
        raise NotImplementedError
