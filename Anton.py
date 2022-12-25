# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
c = 0
l = []
for i in range(1, int(input()) + 1):
    s = input()
    for j in s:
        if j in 'anton':
            c += 1

    if c == 5:
        l.append(i)
        c = 0

print(*l)


