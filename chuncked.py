st = input().split()
n = int(input())

def chunked(st, n):
    list_ = []
    new_l = []
    count = 0
    for i in range(len(st)):
        if count == n:
            new_l.append(list_)
            list_ = []
            count -= n
        if count != n:
            list_.append(st[i])
            count += 1
    if list_:
        new_l.append(list_)

    return new_l
print(chunked(st, n))
