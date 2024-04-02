import collections
import random
import math

#my files that are used just os it doesnt look ugly
import level_definition
import point_generator
import random_word
from killer_functions import Kill


#making sure it defo downloads the dependencies into the same directory as we play in
import nltk
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
        self.words_on_screen[random_word.get_word(self.word_theme, 3, 8)] = (point_generator.random_point_generator(self.words_on_screen, self.banned_area_game_end, width, x_origin, y_origin))

        self.renderer = self.Render()


    def update_text_position(self, font, width):
        total_text_width, _ = font.size(self.typed_text)
        self.text_x = (width - total_text_width) // 2

    class Render:
        def render_origin_and_bg(self, screen, banned_area_game_end, x_origin, y_origin):
            screen.fill('gray')
            pygame.draw.circle(screen, 'white', (x_origin, y_origin), banned_area_game_end)
            pygame.draw.circle(screen, 'gray', (x_origin, y_origin), banned_area_game_end - 5)
            pygame.draw.circle(screen, 'white', (x_origin, y_origin), 10)

        def render_all_points(self, screen, font, words_on_screen):
            for txt, val in words_on_screen.items():
                i, j = val
                pygame.draw.circle(screen, 'red', (i, j), 5)
                text_surface = font.render(txt, True, (255, 255, 255))
                screen.blit(text_surface, (i, j))

        def render_exit_button(self, screen, font):
            button_width, button_height = 100, 50
            button_x, button_y = width - button_width, 0

            pygame.draw.rect(screen, (255, 0, 0), (button_x, button_y, button_width, button_height))
            text_surface = font.render('Leave', True, 'white')
            screen.blit(text_surface, (button_x + 15, button_y + 15))

        def render_colorful_typed_text(self, screen, words_on_screen, typed_text, text_x, text_y):
            color = (255, 0, 0)
            prefixes = []
            for word, val in words_on_screen.items():
                i, j = val
                if word.startswith(typed_text):
                    prefixes.append([word, i, j, len(typed_text)])

            if prefixes:
                color = (0, 255, 0)

            typed_text_surface = font.render(typed_text, True, color)
            screen.blit(typed_text_surface, (text_x, text_y + 5))

            for word, i, j, l in prefixes:
                word_surface = font.render(word[:l], True, color)
                screen.blit(word_surface, (i, j))
            pygame.display.flip()

        def render_xp_bar_and_coins(self, screen, lvl, xp, coins):
            xp_bar_start = (2, 50)
            xp_bar_end = (width - 2, 50)
            xp_bar_height = 7

            # outline
            pygame.draw.rect(screen, 'black', (0, 50, width, 2))
            pygame.draw.rect(screen, 'black', (0, 50 + xp_bar_height, width, 2))
            pygame.draw.rect(screen, 'black', (0, xp_bar_start[-1], xp_bar_start[0], xp_bar_height))
            pygame.draw.rect(screen, 'black', (xp_bar_end[0], xp_bar_end[-1], width, xp_bar_height))

            # determine xp proportional to level up
            percentage_full_xp_bar = level_definition.get_xp(lvl)
            current_percentage = xp / percentage_full_xp_bar
            xp_bar_filled = (xp_bar_end[0] - xp_bar_start[0]) * current_percentage
            # do the thing
            pygame.draw.rect(screen, 'blue', (xp_bar_start[0], xp_bar_start[1], xp_bar_filled, xp_bar_height))

            font = pygame.font.Font(None, 36)
            level_text = font.render(f"Lvl: {lvl}", True, (255, 255, 255))
            xp_text = font.render(f"Xp: {xp}", True, (255, 255, 255))
            coins_text = font.render(f"Coins: {coins}", True, (255, 255, 255))

            safe_buffer = 50
            level_text_size_x, _ = level_text.get_size()
            xp_text_size_x, _ = xp_text.get_size()

            screen.blit(level_text, (10 + 0 * safe_buffer, 10))
            screen.blit(xp_text, (10 + 1 * safe_buffer + level_text_size_x, 10))
            screen.blit(coins_text, (10 + 2 * safe_buffer + level_text_size_x + xp_text_size_x, 10))


        def render_all(self, screen, banned_area_game_end, x_origin, y_origin, font, typed_text, text_x, text_y,
                       words_on_screen, lvl, xp, coins):
            self.render_origin_and_bg(screen, banned_area_game_end, x_origin, y_origin)
            self.render_exit_button(screen, font)
            self.render_xp_bar_and_coins(screen, lvl, xp, coins)
            self.render_all_points(screen, font, words_on_screen)
            self.render_colorful_typed_text(screen, words_on_screen, typed_text, text_x, text_y)
            pygame.display.flip()

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

                    new_xp, new_coins = random.randint(3,8), random.randint(3,8)
                    # typed letters/ word is a mistake
                    if event.key == pygame.K_BACKSPACE:
                        # ctrl god mode - I am always pissed if that doesnt work and this is will NOT be the case
                        if pygame.key.get_mods() & pygame.KMOD_CTRL:
                            self.typed_text = ''
                        else:
                            self.typed_text = self.typed_text[:-1]
                        self.update_text_position(font, width)

                    # submission of a word, check if word is in the game
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        if self.typed_text in self.words_on_screen:
                            del self.words_on_screen[self.typed_text]
                            self.xp += new_xp
                            self.coins += new_coins
                            self.lvl, self.xp = level_definition.xp_map(self.lvl, self.xp)

                        self.typed_text = ''
                        self.update_text_position(font, width)

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

                        kickback_constant = random.uniform(40, 50)
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
                    elif (65 <= event.key <= 90) or (97 <= event.key <= 122):
                        # kick back exactly the size of the letter in case it isnt monospaced
                        char_width, _ = font.size(event.unicode)
                        self.typed_text += event.unicode

                        # instead of space confirmation
                        if self.typed_text in self.words_on_screen:
                            del self.words_on_screen[self.typed_text]
                            self.typed_text = ''
                            self.xp += new_xp
                            self.coins += new_coins
                            self.lvl, self.xp = level_definition.determinator(self.lvl, self.xp)

                        self.update_text_position(font, width)


            # moving points
            curr_time = pygame.time.get_ticks()
            if (curr_time - last_update_time_render) > 10:
                last_update_time_render = curr_time

                _q, new_words_on_screen = point_generator.update_all_points(self.banned_area_game_end, x_origin, y_origin, self.words_on_screen, self.cold_factor)
                if _q: return self.lvl, self.xp, self.coins
                self.words_on_screen = new_words_on_screen


                if (curr_time - last_update_time_new_word) > self.words_spawnrate:
                    self.words_on_screen[random_word.get_word(self.word_theme, self.min_word_len, self.max_word_len)] = point_generator.random_point_generator(self.words_on_screen, self.banned_area_game_end, width, x_origin, y_origin)
                    last_update_time_new_word = curr_time

            self.renderer.render_all(screen, self.banned_area_game_end, x_origin, y_origin, font, self.typed_text, self.text_x, self.text_y, self.words_on_screen, self.lvl, self.xp, self.coins)



game = Main() #TODO in shop unlock more of these fuckers
res = game.playing()
print('lvl xp coins')
print(res)

pygame.quit()