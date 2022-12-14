matrix = [[int(i) for i in input().split()] for j in range(int(input()))]
m_x, list_m = [], []
sum_ = 0
#for i in range(n):
#    m_x.insert(i, input().split())
for i in range(n):
    sum_, middle = 0, 0
    for j in range(n):
        sum_ += int(m_x[i][j])
    list_m.insert(i, sum_ // n)
for i in range(n):
    count = 0
    for j in range(n):
        if int(m_x[i][j]) > list_m[i]:
            count += 1
    print(count, end= ' ')
