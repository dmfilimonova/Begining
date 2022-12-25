s = [word.strip('.,!?:;- ') for word in input().lower().split()]
d, l = {}, []

for word in s:
    d[word] = s.count(word)
for i in d:
    if d[i] == min(d.values()) :
        l.append(i)
        l = sorted(l)
print(l[0])


