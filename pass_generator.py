from random import *
from string import *

LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))

def generate_password(length):
    s = []
    while len(s) != length:
        s.append(choice(LETTER))
    return s


def generate_passwords(count, length):
    l = []
    for i in range(count):
        l.append(generate_password(length))
    return ''.join(l)


n, m = int(input()), int(input())


print(*generate_passwords(n, m))