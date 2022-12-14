list_ = []
list_n = []

for char in input().split():
    if len(list_n) == 0:
        list_n.append(char)
    else:
        if list_n[-1] == char:
            list_n.append(char)
        else:
            list_.append(list_n)
            list_n = []
            list_n.append(char)

if list_n:
    list_.append(list_n)

print(list_)

