n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
max_ = -1000
for i in range(n):
    for j in range(n):
        if i >= j and i <= n - 1 - j or i <= j and i >= n - 1 - j:
            if max_ < int(matrix[i][j]):
                max_ = int(matrix[i][j])

print(max_)
