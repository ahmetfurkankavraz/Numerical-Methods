import numpy as np
import sys
sys.stdin = open("in.txt", "r")


s = input()
if s == 'n':
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
    print(x, newtonlist, f_x, sep="\n\n")

elif s == 'l':

    sys.stdin = open("l-in.txt", "r")

    n = int(input())
    x = np.zeros((n))
    y = np.zeros((n))

    for i in range(n):
        x[i], y[i] = [float(i) for i in input().split()]

    for i in range(n):
        yy = 0
        print("     ", end="")
        for j in range(n):
            if j != i:
                s = "(x - " + str(x[j]) + ") * "
                print(s, end="")
                yy += len(s)      

        print(y[i], "\n", i, " "*(5-len(str(i))), "-" * yy, "\n","     ", end="", sep="")

        for j in range(n):
            if j != i:
                print("(" + str(x[i]) + " - " + str(x[j]) + ") * ", end="")  
        print("\n\n")

    xp = float(input())
    yp = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (xp - x[j])/(x[i] - x[j])
        yp += p * y[i]    
    print('Interpolated value at %.3f is %.3f.' % (xp, yp))


else:
    
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
    print(x, a, b, sep="\n\n")
