n, m = int(input()), int(input())

mult = [[int(r * c) for r in range(m)] for c in range(n)]

for i in range(len(mult)):
    print(*mult[i], end= '\n')


