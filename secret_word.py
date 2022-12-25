word, d, l = input(), {}, {}

for i in word:
    l[word.count(i)] = i

for i in range(int(input())):
    s = input().split(': ')
    d[s[0]] = s[1]

for i in word:
    print(d[l[i]], end='')