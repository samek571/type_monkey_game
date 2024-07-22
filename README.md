# Type Monkey Game
A game that I developed in my first semester at the university, got upgraded later on.
The main idea is to improve typing skills on a computer keyboard (I see many people looking for letters and being inefficient as hell) yet still having at least some fun by playing this game.


## Installation
It should be as simple as running `run_me_first.py` once.

### If that doesnt work;
1. Google up `how to allow pip instalation` and maybe approximate your machine OS. 
2. Run the following commands in Konsole to download dependency libraries, every other should be contained within the python installation.
   1. `pip install bcrypt`
   2. `pip install nltk`
   3. `pip install pygame`
   4. `pip install pyfiglet`
3. You might need to configure the correct interpreter (3.10) right after opening the whole folder as project and that should be it, you are ready to go.
4. If there are troubles nevertheless, google up or use an A.I. tool that could assist you. Any of the following should get the job done `GPT4`, `Claude`, `Devin`
(In case of further troubles please contact me via GitHub)

## Start playing
Playing the game is pretty simple, just run the `game.py` file and...
Alternatively open a cmd or konsole, navigate to the folder you just downloaded and enter `chmod +x game.py` (it just grants permission to execute the file), then type `python3 game.py` and you are playing :)

### Motivation behind the game
Killing zombies by explicitly writing out their name, you keep your house safe and not getting eaten by these ugly brain eating monsters. Make sure none of them is by the white circle line (your home), otherwise game is over and your brain gets eaten.
By each killed zombie you are more skilled, therefore the experience (xp) gains. Each of the zombies carry positive number of money. Having enough xp results in a new level which will be beneficial later.
There are abilities which might help killing the zombies however, each of them has some cooldown.
- By pressing `1` closest 5 zombies get killed
- By pressing `2` longest 5 zombies get killed
- By pressing `3` Mega crossbow shoots and kills as many zombies as possible within 15degree view
- By pressing `4` zombies stop spawning and moving, granting you 4 seconds to kill the rest of them
- By pressing `5` few closest zombies get pushed away

Let's call this version a **First Working Version** as there is a functional login database and the game has purpose, just isnt top-tier

## Future Updates?
- more game modes (+languages)
- progressive speed of the points
- settings
- many more bind-able abilities 
- nicer gui
- imporved performance
- autopilot sub-game

## Disclaimer
The front-end is not really great, I am aware of that, nevertheless what is built should be functional without any bugs. 
Future updates are planned primarily and exclusively for the back-end, making the game more enjoyable.
(The whole project has been made in Pycharm Community Edition and I don't want to be familiar with any other non Jet-Brains IDEs, especially visual studio code.)

