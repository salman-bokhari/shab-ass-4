# app/operation/base.py
from abc import ABC, abstractmethod

class OperationBase(ABC):
    """
    Abstract base class for all operations.
    Subclasses must implement the compute method.
    """
    name = "base"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def compute(self, a, b):
        """
        Perform the operation on a and b.
        Must be implemented by subclasses.
        """
        raise NotImplementedError  # pragma: no cover
