n = int(input())
m = int(input())
matrix = [[int(c) for c in input().split()] for r in range(n)]
max_ = -1000
q = []
for r in range(n):
    for c in range(m):
        if matrix[r][c] > max_:
            max_ = matrix[r][c]
            q = []
            q.append(r)
            q.append(c)


print(*q)

