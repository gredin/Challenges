def isPrime(n):
    i = 1
    while i < n/2:
        i += 1
        if n % i == 0:
            return False
    return True

def largestPrimeFactor(n):
    i = 1
    while i < n/2:
        i += 1
        if n % i == 0:
            if isPrime(n/i):
                return n/i

print largestPrimeFactor(600851475143)
