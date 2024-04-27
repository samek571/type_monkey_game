from Employees import Employees

class Statistics:
    def __init__(self, employees: Employees):
        self.employees = employees

    def computeAverageSalary(self) -> int:
        salary = sum(self.employees.getSalary(idx) for idx in self.employees.getAll())
        n = len(self.employees.getAll())
        return salary // n if n > 0 else 0

    def getMinSalary(self) -> int:
        return min((self.employees.getSalary(idx) for idx in self.employees.getAll()), default=0)

    def printSalariesByName(self):
        employees_by_name = sorted(((self.employees.getName(idx), self.employees.getSalary(idx))
                                    for idx in self.employees.getAll()), key=lambda x: x[0])
        for name, salary in employees_by_name:
            print(f"{name}: {salary}")
