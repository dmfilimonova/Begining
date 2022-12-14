n = int(input())

matrix = [[int(i) for i in input().split()] for i in range(n)]
max_ = -1000
for i in range(n):
    for j in range(n):
        if (i >= j and i < n - j - 1) or (i <= j and i > n - j - 1) and matrix[i][j] > max_:
            max_ = matrix[i][j]

print(max_)


