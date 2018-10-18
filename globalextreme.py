F = lambda x, y: 2*x**3 + 2*x**2*y + 3*y**2

a = []
def stem(i,j):
    if i + j <= 1:
        a.append(F(i, j))
        stem(i+0.1, j)
        stem(i, j + 0.1)

stem (0,0)

max = 0
for o in a:
    if o > max:
        max = o
print(max)



