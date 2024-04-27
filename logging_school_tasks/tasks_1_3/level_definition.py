import collections
import random
import math

# def xp_req(q,k,p):
#     arr = []
#     for x in range(64):
#         arr.append(math.ceil(q*x**k+p))
#     return arr

# #function that determines the levels
# lvl = 0
# xp_to_levels=collections.defaultdict(int)
# for xp in xp_req(20, 1.51, 15):
#     xp_to_levels[lvl] = xp
#     lvl+=1
#
# print(xp_to_levels)


xp_map = {0: 15, 1: 35, 2: 72, 3: 121, 4: 178, 5: 243, 6: 315, 7: 393, 8: 478, 9: 567, 10: 663, 11: 763,
          12: 868, 13: 977, 14: 1091, 15: 1209, 16: 1331, 17: 1458, 18: 1588, 19: 1721, 20: 1859, 21: 2000,
          22: 2144, 23: 2292, 24: 2443, 25: 2597, 26: 2755, 27: 2915, 28: 3079, 29: 3246, 30: 3416, 31: 3588,
          32: 3764, 33: 3942, 34: 4123, 35: 4307, 36: 4493, 37: 4682, 38: 4874, 39: 5068, 40: 5265, 41: 5465,
          42: 5667, 43: 5871, 44: 6078, 45: 6287, 46: 6499, 47: 6713, 48: 6929, 49: 7148, 50: 7369, 51: 7592,
          52: 7817, 53: 8045, 54: 8275, 55: 8507, 56: 8741, 57: 8977, 58: 9216, 59: 9456, 60: 9699, 61: 9944,
          62: 10191, 63: 10439}

def get_xp(lvl):
    return xp_map[lvl]

def determinator(lvl, xp):
    global xp_map
    while xp_map[lvl] < xp:
        lvl, xp = lvl+1, float(str(round(xp-xp_map[lvl], 2)))

    return lvl, xp

# def decomposer_to_xp(lvl, xp):
#     global xp_map #TODO mistake ?

