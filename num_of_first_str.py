s1, s2 = set(input().split()), set(input().split())
s = list(s1 - s2)
my = set()
for i in range(len(s)):
    my.add(int(s[i]))

print(*sorted(my))






