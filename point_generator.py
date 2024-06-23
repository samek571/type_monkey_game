import random
import math
import collections

def move_points(target_x, target_y, current_x, current_y, step_size):
    vector_x = target_x - current_x
    vector_y = target_y - current_y
    distance = math.sqrt(vector_x**2 + vector_y**2)

    vector_x = (vector_x / distance) * step_size
    vector_y = (vector_y / distance) * step_size

    #how shaky it is
    new_x = current_x + vector_x + random.randint(-4, 4)/10
    new_y = current_y + vector_y

    return new_x, new_y


def random_point_generator(radius, width, height, x_origin, y_origin):
    while True:
        angle = random.uniform(-math.pi/4, -3/4*math.pi)
        r = random.uniform(2*radius, 3*radius)
        # lambda_ = 0.1
        # u = random.uniform(0,1)
        # r = -math.log(u) / lambda_
        # r = 2 * radius + (3 * radius - 2 * radius) * (1 - math.exp(-lambda_ * r))  # Scale to the desired range

        x = r * math.cos(angle) + x_origin
        y = r * math.sin(angle) + y_origin

        if 0 <= x <= width and 0 <= y <= height:
            return (x, y)


def update_all_points(safe_distance, x_origin, y_origin, words_on_the_screen, cold_factor):

    moved_points = collections.defaultdict(tuple)
    for txt, val in words_on_the_screen.items():
        i, j = val
        dx, dy = move_points(x_origin, y_origin, i, j, cold_factor)
        moved_points[txt] = (dx, dy)

        if math.sqrt((dx - x_origin) ** 2 + (dy - y_origin) ** 2) < safe_distance:
            return (True, moved_points)

    return (False, moved_points)