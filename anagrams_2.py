p1, p2 = [list(i.strip('.,!?:;-').lower()) for i in input().split()], [list(i.strip('.,!?:;-').lower()) for i in input().split()]
d1, d2 = {}, {}

for i in p1:
    for j in i:
        d1[j] = p1.count(j)
for i in p2:
    for j in i:
        d2[j] = p1.count(j)
if d1 == d2:
    print("YES")
else:
    print("NO")

