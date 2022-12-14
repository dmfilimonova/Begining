#5 4 3 2 1

string = input().split(' ')
new = []
for i in range(len(string)):
    if i == len(string):
        new.insert(0, new[len(string)])
    else:
        new.insert(i + 1, string[i])

    

print(new)