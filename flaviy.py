n = int(input())
k = int(input())

cheel = 0

for i in range(1, n):
    cheel = (cheel + k) % i

print(cheel + 1)
