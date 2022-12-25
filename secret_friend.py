from random import *

l = [[j for j in input().split()] for i in range(int(input()))]
n = l

for i in l:
    m = choice(n)
    if i != m:
        print(f"{i} - {m}")
        del n[n.find(m)]









