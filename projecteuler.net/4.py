def f():
    for i in range(999, 1, -1):
        p = int(str(i) + str(i)[::-1])

        for j in range(100, 999+1):
            if (p % j == 0) and (100 < p/j < 999):
                return p, j, p/j

print f()
