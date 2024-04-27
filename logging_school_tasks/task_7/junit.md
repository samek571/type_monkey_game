## Task 1-3

```sh
samuel@finkbuk:~/Downloads$ python3 -m unittest test_sorted_map.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
```

```sh
samuel@finkbuk:~/Downloads$ python3 -m unittest test_sorted_map.py 
.......F
======================================================================
FAIL: test_that_fails (sorted_map.TestSortedDict)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/samuel/Downloads/test_sorted_map.py", line 52, in test_that_fails
    self.assertEqual(self.map.get("b", None), 1, "Custom Error: 'b' does not map to 1")
AssertionError: None != 1 : Custom Error: 'b' does not map to 1

----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (failures=1)
```

## Task 4-7
```sh
samuel@finkbuk:~/Downloads$ python3 -m unittest test_statistics.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

```shell
samuel@finkbuk:~/Downloads$ python3 -m unittest test_datetime_parsing_formatting.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.002s

OK
```

## Task 8
Contained within mail 