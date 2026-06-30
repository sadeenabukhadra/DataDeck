from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self, transformed: bool):
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revernt(self) -> str:
        pass
