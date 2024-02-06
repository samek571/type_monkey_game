# Type_monkey
A game I created as my first semester project at university

## Installation
1. To be able to play the game, just download `nltk` and `pygame` libraries, every other should be contained within the python installation you did a long time ago.
2. Afterwards, head to **Python Console** and download all the `nltk` data by entering `import nltk` and `nltk.download()`. Afterwards hit `import nltk` followed by a `nltk download('brown')` command.
It should be no surprise there is everything contained within, as you already downloaded `nltk_data` folder, however there might have been some updates...
3. Configure the correct interpreter right after opening the whole folder as project and you are ready to go. (It has been made in Python 3.9)

## Idea
The main idea is to improve typing skills on a computer keyboard (I see many people looking for letters and being inefficient as hell) yet still having at least some fun by playing this game.

## Start playing
Playing the game is pretty simple, just run the `game.py` file and...

(Motivation behind the game)
Killing zombies by explicitely writting out their name, you keep your house safe and not getting eaten by these ugly brain eating monsters. Make sure none of them is by the white circle line, otherwise game is over and your brain gets eaten.
By each killed zombie you are more skilled, therefore the experience (xp) gains. Each of the zombies carry positive number of money. Having enough xp results in new level which will be beneficial later.
There are abilities which might help killing the zombies. As if right now, abilites doesnt have a cooldown, therefore can be abused so the game is able to be played for an undefined period of time. Lets call this version a **Testnet Version**.
- By pressing `1` closest 5 zombies get killed
- By pressing `2` longest 5 zombies get killed
- By pressing `3` Mega crossbow shoots and kills as many zombies as possible within 15degree view
- By pressing `4` zombies stop spawning and moving, granting you 4 seconds to kill the rest of them


## Disclaimer
The front-end (or the stuff you see) is not really great, I am aware of that, nevertheless what is built is made properly without any bugs. Future updates are planned primarly and exclusively for the back-end, making the game more enjoyable and rich not through visuals, but rather through imagination (Potential updates might include futures as login, settings, shop to utilize coins and many more abilities as well as game modes).

(The whole project has been coded in Pycharm Community Edition and I dont want to be familiar with any other IDEs that are not from Jet Brains, especially visual studio code.)
