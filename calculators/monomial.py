import sys
import numpy as np
sys.stdin = open("m-in.txt", "r")

n = int(input())
x = []
fx = []

for i in range(n):
    xx, y = [int(i) for i in input().split()]
    fx.append(y)
    x.append(xx)

l = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    a = 1
    for j in range(n):
        l[i][j] = a
        a *= x[i]


a = np.array(fx)
b = np.array(l)
x = np.linalg.solve(b, a)
print("X matrix")
print(x, "\n")
print("Vandermonde matrix")
print(a, "\n")
print("F(x) matrix")
print(b, "\n")