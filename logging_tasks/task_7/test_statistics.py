import unittest
from unittest.mock import MagicMock
from statistics import Statistics
from Employees import Employees


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.q_employees = MagicMock()
        self.statistics = Statistics(self.q_employees)

    def test_compute_average_salary(self):
        self.q_employees.getAll.return_value = {1, 2, 3}
        self.q_employees.getSalary.side_effect = [50000, 60000, 55000]

        avg = self.statistics.computeAverageSalary()
        self.assertEqual(avg, 55000, "Average salary should be 55000")

    def test_get_min_salary(self):
        self.q_employees.getAll.return_value = {1, 2, 3}
        self.q_employees.getSalary.side_effect = [50000, 60000, 40000]

        min_salary = self.statistics.getMinSalary()
        self.assertEqual(min_salary, 40000, "Minimum salary should be 40000")

    def test_print_salaries_by_name(self):
        self.q_employees.getAll.return_value = {1, 2, 3}
        self.q_employees.getName.side_effect = ["Charlie", "Alice", "Bob"]
        self.q_employees.getSalary.side_effect = [55000, 50000, 60000]

        with unittest.mock.patch('builtins.print') as q_print:
            self.statistics.printSalariesByName()
            expected = [unittest.mock.call('Alice: 50000'), unittest.mock.call('Bob: 60000'), unittest.mock.call('Charlie: 55000')]
            q_print.assert_has_calls(expected, any_order=False)

if __name__ == '__main__':
    unittest.main()
