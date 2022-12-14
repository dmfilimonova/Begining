s = input().split()
my = set()

for i in range(len(s)):

    if int(s[i]) in my:
        print("YES")
    if int(s[i]) not in my:
        my.add(int(s[i]))
        print("NO")





