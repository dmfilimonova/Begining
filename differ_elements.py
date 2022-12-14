n = input().split(' ')
count = 1
flag = n[0]
for i in range(len(n)):
    if flag != n[i]:
        count += 1
        flag = n[i]
    
print(count)

