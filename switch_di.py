n = int(input())
matrix = [[i for i in input().split()] for j in range(n)]

for r in range(n):
    for c in range(n):
        if r == c:
            matrix[r][c], matrix[r][n-1-r] = matrix[[n-1-r][r]], matrix[r][r]
    print(*matrix[r])
