s1 = set([int(i) for i in input().split()])
s2 = set([int(i) for i in input().split()])
s3 = set([int(i) for i in input().split()])
union_s = (s1.union(s2)).union(s3)
inter_s = (s1.intersection(s2)).intersection(s3)
print(union_s.difference(inter_s))
