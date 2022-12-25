n, d = int(input()), {}

for i in range(n):
    s = input().split()
    a, b, c = s[0], s[1], int(s[2])
    if a not in d:
        d[a] = d.setdefault(a, {b: c})
    else:
        if b not in d[a]:
            d[a].update({b:c})
        else:
            d[a][b] = d[a].get(b) + c

for k in sorted(d):
    print(k)
    for k2, v2 in sorted(d[k].items()):
        print(k2, v2)








