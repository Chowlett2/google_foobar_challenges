'''Making fuel for the LAMBCHOP's reactor core is a tricky process because of 
the exotic matter involved. It starts as raw ore, then during processing, 
begins randomly changing between forms, eventually reaching a stable form. 
There may be multiple stable forms that a sample could ultimately reach, 
not all of which are useful as fuel.

Commander Lambda has tasked you to help the scientists increase fuel creation 
efficiency by predicting the end state of a given ore sample. You have carefully 
studied the different structures that the ore can take and which transitions it undergoes. 
It appears that, while random, the probability of each structure transforming is fixed. 
That is, each time the ore is in 1 state, it has the same probabilities of entering the 
next state (which might be the same state). You have recorded the observed transitions in a matrix.
The others in the lab have hypothesized more exotic forms that the ore can become, 
but you haven't seen all of them.

Write a function answer(m) that takes an array of array of nonnegative ints representing 
how many times that state has gone to the next state and return an array of ints for each 
terminal state giving the exact probabilities of each terminal state, represented as the 
numerator for each state, then the denominator for all of them at the end and in simplest form. 
The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, 
there is a path from that state to a terminal state. That is, the processing will always eventually 
end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit 
integer during the calculation, as long as the fraction is simplified regularly.'''

from fractions import Fraction
from math import gcd

def lcm(x, y):
    return int(x*y/gcd(x,y))

def transform_function(x):
    newMatrix = []
    transformMatrix = []
    zerosMatrix = []
    sums = list(map(sum, x))
    bools = list(map(lambda x: x == 0, sums))
    index = set([i for i, x in enumerate(bools) if x])
    for i in range(len(x)):
        newMatrix.append(list(map(lambda x: Fraction(0, 1) if(sums[i] == 0) 
                                  else Fraction(x, sums[i]), x[i])))
    for i in range(len(newMatrix)):
        if i not in index:
            transformMatrix.append(newMatrix[i])
        else:
            zerosMatrix.append(newMatrix[i])
    transformMatrix.extend(zerosMatrix)
    transMatrix = []
    for i in range(len(transformMatrix)):
        transMatrix.append([])
        extransMatrix = []
        for j in range(len(transformMatrix)):
            if j not in index:
                transMatrix[i].append(transformMatrix[i][j])
            else:
                extransMatrix.append(transformMatrix[i][j])
        transMatrix[i].extend(extransMatrix)
    return [transMatrix, len(zerosMatrix)]

def duplicate_matrix(x):
    dupMatrix = []
    for i in range(len(x)):
        dupMatrix.append([])
        for j in range(len(x[i])):
            dupMatrix[i].append(Fraction(x[i][j].numerator, x[i][j].denominator))
    return dupMatrix

def gaussian_elimination(matrix, values):
    newMatrix = duplicate_matrix(matrix)
    for i in range(len(newMatrix)):
        index = -1
        for j in range(i, len(newMatrix)):
            if newMatrix[j][i].numerator != 0:
                index = j
                break
        newMatrix[i], newMatrix[index] = newMatrix[index], newMatrix[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i+1, len(newMatrix)):
            if newMatrix[j][i].numerator == 0:
                continue
            ratio = -newMatrix[j][i]/newMatrix[i][i]
            for k in range(i, len(newMatrix)):
                newMatrix[j][k] += ratio * newMatrix[i][k]
            values[j] += ratio * values[i]
    x = [0 for i in range(len(newMatrix))]
    for i in range(len(newMatrix)):
        index = len(newMatrix) -1 -i
        y = len(newMatrix) - 1
        while y > index:
            values[index] -= newMatrix[index][y] * x[y]
            y -= 1
        x[index] = values[index]/newMatrix[index][index]
    return x

def transpose_func(x):
    transMatrix = []
    for i in range(len(x)):
        for j in range(len(x)):
            if i == 0:
                transMatrix.append([])
            transMatrix[j].append(x[i][j])
    return transMatrix

def inverse_matrix(x):
    transMatrix = transpose_func(x)
    invMatrix = []
    for i in range(len(transMatrix)):
        values = [Fraction(int(i==j), 1) for j in range(len(x))]
        invMatrix.append(gaussian_elimination(transMatrix, values))
    return invMatrix

def multiply_matrices(x, y):
    product = []
    for i in range(len(x)):
        product.append([])
        for j in range(len(y[0])):
            product[i].append(Fraction(0, 1))
            for k in range(len(x[0])):
                product[i][j] += x[i][k] * y[k][j]
    return product

def split(x, y):
    lengthQ = len(x) - y
    Q = []
    R = []
    for i in range(lengthQ):
        Q.append([int(i==j)-x[i][j] for j in range(lengthQ)])
        R.append(x[i][lengthQ:])
    return [Q, R]

def solution(m):
    final = transform_function(m)
    if final[1] == len(m):
        return [1, 1]
    Q, R = split(*final)
    inv = inverse_matrix(Q)
    final = multiply_matrices(inv, R)
    row = final[0]
    l = 1
    for item in row:
        l = lcm(l, item.denominator)
    final = list(map(lambda m: int(m.numerator*l/m.denominator), row))
    final.append(l)
    return final
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))