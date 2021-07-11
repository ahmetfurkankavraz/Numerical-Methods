import numpy as np

import sys

sys.stdin = open("n-in.txt", "r")

n = int(input())
x = []
f_x = []

for i in range(n):
    xx, y = [int(i) for i in input().split()]
    f_x.append(y)
    x.append(xx)

liste = []
liste += [[1]*len(x)]

for i in range(len(x)-1):
    newliste = []
    for j in range(len(x)):
        newliste += [x[j] - x[i]]

    liste += [newliste]
  
newtonlist_tp = []

for i in range(len(x)):
    sumliste = []
    for j in range(len(x)):
        sumliste += [liste[i][j]]
    

    if i != 0:
        for j in range(len(x)):
            sumliste[j] *= newtonlist_tp[-1][j]

    newtonlist_tp += [sumliste]



newtonlist = np.transpose(newtonlist_tp)
f_x = np.array(f_x)


x = np.linalg.solve(newtonlist, f_x)

print("X matrix")
print(x, "\n")
print("Newton's Basis matrix")
print(newtonlist, "\n")
print("F(x) matrix")
print(f_x, "\n")
