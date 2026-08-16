from abc import ABC, abstractmethod

class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        ...

class TransformCapability(ABC):
    transformed = False

    @abstractmethod
    def transform(self) -> str:
        ...
    
    @abstractmethod
    def revert(self) -> str:
        ...