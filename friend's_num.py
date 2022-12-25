l, d = [[j for j in input().split()] for i in range(int(input()))], {}

for i in l:
    d.setdefault(i[1].lower(), []).append(i[0])

for i in range(int(input())):
    s = input().lower()

    if s in d:
        print(*d[s])
    if s not in d:
        print("абонент не найден")
