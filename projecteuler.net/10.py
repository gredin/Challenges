n = 2*10**6

dicoPrimes = {}
for i in range(2, n):
    dicoPrimes[i] = True

for i in range(2, n):
    k = 1
    while i*k < n:
        k += 1
        dicoPrimes[i*k] = False

s = 0
for p in dicoPrimes:
    if dicoPrimes[p]:
        s += p

print s
