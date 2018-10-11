import math
from pprint import pprint

def sin(x):
    x = x % 2*3.1415926535
    taylor = 0
    fact = 1
    j = 1
    for i in range(1, 50):
        # print(fact)
        taylor = taylor + (((-1)**(i-1))*(x**(2*i-1)))/fact
        fact = fact * (j+1) * (j+2)
        j = j + 2
    return taylor

test = []
t = 0
while t < 40:
    if round(math.sin(t), 3) == round(sin(t), 3):
        test.append([t, round(sin(t), 3)])
    else:
        test.append([t, False])
    t += 1
pprint(test)