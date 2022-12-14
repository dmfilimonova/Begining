n = int(input())
m = int(input())

matrix = []
m_x = []

for r in range(n):
    for c in range(m):
        m_x.append(input())
    matrix.append(m_x)
    m_x = []

for r in range(n):

    print(*matrix[r], end= ' ')
    print()
