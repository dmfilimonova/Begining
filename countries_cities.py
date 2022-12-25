l, d = [[j for j in input().split()] for i in range(int(input()))], {}

for i in l:
    d[i[0]] = i[1:]

for j in range(int(input())):
    for j in d:
        if input() in d[j]:
            print(j)