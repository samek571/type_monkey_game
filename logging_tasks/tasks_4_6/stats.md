```sh
samuel@finkbuk:~/Documents/_uni/2/nastroje/6logging/type_monkey_game-main$ python3 -m memory_profiler game_with_monitoring.py
pygame 2.5.2 (SDL 2.28.2, Python 3.10.12)
Hello from the pygame community. https://www.pygame.org/contribute.html
Enter your username: asd
Enter your password: asd
No user found with that name. Do you want to add a new user? (yes/no):
New user added and logged in.
Welcome back, asd! Login successful.
Filename: game_with_monitoring.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    90    210.9 MiB    210.9 MiB           1       @profile
    91                                             def playing(self):
    92    210.9 MiB      0.0 MiB           1           screen_width, screen_height = self.screen.get_size()
    93    210.9 MiB      0.0 MiB           1           button_width, button_height = screen_width * 0.1, screen_height * 0.1
    94    210.9 MiB      0.0 MiB           1           button_x, button_y = screen_width - button_width - 10, 10
    95
    96    210.9 MiB      0.0 MiB           1           last_update_time_new_word = pygame.time.get_ticks()
    97    210.9 MiB      0.0 MiB           1           last_update_time_render = pygame.time.get_ticks()
    98    210.9 MiB      0.0 MiB           1           time_to_boot = pygame.time.get_ticks()
    99
   100    211.7 MiB    -12.8 MiB       24942           while True:
   101    211.7 MiB    -12.8 MiB       24942               curr_time = pygame.time.get_ticks()
   102    211.7 MiB    -12.8 MiB       24942               time_age = round((curr_time- time_to_boot)/1000, 2)
   103
   104    211.7 MiB    -13.1 MiB       25598               for event in pygame.event.get():
   105
   106                                                         # esc / check if mouse has been pressed - for safe exit
   107    211.7 MiB     -0.3 MiB         657                   if event.type == pygame.MOUSEBUTTONDOWN:
   108    211.7 MiB      0.0 MiB           2                       mouse_x, mouse_y = event.pos
   109    211.7 MiB      0.0 MiB           2                       if (button_x <= mouse_x <= button_x + button_width) and (
   110                                                                     button_y <= mouse_y <= button_y + button_height):
   111                                                                 return self.lvl, self.xp, self.coins, time_age
   112
   113
   114                                                         # if something has been pressed on the keyboard
   115    211.7 MiB     -0.3 MiB         655                   elif event.type == pygame.KEYDOWN:
   116    211.7 MiB     -0.1 MiB         132                       if event.key == pygame.K_ESCAPE: # different pullout methode - no need to use mouse to stop playing
   117    211.6 MiB     -0.0 MiB           1                           return self.lvl, self.xp, self.coins, time_age
   118
   119    211.7 MiB     -0.1 MiB         131                       elif (pygame.key.get_mods() & pygame.KMOD_CTRL) and (
   120                                                                     event.key == pygame.K_BACKSPACE or event.key == pygame.K_a):
   121                                                                 self.typed_text = ''
   122                                                                 self.update_text_position()
   123
   124    211.7 MiB     -0.1 MiB         131                       elif event.key == pygame.K_BACKSPACE:
   125    211.7 MiB     -0.0 MiB          17                           self.typed_text = self.typed_text[:-1]
   126    211.7 MiB     -0.0 MiB          17                           self.update_text_position()
   127
   128                                                             # submission of a word, check if word is in the game
   129    211.7 MiB     -0.1 MiB         131                       if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
   130                                                                 self.typed_text = ''
   131                                                                 self.update_text_position()
   132
   133
   134                                                             # Abilities
   135    211.7 MiB     -0.1 MiB         131                       elif event.key in {pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5}: #TODO abillity to bind this shit
   136    211.7 MiB      0.0 MiB           2                           kill = Kill(self.x_origin, self.y_origin, self.words_on_screen)
   137    211.7 MiB      0.0 MiB           2                           killed_points = []
   138    211.7 MiB      0.0 MiB           2                           pushed_points = []
   139
   140                                                                 # kill p closest words
   141    211.7 MiB      0.0 MiB           2                           if event.key == pygame.K_1:
   142                                                                     if (curr_time - self.last_time_used_abillity[0]) > self.abillity_cooldown[0]:
   143                                                                         self.last_time_used_abillity[0] = curr_time
   144                                                                         killed_points = kill.kill_p_closest(self.abillity_strength[0]) #TODO inheret value based on the shop
   145
   146                                                                 # kill some longest words
   147    211.7 MiB      0.0 MiB           2                           elif event.key == pygame.K_2:
   148    211.7 MiB      0.0 MiB           1                               if (curr_time - self.last_time_used_abillity[1]) > self.abillity_cooldown[1]:
   149    211.7 MiB      0.0 MiB           1                                   self.last_time_used_abillity[1] = curr_time
   150    211.7 MiB      0.0 MiB           1                                   killed_points = kill.kill_q_longest(self.abillity_strength[1]) #TODO inherent value based on the shop
   151
   152                                                                 # kill as much as possible in certain angle; max words killed in angle #nlgn hard leetcode problem #1610
   153    211.7 MiB      0.0 MiB           1                           elif event.key == pygame.K_3:
   154                                                                     if (curr_time - self.last_time_used_abillity[2]) > self.abillity_cooldown[2]:
   155                                                                         self.last_time_used_abillity[2] = curr_time
   156                                                                         killed_points = kill.kill_in_angle(self.abillity_strength[2]) #TODO inheret value based on the shop
   157
   158                                                                 # stop production for certain time
   159    211.7 MiB      0.0 MiB           1                           elif event.key == pygame.K_4:
   160                                                                     if (curr_time - self.last_time_used_abillity[3]) > self.abillity_cooldown[3]:
   161                                                                         self.last_time_used_abillity[3] = curr_time
   162                                                                         last_update_time_new_word += self.abillity_strength[3] #TODO inheret value based on the shop
   163
   164                                                                 # push-back some closest elements
   165    211.7 MiB      0.0 MiB           1                           elif event.key == pygame.K_5:
   166    211.7 MiB      0.0 MiB           1                               if (curr_time - self.last_time_used_abillity[4]) > self.abillity_cooldown[4]:
   167    211.7 MiB      0.0 MiB           1                                   self.last_time_used_abillity[4] = curr_time
   168    211.7 MiB      0.0 MiB           1                                   pushed_points = kill.kill_p_closest(self.abillity_strength[4])
   169
   170
   171    211.7 MiB      0.0 MiB           6                           for p in killed_points:
   172    211.7 MiB      0.0 MiB           4                               del self.words_on_screen[p[-1]]
   173
   174    211.7 MiB      0.0 MiB           6                           for point in pushed_points:
   175    211.7 MiB      0.0 MiB           4                               x,y, word = point[1], point[2], point[-1]
   176
   177    211.7 MiB      0.0 MiB           4                               dx = x - self.x_origin
   178    211.7 MiB      0.0 MiB           4                               dy = y - self.y_origin
   179    211.7 MiB      0.0 MiB           4                               distance = math.sqrt(dx ** 2 + dy ** 2)
   180    211.7 MiB      0.0 MiB           4                               kickback_factor = random.uniform(0.05, 0.15)
   181    211.7 MiB      0.0 MiB           4                               new_distance = distance * (1 + kickback_factor)
   182    211.7 MiB      0.0 MiB           4                               new_x = self.x_origin + (dx / distance) * new_distance
   183    211.7 MiB      0.0 MiB           4                               new_y = self.y_origin + (dy / distance) * new_distance
   184    211.7 MiB      0.0 MiB           4                               self.words_on_screen[word] = (new_x, new_y)
   185
   186
   187                                                             # display the pressed letter
   188    211.7 MiB     -0.1 MiB         129                       elif ((65 <= event.key <= 90) or (97 <= event.key <= 122)) and not (pygame.key.get_mods() & pygame.KMOD_CTRL):
   189                                                                 # kick back exactly the size of the letter in case it isnt monospaced
   190    211.7 MiB     -0.1 MiB         110                           char_width, _ = self.font.size(event.unicode)
   191    211.7 MiB     -0.1 MiB         110                           self.typed_text += event.unicode
   192
   193    211.7 MiB     -0.1 MiB         110                           if self.typed_text in self.words_on_screen:
   194    211.7 MiB     -0.0 MiB          21                               deleted_word = self.typed_text
   195    211.7 MiB     -0.0 MiB          21                               del self.words_on_screen[self.typed_text]
   196
   197    211.7 MiB     -0.0 MiB          21                               rank = self.word_freqs[deleted_word]
   198    211.7 MiB     -0.0 MiB          21                               a,b = 1,10
   199    211.7 MiB     -0.0 MiB          21                               word_value = (a+((b-a)*(rank-1)/2500))
   200
   201    211.7 MiB     -0.0 MiB          21                               self.xp += word_value
   202    211.7 MiB     -0.0 MiB          21                               self.coins += word_value
   203    211.7 MiB     -0.0 MiB          21                               self.lvl, self.xp = level_definition.determinator(self.lvl, self.xp)
   204    211.7 MiB     -0.0 MiB          21                               self.xp, self.lvl, self.coins = round(self.xp,2), round(self.lvl,2), round(self.coins,2)
   205    211.7 MiB     -0.0 MiB          21                               self.typed_text = ''
   206
   207    211.7 MiB     -0.1 MiB         110                           self.update_text_position()
   208
   209                                                     # rendering and shit
   210    211.7 MiB    -12.8 MiB       24941               abillity_render = [False] * len(self.abillity_cooldown)
   211    211.7 MiB    -12.8 MiB       24941               if (curr_time - last_update_time_render) > 40: #this is a constant and wont change
   212    211.7 MiB     -0.1 MiB         148                   last_update_time_render = curr_time
   213
   214    211.7 MiB     -0.1 MiB         148                   _q, new_words_on_screen = point_generator.update_all_points(self.banned_area_game_end, self.x_origin, self.y_origin, self.words_on_screen, self.cold_factor)
   215    211.7 MiB     -0.1 MiB         148                   if _q: return self.lvl, self.xp, self.coins, time_age
   216    211.7 MiB     -0.1 MiB         148                   self.words_on_screen = new_words_on_screen
   217
   218
   219    211.7 MiB     -0.1 MiB         148                   if (curr_time - last_update_time_new_word) > self.words_spawnrate:
   220    211.7 MiB     -0.0 MiB          30                       last_update_time_new_word = curr_time
   221    211.7 MiB     -0.0 MiB          30                       self.words_on_screen[random_word.get_word(self.word_theme, self.min_word_len, self.max_word_len)] = point_generator.random_point_generator(self.banned_area_game_end, self.width, self.height, self.x_origin, self.y_origin)
   222
   223
   224    211.7 MiB     -0.4 MiB         888                   for i in range(len(self.abillity_cooldown)):
   225    211.7 MiB     -0.4 MiB         740                       if (curr_time - self.last_time_used_abillity[i]) > self.abillity_cooldown[i]:
   226    211.7 MiB     -0.4 MiB         524                           abillity_render[i] = True
   227
   228    211.7 MiB      0.7 MiB         148                   self.renderer.render_all(self.banned_area_game_end, self.typed_text, self.text_x, self.text_y, self.words_on_screen, self.lvl, self.xp, self.coins, time_age, abillity_render)



lvl xp coins time
2 3.85 53.85 65.96

Do you want to play again or log out? (play/log out): log out
samuel@finkbuk:~/Documents/_uni/2/nastroje/6logging/type_monkey_game-main$
```
