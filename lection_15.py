from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Super class
    """

    def __init__(self, name: str, eyes: int = 2, legs: int = 0, wings: int = 0):
        super().__init__()

    @abstractmethod
    def sleap():
        """
        Sleap some minutes
        :param minutes: time in minutes
        """

    def __str__(self) -> str:
        return super().__str__()
    
class Fish(Animal):
    """
    Fish class
    """