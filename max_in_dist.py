n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
max_ = 0
for i in range(n):
    for j in range(n):
        if i >= j and max_ < matrix[i][j]:
            max_ = matrix[i][j]

print(max_)




