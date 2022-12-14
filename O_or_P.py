string = input()
count = 0
for i in range(len(string)):
    while string[i] == 'Р':
        count += 1
        i += 1

print(count)

