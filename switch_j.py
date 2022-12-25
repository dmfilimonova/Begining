n, m = int(input()), int(input())

matrix = [[c for c in input().split()] for r in range(n)]
i_j = input().split()
i, j = int(i_j[0]), int(i_j[1])

for r in range(n):
    for c in range(m):
        if j > i:
            if c == j:
                matrix[r][j], matrix[r][i] = matrix[r][i], matrix[r][j]
        if i > j:
            if c == i:
                matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
    print(matrix[r])



