def multiplier(tableau):
    resultat = []
    i = 1
    retenue = 0
    while i <= len(tableau):
        n = 2 * tableau[-i] + retenue
        if n < 10:
            resultat.append(n)
            retenue = 0
        else:
            resultat.append(n-10)
            retenue = 1
        i += 1
    if retenue > 0:
        resultat.append(retenue)
    resultat.reverse()
    return resultat

resultat = [1]
for i in range(1, 1000+1):
    resultat = multiplier(resultat)

print sum(resultat)
