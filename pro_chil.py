n = int(input())
num = []
for i in range(n):
    num.append(int(input()))


pro = int(input())
count = 0
for i in range(len(num)):
    for j in range(len(num)):
        if num[j] * num[i] == pro and j != i:
            count += 1

if count > 0:
    print("ДА")
if count == 0:
    print("НЕТ")



