n = int(input())

m_x = []
track = 0

for i in range(n):
    m_x.insert(i, input().split())

for i in range(n):
    print(*m_x[i], end= ' ')
    print()

for i in range(n):
    for j in range(n):
        if i == j:
            track += int(m_x[i][i])

print(track)



