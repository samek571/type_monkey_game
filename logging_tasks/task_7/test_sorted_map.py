import unittest
from sortedcontainers import SortedDict

class TestSortedDict(unittest.TestCase):
    def setUp(self):
        self.map = SortedDict()

    def test_add_new_mapping_unique_key(self):
        self.map["b"] = 2
        self.assertIn("b", self.map)
        self.assertEqual(self.map["b"], 2)
        self.assertEqual(len(self.map), 1)

    def test_add_new_mapping_existing_key(self):
        self.map["a"] = 1
        self.map["a"] = 2
        self.assertIn("a", self.map)
        self.assertEqual(self.map["a"], 2)
        self.assertEqual(len(self.map), 1)

    def test_remove_existing_element(self):
        self.map["a"] = 1
        del self.map["a"]
        self.assertNotIn("a", self.map)
        self.assertEqual(len(self.map), 0)

    def test_remove_all_elements_check_empty(self):
        self.map["a"] = 1
        self.map["b"] = 2
        self.map.clear()
        self.assertEqual(len(self.map), 0)

    def test_get_value_by_key(self):
        self.map["a"] = 1
        value = self.map["a"]
        self.assertEqual(value, 1)

    def test_get_value_for_nonexistent_key(self):
        with self.assertRaises(KeyError):
            value = self.map["nonexistent"]

    def test_iterator_state(self):
        self.map["c"] = 3
        self.map["a"] = 1
        self.map["b"] = 2
        keys = list(self.map)
        self.assertEqual(keys, ["a", "b", "c"])

    """comment out this for the task 3"""
    # def test_that_fails(self):
    #     self.map["a"] = 1
    #     self.assertEqual(self.map.get("b", None), 1, "Custom Error: 'b' does not map to 1")


if __name__ == '__main__':
    unittest.main()
