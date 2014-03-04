sumSquares = 0
s = 0
for i in range(1, 100+1):
    sumSquares += i*i
    s += i

squareSum = s*s

print (squareSum - sumSquares)
