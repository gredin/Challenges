def isPrime(n, primes):
    for i in primes:
        if n % i == 0:
            return False
    return True

primes = []
i = 1
while len(primes) <= 10000:
    i += 1
    if isPrime(i, primes):
        primes.append(i)

print primes.pop()
