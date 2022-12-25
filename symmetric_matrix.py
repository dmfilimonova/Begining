n = int(input())

matrix = [[i for i in input().split()] for j in range(n)]
flag = 'YES'
for r in range(n):
    for c in range(n):
        if matrix[r][c] == matrix[c][r]:
            flag = flag
        if matrix[r][c] != matrix[c][r]:
            flag = 'NO'

print(flag)

