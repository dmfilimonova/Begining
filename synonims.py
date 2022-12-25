l, d = [[j for j in input().split()] for i in range(int(input()))], {}

for i in l:
    d[i[1]] = i[0]
    d[i[0]] = i[1]


print(d[input()])


