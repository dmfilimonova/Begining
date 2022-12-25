s1_2 = set([int(i) for i in input().split()]).union([int(i) for i in input().split()])
s3 = set([int(i) for i in input().split()])
print(*sorted(s3.difference(s1_2), reverse= True))