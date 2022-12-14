s1, s2 = input().split(), input().split()
my = set()
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            my.add(int(s1[i]))



print(*sorted(my))




