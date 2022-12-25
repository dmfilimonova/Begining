w1 = list(input())
w2 = list(input())
d1 = {}
d2 = {}

for i in w1:
    for j in w2:
        d1[i] = w1.count(i)
        d2[j] = w2.count(j)
if d1 == d2:
    print("YES")
else:
    print("NO")