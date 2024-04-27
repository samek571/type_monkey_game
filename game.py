import collections
import random
import math

#my files that are used just os it doesnt look ugly
import level_definition
import point_generator
import random_word
from rendering_the_game import Render
from killer_functions import Kill
import userdb


#making sure it defo downloads the dependencies into the same directory as we play in
import pygame
import nltk
from nltk.corpus import brown


'''interesting stuff'''
def login(name=None, password=None):
    conn = userdb.create_connection(db_file='users.db')
    userdb.create_table(conn)


    if name is None and password is None:
        name = input("Enter your username: ")
        password = input("Enter your password: ")
    user_exists, password_correct, tmp_lvl, tmp_xp, tmp_coins, tmp_time = userdb.check_user(conn, name, password)


    if user_exists and password_correct:
        print(f"Welcome back, {name}! Login successful.")
        return conn, name, tmp_lvl, tmp_xp, tmp_coins, tmp_time
    elif user_exists and not password_correct:
        print("Incorrect password.")
        exit()  # Or handle this scenario differently
    else:
        print(f"User {name} not found.")
        response = input("Would you like to register? (yes/no): ")
        if response.lower() == 'yes':
            userdb.add_user(conn, name, password)  # Here, ensure password hashing
            print("You are registered and logged in.")
            return conn, name, 0, 0, 0, None  # Assuming new user starts with no progress
        else:
            print("You need to register to play.")
            exit()


