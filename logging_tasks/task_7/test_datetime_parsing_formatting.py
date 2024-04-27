import unittest
from datetime import datetime
from ddt import ddt, data, unpack

@ddt
class TestDateTimeParsingAndFormatting(unittest.TestCase):

    @data(
        ("2022-01-01", "%Y-%m-%d", datetime(2022, 1, 1)),
        ("01/31/2022", "%m/%d/%Y", datetime(2022, 1, 31)),
        ("2022-12-31 23:59", "%Y-%m-%d %H:%M", datetime(2022, 12, 31, 23, 59)),
        ("15:04:05 2022-02-02", "%H:%M:%S %Y-%m-%d", datetime(2022, 2, 2, 15, 4, 5))
    )
    @unpack
    def test_strptime(self, date_str, formated, expected_date):
        parsed_date = datetime.strptime(date_str, formated)
        self.assertEqual(parsed_date, expected_date)

    @data(
        (datetime(2022, 1, 1), "%Y-%m-%d", "2022-01-01"),
        (datetime(2022, 1, 31), "%m/%d/%Y", "01/31/2022"),
        (datetime(2022, 12, 31, 23, 59), "%Y-%m-%d %H:%M", "2022-12-31 23:59"),
        (datetime(2022, 2, 2, 15, 4, 5), "%H:%M:%S %Y-%m-%d", "15:04:05 2022-02-02")
    )
    @unpack
    def test_strftime(self, date_obj, formated, expected_str):
        formatted_date = date_obj.strftime(formated)
        self.assertEqual(formatted_date, expected_str)

if __name__ == '__main__':
    unittest.main()