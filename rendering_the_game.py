import pygame
import level_definition

class Render:
    def __init__(self, screen, font, width, x_origin, y_origin):
        self.screen = screen
        self.font = font
        self.width = width
        self.x_origin = x_origin
        self.y_origin = y_origin

    def render_origin_and_bg(self, banned_area_game_end):
        self.screen.fill('gray')
        pygame.draw.circle(self.screen, 'white', (self.x_origin, self.y_origin), banned_area_game_end)
        pygame.draw.circle(self.screen, 'gray', (self.x_origin, self.y_origin), banned_area_game_end - 5)
        pygame.draw.circle(self.screen, 'white', (self.x_origin, self.y_origin), 10)

    def render_all_points(self, words_on_screen):
        for txt, val in words_on_screen.items():
            i, j = val
            pygame.draw.circle(self.screen, 'red', (i, j), 5)
            text_surface = self.font.render(txt, True, (255, 255, 255))
            self.screen.blit(text_surface, (i, j))

    def render_exit_button(self):
        button_width, button_height = 100, 50
        button_x, button_y = self.width - button_width, 0

        pygame.draw.rect(self.screen, (255, 0, 0), (button_x, button_y, button_width, button_height))
        text_surface = self.font.render('Leave', True, 'white')
        self.screen.blit(text_surface, (button_x + 15, button_y + 15))


    # def render_colorful_typed_text(self, words_on_screen, typed_text, text_x, text_y):
    #     red = (255, 0, 0)
    #     green = (0, 255, 0)
    #
    #     if typed_text:
    #         matches_prefix = any(word.startswith(typed_text) for word in words_on_screen)
    #
    #         typed_text_color = green if matches_prefix else red
    #
    #         typed_text_surface = self.font.render(typed_text, True, typed_text_color)
    #         self.screen.blit(typed_text_surface, (text_x, text_y + 5))
    #
    #         for word, (i, j) in words_on_screen.items():
    #             for idx, char in enumerate(word):
    #                 if idx < len(typed_text):
    #                     char_color = green if char == typed_text[idx] else red
    #                     char_surface = self.font.render(char, True, char_color)
    #                     self.screen.blit(char_surface, (i, j))
    #
    #                 char_width, _ = self.font.size(char)
    #                 i += char_width
    #
    #     pygame.display.flip()

    def render_colorful_typed_text(self, words_on_screen, typed_text, text_x, text_y):
        color = (255, 0, 0)
        prefixes = []
        for word, val in words_on_screen.items():
            i, j = val
            if word.startswith(typed_text):
                prefixes.append([word, i, j, len(typed_text)])

        if prefixes:
            color = (0, 255, 0)

        typed_text_surface = self.font.render(typed_text, True, color)
        self.screen.blit(typed_text_surface, (text_x, text_y + 5))

        for word, i, j, l in prefixes:
            word_surface = self.font.render(word[:l], True, color)
            self.screen.blit(word_surface, (i, j))
        pygame.display.flip()

    def render_top(self, lvl, xp, coins, time, abillity_render):
        xp_bar_start = (2, 50)
        xp_bar_end = (self.width - 2, 50)
        xp_bar_height = 7

        # xp bar outline
        pygame.draw.rect(self.screen, 'black', (0, 50, self.width, 2))
        pygame.draw.rect(self.screen, 'black', (0, 50 + xp_bar_height, self.width, 2))
        pygame.draw.rect(self.screen, 'black', (0, xp_bar_start[-1], xp_bar_start[0], xp_bar_height))
        pygame.draw.rect(self.screen, 'black', (xp_bar_end[0], xp_bar_end[-1], self.width, xp_bar_height))
        # determine xp proportional to level up
        percentage_full_xp_bar = level_definition.get_xp(lvl)
        current_percentage = xp / percentage_full_xp_bar
        xp_bar_filled = (xp_bar_end[0] - xp_bar_start[0]) * current_percentage
        # do the thing
        pygame.draw.rect(self.screen, 'blue', (xp_bar_start[0], xp_bar_start[1], xp_bar_filled, xp_bar_height))


        level_text = self.font.render(f"Lvl: {lvl}", True, (255, 255, 255))
        xp_text = self.font.render(f"Xp: {xp}", True, (255, 255, 255))
        coins_text = self.font.render(f"Coins: {coins}", True, (255, 255, 255))
        time_txt = self.font.render(f"Time: {time}", True, (255, 255, 255))

        safe_buffer = 50
        level_text_size_x, _ = level_text.get_size()
        xp_text_size_x, _ = xp_text.get_size()

        self.screen.blit(level_text, (10 + 0 * safe_buffer, 10))
        self.screen.blit(xp_text, (10 + 1 * safe_buffer + level_text_size_x, 10))
        self.screen.blit(coins_text, (10 + 2 * safe_buffer + level_text_size_x + xp_text_size_x, 10))
        self.screen.blit(time_txt, (self.width-5*safe_buffer, 10))

        n=len(abillity_render)
        for i in range(n-1,-1,-1):
            tmp = self.font.render(str(n-i), True, (155, 155, 155))
            if abillity_render[n-i-1]:
                tmp = self.font.render(str(n-i), True, (255, 255, 255))

            self.screen.blit(tmp, (self.width-(9+i)*safe_buffer, 10))


    def render_all(self, banned_area_game_end, typed_text, text_x, text_y, words_on_screen, lvl, xp, coins, time, abillity_render):
        self.render_origin_and_bg(banned_area_game_end)
        self.render_exit_button()
        self.render_top(lvl, xp, coins, time, abillity_render)
        self.render_all_points(words_on_screen)
        self.render_colorful_typed_text(words_on_screen, typed_text, text_x, text_y)
        pygame.display.flip()

