s1_2 = set([int(i) for i in input().split()]).intersection(set([int(j) for j in input().split()]))
s3 = set([int(i) for i in input().split()])
print(*sorted(s1_2.difference(s3), reverse= True))



