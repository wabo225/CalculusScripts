lhsA = 0
rhsA = 0
n = int(input("n: "))
for x in range(0, n):
    lhsA = lhsA + x**2
    rhsA = rhsA + (2*x-1)*(n-x)
    print(lhsA, "    ", rhsA)
