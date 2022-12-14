n = int(input())
first = 0
second = 0
third = 0
fourth = 0

for i in range(n):
    str = input().split(' ')
    x = int(str[0])
    y = int(str[1])
    if x > 0 and y > 0:
        first += 1
    if x > 0 and y < 0:
        fourth += 1
    if x < 0 and y < 0:
        third += 1
    if x < 0 and y > 0:
        second += 1
    
print(f"Первая четверть: {first}")
print(f"Вторая четверть: {second}")
print(f"Третья четверть: {third}")
print(f"Четвертая четверть: {fourth}")

