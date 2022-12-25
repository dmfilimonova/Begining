
s = input().split()

result = {}
for w in s:
    if w not in result:
        result[w] = result.get(w, 0) + 1
        print(w, end= ' ')
    else:
        result[w] = result.get(w, 0) + 1
        print(f"{w}_{result[w] - 1}", end= ' ')