class Main:
    def __init__(self, tmp_lvl, tmp_xp, tmp_coins):
        self.coins = tmp_coins
        self.lvl, self.xp = level_definition.determinator(tmp_lvl, tmp_xp)

        self.height = 1000
        self.width = math.floor(1.618 * 1000)
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.x_origin, self.y_origin = self.width // 2, self.height
        self.font = pygame.font.Font(None, 36)

        #words
        self.banned_area_game_end = 404
        self.cold_factor = 1.25 #higher~faster TODO make it progressively fast
        self.words_spawnrate = 1000 #time in ms
        self.word_theme = ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
        self.min_word_len = 3
        self.max_word_len = 8

        self.typed_text = ''
        self.words_on_screen = collections.defaultdict(tuple)
        self.text_x, self.text_y = self.width // 2, 10
        self.words_on_screen[random_word.get_word(self.word_theme, self.min_word_len, self.max_word_len)] =\
            (point_generator.random_point_generator(self.banned_area_game_end, self.width, self.height, self.x_origin, self.y_origin))

        self.renderer = Render(self.screen, self.font, self.width, self.x_origin, self.y_origin)
        self.word_freqs = nltk.FreqDist(w.lower() for w in brown.words())
        
        #abilities
        self.last_time_used_abillity = [0,0,0,0,0]
        self.abillity_cooldown = [6000, 12000, 7000, 16000, 2000]
        self.abillity_strength = [8,5,15,4000,8]


    def update_text_position(self):
        total_text_width, _ = self.font.size(self.typed_text)
        self.text_x = (self.width - total_text_width) // 2


    def playing(self):
        screen_width, screen_height = self.screen.get_size()
        button_width, button_height = screen_width * 0.1, screen_height * 0.1
        button_x, button_y = screen_width - button_width - 10, 10

        last_update_time_new_word = pygame.time.get_ticks()
        last_update_time_render = pygame.time.get_ticks()
        time_to_boot = pygame.time.get_ticks()

        while True:
            curr_time = pygame.time.get_ticks()
            time_age = round((curr_time- time_to_boot)/1000, 2)

            for event in pygame.event.get():

                # esc / check if mouse has been pressed - for safe exit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if (button_x <= mouse_x <= button_x + button_width) and (
                            button_y <= mouse_y <= button_y + button_height):
                        return self.lvl, self.xp, self.coins, time_age


                # if something has been pressed on the keyboard
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # different pullout methode - no need to use mouse to stop playing
                        return self.lvl, self.xp, self.coins, time_age

                    elif (pygame.key.get_mods() & pygame.KMOD_CTRL) and (
                            event.key == pygame.K_BACKSPACE or event.key == pygame.K_a):
                        self.typed_text = ''
                        self.update_text_position()

                    elif event.key == pygame.K_BACKSPACE:
                        self.typed_text = self.typed_text[:-1]
                        self.update_text_position()

                    # submission of a word, check if word is in the game
                    if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        self.typed_text = ''
                        self.update_text_position()


                    # Abilities
                    elif event.key in {pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5}: #TODO abillity to bind this shit
                        kill = Kill(self.x_origin, self.y_origin, self.words_on_screen)
                        killed_points = []
                        pushed_points = []

                        # kill p closest words
                        if event.key == pygame.K_1:
                            if (curr_time - self.last_time_used_abillity[0]) > self.abillity_cooldown[0]:
                                self.last_time_used_abillity[0] = curr_time
                                killed_points = kill.kill_p_closest(self.abillity_strength[0]) #TODO inheret value based on the shop

                        # kill some longest words
                        elif event.key == pygame.K_2:
                            if (curr_time - self.last_time_used_abillity[1]) > self.abillity_cooldown[1]:
                                self.last_time_used_abillity[1] = curr_time
                                killed_points = kill.kill_q_longest(self.abillity_strength[1]) #TODO inherent value based on the shop

                        # kill as much as possible in certain angle; max words killed in angle #nlgn hard leetcode problem #1610
                        elif event.key == pygame.K_3:
                            if (curr_time - self.last_time_used_abillity[2]) > self.abillity_cooldown[2]:
                                self.last_time_used_abillity[2] = curr_time
                                killed_points = kill.kill_in_angle(self.abillity_strength[2]) #TODO inheret value based on the shop

                        # stop production for certain time
                        elif event.key == pygame.K_4:
                            if (curr_time - self.last_time_used_abillity[3]) > self.abillity_cooldown[3]:
                                self.last_time_used_abillity[3] = curr_time
                                last_update_time_new_word += self.abillity_strength[3] #TODO inheret value based on the shop

                        # push-back some closest elements
                        elif event.key == pygame.K_5:
                            if (curr_time - self.last_time_used_abillity[4]) > self.abillity_cooldown[4]:
                                self.last_time_used_abillity[4] = curr_time
                                pushed_points = kill.kill_p_closest(self.abillity_strength[4])


                        for p in killed_points:
                            del self.words_on_screen[p[-1]]

                        for point in pushed_points:
                            x,y, word = point[1], point[2], point[-1]

                            dx = x - self.x_origin
                            dy = y - self.y_origin
                            distance = math.sqrt(dx ** 2 + dy ** 2)
                            kickback_factor = random.uniform(0.05, 0.15)
                            new_distance = distance * (1 + kickback_factor)
                            new_x = self.x_origin + (dx / distance) * new_distance
                            new_y = self.y_origin + (dy / distance) * new_distance
                            self.words_on_screen[word] = (new_x, new_y)


                    # display the pressed letter
                    elif ((65 <= event.key <= 90) or (97 <= event.key <= 122)) and not (pygame.key.get_mods() & pygame.KMOD_CTRL):
                        # kick back exactly the size of the letter in case it isnt monospaced
                        char_width, _ = self.font.size(event.unicode)
                        self.typed_text += event.unicode

                        if self.typed_text in self.words_on_screen:
                            deleted_word = self.typed_text
                            del self.words_on_screen[self.typed_text]

                            rank = self.word_freqs[deleted_word]
                            a,b = 1,10
                            word_value = (a+((b-a)*(rank-1)/2500))

                            self.xp += word_value
                            self.coins += word_value
                            self.lvl, self.xp = level_definition.determinator(self.lvl, self.xp)
                            self.xp, self.lvl, self.coins = round(self.xp,2), round(self.lvl,2), round(self.coins,2)
                            self.typed_text = ''
                        self.update_text_position()

            # rendering and shit
            abillity_render = [False] * len(self.abillity_cooldown)
            if (curr_time - last_update_time_render) > 40: #this is a constant and wont change
                last_update_time_render = curr_time

                _q, new_words_on_screen = point_generator.update_all_points(self.banned_area_game_end, self.x_origin, self.y_origin, self.words_on_screen, self.cold_factor)
                if _q: return self.lvl, self.xp, self.coins, time_age
                self.words_on_screen = new_words_on_screen


                if (curr_time - last_update_time_new_word) > self.words_spawnrate:
                    last_update_time_new_word = curr_time
                    self.words_on_screen[random_word.get_word(self.word_theme, self.min_word_len, self.max_word_len)] = point_generator.random_point_generator(self.banned_area_game_end, self.width, self.height, self.x_origin, self.y_origin)


                for i in range(len(self.abillity_cooldown)):
                    if (curr_time - self.last_time_used_abillity[i]) > self.abillity_cooldown[i]:
                        abillity_render[i] = True

                self.renderer.render_all(self.banned_area_game_end, self.typed_text, self.text_x, self.text_y, self.words_on_screen, self.lvl, self.xp, self.coins, time_age, abillity_render)

def main():
    session_token = True

    #autologin testnet
    conn, name, lvl, xp, coins, time = login(name='cigan', password='cigan')
    #conn, name, lvl, xp, coins, time = login(name=None, password=None)
    # TODO prompt shop
    # TODO prompt gamemode

    while session_token:
        pygame.init()
        pygame.display.set_caption("Type monkey")
        pygame.time.Clock().tick(10)
        game = Main(lvl, xp, coins)
        lvl, xp, coins, time = game.playing()

        userdb.update_progress(conn, name, lvl, xp, coins, time)
        print('\nlvl xp coins time')
        print(lvl, xp, coins, time)
        pygame.quit()

        #TODO prompt shop aswell
        choice = input("\nDo you want to play again or log out? (play/log out): ").lower()
        if choice in {"log out", "out", "no", "logout"}:
            session_token = False


if __name__ == '__main__': main()