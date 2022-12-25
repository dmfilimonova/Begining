s = [[j for j in input().split(': ')] for i in range(int(input()))]
d, l = {}, []
for i in s:
    d[i[0].lower()] = i[1]

l = [[i.lower() for i in input().split()] for j in range(int(input()))]
print(d)
for i in l:
    for j in i:
        if j in d:
            print(d[j])
        else:
            print("Не найдено")

