import random
import math
import collections
import random_word

def move_points(target_x, target_y, current_x, current_y, step_size):
    vector_x = target_x - current_x
    vector_y = target_y - current_y
    distance = math.sqrt(vector_x**2 + vector_y**2)

    vector_x = (vector_x / distance) * step_size
    vector_y = (vector_y / distance) * step_size

    new_x = current_x + vector_x + random.randint(-10, 10)
    new_y = current_y + vector_y

    return new_x, new_y


def random_point_generator(words:dict, radius, width, x_origin, y_origin):
    # banned_area = set()
    # for val in words.values():
    #     banned_area.add((val[0], val[1]))

    while True:
        #could be improved to not be just rectangle but rather circle of some kind
        x = random.randint(10, width-10)
        y = random.randint(60, 85)

        #safe distance from origin
        # distance_from_origin = math.sqrt((x - x_origin) ** 2 + (y - y_origin) ** 2)
        # if 20/10*distance_from_origin < radius:
        return (x,y)



def update_all_points(safe_distance, width, x_origin, y_origin, words_on_the_screen, word_theme):

    new_txt = collections.defaultdict(tuple)
    for txt, val in words_on_the_screen.items():
        i, j = val
        dx, dy = move_points(x_origin, y_origin, i, j, 20)
        new_txt[txt] = (dx, dy)

        if math.sqrt((dx - x_origin) ** 2 + (dy - y_origin) ** 2) < safe_distance:
            return (True, new_txt)

    #TODO no overlap of the points
    new_txt[random_word.get_word(word_theme, 3, 8)] = random_point_generator(words_on_the_screen, safe_distance, width, x_origin, y_origin)

    return (False, new_txt)