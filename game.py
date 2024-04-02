import collections
import random
import math

#my files that are used just os it doesnt look ugly
import level_definition
import point_generator
import random_word
from rendering_the_game import Render
from killer_functions import Kill


#making sure it defo downloads the dependencies into the same directory as we play in
import nltk
from nltk.corpus import brown
import os
import pygame
current_directory = os.path.dirname(os.path.abspath(__file__))
nltk_data_directory = os.path.join(current_directory, 'nltk_data')
nltk.data.path.append(nltk_data_directory)
nltk.download('brown', download_dir=nltk_data_directory)
#TODO basically same shit for pygame lib, nonpythonist wont play jackshit


pygame.init()
pygame.display.set_caption("Type monkey")

dimension = 1000
width, height = math.floor(1.618 * dimension), dimension
screen = pygame.display.set_mode((width, height))
x_origin, y_origin = width // 2, height
font = pygame.font.Font(None, 36)
word_freqs = nltk.FreqDist(w.lower() for w in brown.words())

class Main:
    def __init__(self):
        self.coins = 0
        self.lvl, self.xp = level_definition.determinator(0, 0)
        self.banned_area_game_end = 404

        #words
        self.cold_factor = 0.5 #TODO make it progressively fast
        self.words_spawnrate = 1000 #time in ms
        self.word_theme = ['lore', 'news']
        self.min_word_len = 3
        self.max_word_len = 8

        self.typed_text = ''
        self.words_on_screen = collections.defaultdict(tuple)
        self.text_x, self.text_y = width // 2, 10
        self.words_on_screen[random_word.get_word(self.word_theme, self.min_word_len, self.max_word_len)] =\
            (point_generator.random_point_generator(self.banned_area_game_end, width, height, x_origin, y_origin))

        self.renderer = Render(screen, width, font, x_origin, y_origin)


    def update_text_position(self):
        total_text_width, _ = font.size(self.typed_text)
        self.text_x = (width - total_text_width) // 2


    def playing(self):
        screen_width, screen_height = screen.get_size()
        button_width, button_height = screen_width * 0.1, screen_height * 0.1
        button_x, button_y = screen_width - button_width - 10, 10

        last_update_time_new_word = pygame.time.get_ticks()
        last_update_time_render = pygame.time.get_ticks()

        while True:
            for event in pygame.event.get():

                # esc / check if mouse has been pressed - for safe exit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if (button_x <= mouse_x <= button_x + button_width) and (
                            button_y <= mouse_y <= button_y + button_height):
                        return self.lvl, self.xp, self.coins


                # if something has been pressed on the keyboard
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # different pullout methode - no need to use mouse to stop playing
                        return self.lvl, self.xp, self.coins

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
                        kill = Kill(x_origin, y_origin, self.words_on_screen)
                        killed_points = []
                        pushed_points = []

                        # kill p closest words
                        if event.key == pygame.K_1:
                            killed_points = kill.kill_p_closest(5) #TODO inheret value based on the shop

                        # kill q longest words
                        elif event.key == pygame.K_2:
                            killed_points = kill.kill_q_longest(5) #TODO inheret value based on the shop

                        # angle; max words killed in angle #nlgn hard leetcode problem #1610
                        elif event.key == pygame.K_3:
                            killed_points = kill.kill_in_angle(15) #TODO inheret value based on the shop

                        # freeeeeeeeeeeeze
                        elif event.key == pygame.K_4:
                            last_update_time_new_word += 4000 #TODO inheret value based on the shop
                            last_update_time_render += 4000 #TODO inheret value based on the shop

                        # push-back some closest elements
                        elif event.key == pygame.K_5:
                            pushed_points = kill.kill_p_closest(8)


                        for p in killed_points:
                            del self.words_on_screen[p[-1]]

                        for point in pushed_points:
                            x,y, word = point[1], point[2], point[-1]

                            dx = x - x_origin
                            dy = y - y_origin
                            distance = math.sqrt(dx ** 2 + dy ** 2)
                            kickback_factor = random.uniform(0.05, 0.15)
                            new_distance = distance * (1 + kickback_factor)
                            new_x = x_origin + (dx / distance) * new_distance
                            new_y = y_origin + (dy / distance) * new_distance
                            self.words_on_screen[word] = (new_x, new_y)


                    # display the pressed letter
                    elif ((65 <= event.key <= 90) or (97 <= event.key <= 122)) and not (pygame.key.get_mods() & pygame.KMOD_CTRL):
                        # kick back exactly the size of the letter in case it isnt monospaced
                        char_width, _ = font.size(event.unicode)
                        self.typed_text += event.unicode

                        if self.typed_text in self.words_on_screen:
                            deleted_word = self.typed_text
                            del self.words_on_screen[self.typed_text]

                            rank = word_freqs[deleted_word]
                            a,b = 1,10
                            word_value = (a+((b-a)*(rank-1)/2500))

                            self.xp += word_value
                            self.coins += word_value
                            self.lvl, self.xp = level_definition.determinator(self.lvl, self.xp)
                            self.xp, self.lvl, self.coins = round(self.xp,2), round(self.lvl,2), round(self.coins,2)
                            self.typed_text = ''

                        self.update_text_position()


            # moving points
            curr_time = pygame.time.get_ticks()
            if (curr_time - last_update_time_render) > 10: #this wont change because because its smoothness
                last_update_time_render = curr_time

                _q, new_words_on_screen = point_generator.update_all_points(self.banned_area_game_end, x_origin, y_origin, self.words_on_screen, self.cold_factor)
                if _q: return self.lvl, self.xp, self.coins
                self.words_on_screen = new_words_on_screen


                if (curr_time - last_update_time_new_word) > self.words_spawnrate:
                    last_update_time_new_word = curr_time
                    self.words_on_screen[random_word.get_word(self.word_theme, self.min_word_len, self.max_word_len)] = point_generator.random_point_generator(self.banned_area_game_end, width, height, x_origin, y_origin)

            self.renderer.render_all(self.banned_area_game_end, self.typed_text, self.text_x, self.text_y, self.words_on_screen, self.lvl, self.xp, self.coins)



game = Main() #TODO in shop unlock more of these fuckers
res = game.playing()
print('lvl xp coins')
print(res)

pygame.quit()