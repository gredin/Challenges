cache = {}

def f(p, q):
    if ((p, q) in cache):
        return cache[(p,q)]
    if min(p, q) == 0:
        return 1
    else:
        cache[] = f(p-1, q)
        b = f(p, q-1)
        return 

print f(20, 20, {})
