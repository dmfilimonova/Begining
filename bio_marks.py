
s1 = set([int(i) for i in input().split()])
s2 = set([int(i) for i in input().split()])
s3 = set([int(i) for i in input().split()])
un = (s1.union(s2)).union(s3)
s = set([int(i) for i in range(10)])
print(*sorted(s.difference(un)))
