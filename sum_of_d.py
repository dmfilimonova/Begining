n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
sum_1, sum_2, sum_3, sum_4 = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if i < j and i < n - j - 1:
            sum_1 += matrix[i][j]
        if i < j and i > n - j - 1:
            sum_2 += matrix[i][j]
        if i > j and i > n - j - 1:
            sum_3 += matrix[i][j]
        if i > j and i < n - j - 1:
            sum_4 += matrix[i][j]

print(f"Верхняя четверть: {sum_1}")
print(f"Правая четверть: {sum_2}")
print(f"Нижняя четверть: {sum_3}")
print(f"Левая четверть: {sum_4}")
