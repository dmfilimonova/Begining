n = int(input())

table = [[i for i in input().split()] for j in range(n)]

for i in range(len(table)):
    print(*table[i])

print()

for i in range(len(table)):
    if table[i][1] == '4' or table[i][1] == '5':
        print(*table[i])




