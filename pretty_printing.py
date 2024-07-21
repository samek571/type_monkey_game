import pyfiglet
import re
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


def extract_text_outside_parentheses(text):
    depth = 0
    result = []
    skip_space = False

    for char in text:
        if char == '(':
            depth += 1
        elif char == ')':
            if depth > 0:
                depth -= 1
                skip_space = True
        elif depth == 0:
            if char != ' ':
                skip_space = False
            if not skip_space:
                result.append(char)

    return ''.join(result).strip()

#TODO separate ownedstuff to own fx
def print_game_progress(word, lvl, xp, coins, time, owned_stuff):
    print(pretty_print(word, font='stick_letters'))

    print(f"lvl: {lvl}")
    print(f"xp: {xp}")
    print(f"coins: {coins}")
    if "&" in word:
        print(f"Best time: {time}")
    else:
        print(f"This run time: {time}")

    if type(owned_stuff) == str: #cuz of the databaze...
        owned_stuff = eval(owned_stuff)

    if owned_stuff:
        print('\nowned_stuff: {')

        for k,v in owned_stuff.items():
            txt = extract_text_outside_parentheses(k) #handles just one bracket, no nested shits
            res = ''.join([match for match in txt if match]).strip()
            print(f"{res}: {v}")
        print("}")


#print_game_progress("a", 1,1,1,1, {"tst (ajsda+34js8shd) opel meriva": 62})
#print_game_progress("a", 1,1,1,1, {"tst ajsda+34js8shd": 62})
