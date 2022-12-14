n = int(input())
m = int(input())

matrix = []
matrix_ = []
m_x = []
for r in range(n):
    for c in range(m):
        m_x.append(input())
    matrix.insert(r, m_x)
    m_x = []
for r in range(n):
    print(*matrix[r], end= ' ')
    print()

print()

for r in range(m):
    for c in range(n):
        m_x.append(matrix[c][r])
    matrix_.insert(r, m_x)
    m_x = []

for i in range(m):
    print(*matrix_[i], end= ' ')
    print()

