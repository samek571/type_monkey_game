user_info = [0]*10
def f():
    return True, *user_info[:6], {}
    return True, False, *[None]*4, {}

print(f())