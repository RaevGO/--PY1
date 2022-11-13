import random

def get_random_password(n = 8) -> str:
    list_ = ''.join([chr(i) for i in range(ord('A'), ord('Z') + 1)]
                    + [chr(i) for i in range(ord('a'), ord('z') + 1)]
                    + [str(x) for x in range(0, 10)])
    return ''.join(random.sample(list_, 8))


print(get_random_password())