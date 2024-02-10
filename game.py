import collections
import random

import pygame
import math

#my files that are used just os it doesnt look ugly
import level_definition
import point_generator
import random_word
from killer_functions import Kill


#making sure it defo downloads the dependencies into the same directory as we play in
import nltk
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
nltk_data_directory = os.path.join(current_directory, 'nltk_data')
nltk.data.path.append(nltk_data_directory)
nltk.download('brown', download_dir=nltk_data_directory)


pygame.init()
pygame.display.set_caption("Type monkey")

dimension = 1000
width, height = math.floor(1.618 * dimension), dimension
screen = pygame.display.set_mode((width, height))
x_origin, y_origin = width // 2, height
font = pygame.font.Font(None, 36)


class Main:
    def __init__(self, xp, coins, safe_distance, word_theme):
        self.xp = xp
        self.coins = coins
        self.lvl, self.xp = level_definition.determinator(0, self.xp)
        self.safe_distance = safe_distance
        self.word_theme = word_theme

        self.typed_text = ''
        self.words_on_the_screen = collections.defaultdict(tuple)
        self.text_x, self.text_y = width // 2, 10
        self.words_on_the_screen[random_word.get_word(word_theme, 3, 8)] = (point_generator.random_point_generator(self.words_on_the_screen, safe_distance, width, x_origin, y_origin))

        self.renderer = self.Render()

    def update_text_position(self, font, width):
        total_text_width, _ = font.size(self.typed_text)
        self.text_x = (width - total_text_width) // 2

    class Render:
        def render_origin_and_bg(self, screen, safe_distance, x_origin, y_origin):
            screen.fill('gray')
            pygame.draw.circle(screen, 'white', (x_origin, y_origin), safe_distance)
            pygame.draw.circle(screen, 'gray', (x_origin, y_origin), safe_distance - 5)
            pygame.draw.circle(screen, 'white', (x_origin, y_origin), 10)

        def render_all_points(self, screen, font, words_on_the_screen):
            for txt, val in words_on_the_screen.items():
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

        def render_colorful_typed_text(self, screen, words_on_the_screen, typed_text, text_x, text_y):
            color = (255, 0, 0)
            prefixes = []
            for word, val in words_on_the_screen.items():
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


        def render_all(self, screen, safe_distance, x_origin, y_origin, font, typed_text, text_x, text_y,
                       words_on_the_screen, lvl, xp, coins):
            self.render_origin_and_bg(screen, safe_distance, x_origin, y_origin)
            self.render_exit_button(screen, font)
            self.render_xp_bar_and_coins(screen, lvl, xp, coins)
            self.render_all_points(screen, font, words_on_the_screen)
            self.render_colorful_typed_text(screen, words_on_the_screen, typed_text, text_x, text_y)
            pygame.display.flip()

    def playing(self):
        last_update_time_new_word = pygame.time.get_ticks()

        screen_width, screen_height = screen.get_size()
        button_width, button_height = screen_width * 0.1, screen_height * 0.1
        button_x, button_y = screen_width - button_width - 10, 10

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
                        if self.typed_text in self.words_on_the_screen:
                            del self.words_on_the_screen[self.typed_text]
                            self.xp += new_xp
                            self.coins += new_coins
                            self.lvl, self.xp = level_definition.xp_map(self.lvl, self.xp)

                        self.typed_text = ''
                        self.update_text_position(font, width)

                    # Abilities
                    elif event.key in {pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4}:
                        kill = Kill(x_origin, y_origin, self.words_on_the_screen)
                        killed_points = []

                        # p; p closest words
                        if event.key == pygame.K_1:
                            killed_points = kill.kill_p_closest(5)

                        # q; q longest words
                        elif event.key == pygame.K_2:
                            killed_points = kill.kill_q_longest(5)

                        # angle; max words killed in angle #nlgn hard leetcode problem #1610
                        elif event.key == pygame.K_3:
                            killed_points = kill.kill_in_angle(15)

                        # freeeeeeeeeeeeze
                        elif event.key == pygame.K_4:
                            last_update_time_new_word += 4000

                        for p in killed_points:
                            del self.words_on_the_screen[p[-1]]

                    # display the pressed letter
                    elif (65 <= event.key <= 90) or (97 <= event.key <= 122):
                        # kick back exactly the size of the letter in case it isnt monospaced
                        char_width, _ = font.size(event.unicode)
                        self.typed_text += event.unicode

                        # instead of space confirmation
                        if self.typed_text in self.words_on_the_screen:
                            del self.words_on_the_screen[self.typed_text]
                            self.typed_text = ''
                            self.xp += new_xp
                            self.coins += new_coins
                            self.lvl, self.xp = level_definition.determinator(self.lvl, self.xp)

                        self.update_text_position(font, width)

            # moving points
            current_time = pygame.time.get_ticks()
            if current_time - last_update_time_new_word >= 900:
                _q, new_txt = point_generator.update_all_points(self.safe_distance, width, x_origin, y_origin, self.words_on_the_screen, self.word_theme)
                if _q:
                    return self.lvl, self.xp, self.coins
                else:
                    self.words_on_the_screen = new_txt
                    last_update_time_new_word = current_time

            # render
            self.renderer.render_all(screen, self.safe_distance, x_origin, y_origin, font, self.typed_text, self.text_x, self.text_y, self.words_on_the_screen, self.lvl, self.xp, self.coins)


game = Main(0, 0, 500, ['lore', 'news'])
res = game.playing()
print('lvl xp coins')
print(res)

pygame.quit()