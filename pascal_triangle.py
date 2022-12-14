n = int(input())


def pascal(n):
    list_p = []

    for i in range(0, n + 1):
        if i == 0 or i == n:
            list_p.append(1)
        elif i == 1 or i == n - 1:
            list_p.append(n)
        elif i == 2 or i == n - 2:
            num = n * (n - 1) // 2
            list_p.append(num)
        elif i >= 3 or i == n - i:
            list_p.append(f(n) // (f(i) * f(n - i)))

    return list_p


def f(n):
    n_1 = 1
    for i in range(1, n + 1):
        n_1 *= i
    return n_1

print(pascal(n))