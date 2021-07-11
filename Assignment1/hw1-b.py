import math

x = 1.2

for i in range(-20,0):
    h = math.pow(10, i)

    result = round((2 * math.cos(x + h/2) * math.sin(h/2)) / h, 8)
    print("For h = 1e-", -i , ", Result is = " , result, sep="")


""" Results:
For h = 1e-20, Result is = 0.36235775
For h = 1e-19, Result is = 0.36235775
For h = 1e-18, Result is = 0.36235775
For h = 1e-17, Result is = 0.36235775
For h = 1e-16, Result is = 0.36235775
For h = 1e-15, Result is = 0.36235775
For h = 1e-14, Result is = 0.36235775
For h = 1e-13, Result is = 0.36235775
For h = 1e-12, Result is = 0.36235775
For h = 1e-11, Result is = 0.36235775

For h = 1e-10, Result is = 0.36235775
For h = 1e-9, Result is = 0.36235775
For h = 1e-8, Result is = 0.36235775
For h = 1e-7, Result is = 0.36235771
For h = 1e-6, Result is = 0.36235729
For h = 1e-5, Result is = 0.36235309
For h = 1e-4, Result is = 0.36231115
For h = 1e-3, Result is = 0.36189167
For h = 1e-2, Result is = 0.35769156
For h = 1e-1, Result is = 0.31519099
"""