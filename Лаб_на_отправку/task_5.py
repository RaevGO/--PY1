import random
import string

def get_random_password(n = 8) -> str:
    list_ = string.ascii_letters + string.digits
    return ''.join(random.sample(list_, 8))


print(get_random_password())
