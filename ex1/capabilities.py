from abc import ABC, abstractmethod
from typing import Optional, Any


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Optional[Any] = None) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
