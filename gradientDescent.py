import numpy as np
import matplotlib.pyplot as plt
from random import randint


def wikiExample(cur_x: float, df):
    # From calculation, it is expected that the local minimum occurs at x=9/4

    gamma = 0.01 # step size multiplier
    precision = 0.00001
    previous_step_size = 1 
    max_iters = 10000 # maximum number of iterations
    iters = 0 #iteration counter
    ax = []

    while (previous_step_size > precision) & (iters < max_iters):
        prev_x = cur_x
        ax.append(cur_x)
        cur_x = cur_x - (gamma * df(prev_x))
        previous_step_size = abs(cur_x - prev_x)
        iters+=1

    print("The local minimum occurs at", cur_x)
    #The output for the above will be: ('The local minimum occurs at', 2.2499646074278457)

    # visualization of x's approach to the answer

    # plt.plot(np.array(ax))
    # plt.show()

# wikiExample(-1, lambda x: 4 * x**3 - 9 * x**2)

# in three and more dimensions you're going to need to calculate a vector for the "direction of steepest ascent"
# luckily enough theres a name for that. the negative gradient
# unfortunately theres really no good way of finding that programatically
# in python numpy is a great tool for doing "vector" calculations. vectors are technically just lists of numbers e.g. fancy array library

def quickTuple(data, n: int):
    a = []
    for x in range(0, n):
        a.append(data)
    return(tuple(a))

def makeRandomArray(dimensions: int, width: int):
    randomArray = []
    for x in range(0, width**dimensions):
        randomArray.append(randint(-10,10))
    a = np.array(randomArray)
    a = np.reshape(a, quickTuple(width, dimensions))
    print(a)

def makeFunctionalArray(fn, width, shape):
    a = np.zeros(shape)
makeRandomArray(2, 10)


def gradientDescent(unde: np.array, munus: np.array):
    quo = manus[unde]
    return (quo)