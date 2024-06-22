import pyfiglet

import os
import subprocess
import platform

def clear_console():
    if "PYCHARM_HOSTED" in os.environ:
        print("\n" * 100)
    else:
        try:
            current_os = platform.system()
            if current_os == "Windows":
                subprocess.run("cls", shell=True, check=True)
            else:
                subprocess.run("clear", shell=True, check=True)
        except Exception as e:
            print("\n" * 100)

def _printall(text_to_print):
    fonts = pyfiglet.FigletFont.getFonts()
    print("Available fonts:", fonts)
    for word in fonts:
        figlet = pyfiglet.Figlet(word)
        print(figlet.renderText(text_to_print))

#print(_printall("hovno"))

def pretty_print(word, font='standard'):
    #figlet = pyfiglet.Figlet(font='georgia11')
    #figlet = pyfiglet.Figlet(font='stick_letters')
    figlet = pyfiglet.Figlet(font=font)
    return figlet.renderText(word)


def print_game_progress(word, lvl, xp, coins, time):
    print(pretty_print(word, font='stick_letters'))

    print(f"lvl: {lvl}")
    print(f"xp: {xp}")
    print(f"coins: {coins}")
    if "&" in word:
        print(f"Best time: {time}")
    else:
        print(f"This run time: {time}")
