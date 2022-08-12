from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def Side(self):
        pass
class square(Shape):
    def Side(self):
        return 4
sq = square()
print(sq.Side())
# Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared, but contains no implementation. Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.