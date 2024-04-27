## Logger

### Tasks 1-3
I have chosen my term project that has been written in python in the first semester and later on upgraded.

There are logs in `events.log` file, and by command `diff -u game.py game_with_logs.py > game_diff.txt` I created a diff file which should be in a readable format and give a brief info of what has been added to the original code. There are just basic logs when user logins or uses some ability...

### Tasks 4-6
`pip install memory_profiler` and take the same game as before, my term project

literally added 2 lines of code and ran the program by `python3 -m memory_profiler game_with_monitoring.py` via konsole. My laptop was lagging as hell, it was unplayable so i let it run like a minute and tried to type play it a little, use abilities. See the `stats.md` file for reports it has been giving.

Modifications are
One is `from memory_profiler import profile`
second `@profile`right above the `def playing(self):` method.


### Task 7
`pip install coverage` and we are using the program from previous lab session, the one that has unit tests. We move there with konsole commands and hit the followings;
`coverage run -m unittest test_sorted_map.py`
`coverage report -m`
`coverage html`

See the appropriate folder for konsole output


### Survey
(1) How new was the topic and content of the lab for you?
     4 I kinda had an image of something like this, it definitely had to exist because i thought about such tool several times while building my temr project

(2) Do you think that the content of this lab was useful?
     7 somewhat useful, it makes sense to keep track of memory usage when doing complicated recursion for example
(3) How do you evaluate the level of complexity of the homework assignment?
    kinda easier than i expect, maybe because python has everything integrated or lib for that particular thing.
(4) How do you evaluate your prior experience with the tool in the context of the homework assignment?
    8 I tried it for the first time except for the unittests that has been covered in prev lab, other than that i just knew something like this existed but never actually touched it
(5) How much time (in minutes) did you spend working on the homework assignment?
    somewhat around 2.5 hours?
