from abc import ABC, abstractmethod
from typing import Set

class Employees(ABC):
    @abstractmethod
    def add(self, name: str, salary: int) -> int:
        pass

    @abstractmethod
    def getAll(self) -> Set[int]:
        pass

    @abstractmethod
    def getName(self, id: int) -> str:
        pass

    @abstractmethod
    def getSalary(self, id: int) -> int:
        pass

    @abstractmethod
    def changeSalary(self, id: int, newSalary: int):
        pass