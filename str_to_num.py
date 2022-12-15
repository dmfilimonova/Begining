num = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

l = []
numer = int(input())

while numer >= 1:

    l.append(num[numer % 10])
    numer //= 10


print(*l[::-1])
