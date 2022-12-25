my = [set(input()) for i in range(int(input()))]
m_ = set()
for i in range(1,len(my)):
    m_.add(my[i].intersection_update(my[i-1]))


print(m_)



