import math
import collections

class Kill:
    def __init__(self, x, y, words_on_the_screen):
        self.x = x
        self.y = y
        self.words = words_on_the_screen
    def kill_q_longest(self, q):
        tmp = [key for key in self.words.keys()]
        tmp.sort(reverse=True)

        return [[word] for word in tmp][:q]

    def kill_p_closest(self, p):
        all = []

        for txt, val in self.words.items():
            i, j = val
            tmp = math.sqrt((self.x - i) ** 2 + (self.y - j) ** 2)
            all.append([tmp, i, j, txt])

        all.sort()
        return all[:p]


    def kill_in_angle(self, angle):
        # preprocess
        points = [[val[0], val[1], txt] for txt, val in self.words.items()]

        def angle_from_location(p):
            dy, dx = p[0] - self.x, p[1] - self.y
            return math.degrees(math.atan2(dy, dx))

        same_location_points = []
        angles = []
        point_map = collections.defaultdict(list)
        for p in points:
            if p[:2] == [self.x, self.y]:
                same_location_points.append(p)
            else:
                angle_p = angle_from_location(p[:2])
                angles.append(angle_p)
                point_map[angle_p].append(p)

        # wrapping so 15 and 355 gets popped if view is 45
        angles.sort()
        angles += [a + 360 for a in angles]

        max_points = 0
        max_points_list = []
        current_points_list = []
        left = 0
        for right in range(len(angles)):
            current_angle = angles[right]
            while current_angle - angles[left] > angle:
                for p in point_map[angles[left]]:
                    current_points_list.remove(p)
                left += 1
            for p in point_map[current_angle]:
                current_points_list.append(p)
            if len(current_points_list) > max_points:
                max_points = len(current_points_list)
                max_points_list = current_points_list.copy()

        return same_location_points + max_points_list

