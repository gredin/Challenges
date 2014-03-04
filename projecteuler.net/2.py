i = 1
j = 1
k = 1

s = 0

while k < 4000000:
    if k % 2 == 0:
        s += k

    k = i+j
    i = j
    j = k

print s
