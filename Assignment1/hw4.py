def calculateCubeRoot(y):
    print("\n")
    a, e = y, 0

    while a >= 1:
        a = a/2
        e += 1

    c1, c2, c3 = 2**(1/3), 2/3, a/3

    # Calculate a^(1/3) using Newton iteration #
    an = 0
    an1 = 0.90

    flopCounterForNewtonIteration = 0
    newtonIterationCounter = 0
    while abs(an1-an) > 2**(-52):
        an = an1
        k = c2 * an 
        flopCounterForNewtonIteration += 1  # Increment flopCounterForNewtonIteration for every flop operation
        l1 = an**2
        flopCounterForNewtonIteration += 1
        l = c3 / l1
        flopCounterForNewtonIteration += 1
        an1 = k + l
        flopCounterForNewtonIteration += 1
        newtonIterationCounter+=1


    qubeRootA = an1
    flopCounterPerNewtonIteration = int(flopCounterForNewtonIteration / newtonIterationCounter)
    # Printing informations about Newton iteration #
    print("A = ", a, " QubeRoot of A = ",qubeRootA, ". ")
    print("Found with ", newtonIterationCounter, " iteration. ") 
    print("Per iteration flop count is = ", flopCounterPerNewtonIteration)

    flopCounter = 0

    integerExp = e // 3   # These are not floating point operations. #
    remainExp = e % 3   # These are only integer operations. #
    qubeRootY = 2**(integerExp)

    qubeRootY *= qubeRootA  # Increment flopCounter for every flop operation
    flopCounter += 1

    if remainExp == 1:
        qubeRootY *= c1     # Increment flopCounter for every flop operation
        flopCounter += 1
    elif remainExp == 2:
        qubeRootY *= c1     # Increment flopCounter for every flop operation
        flopCounter += 1
        qubeRootY *= c1     # Increment flopCounter for every flop operation
        flopCounter += 1
    
    # Printing informations about Newton Iteration #
    print("Y = ", y,"QubeRoot of Y = ", qubeRootY, ". ")
    print("Flop count after a^(1/3) found is ", flopCounter)


# Some test cases #
y = int(input("Please write a Y value = "))
calculateCubeRoot(y)
calculateCubeRoot(1)
calculateCubeRoot(954945211586315)
calculateCubeRoot(46854531351)
calculateCubeRoot(201468541616516)
calculateCubeRoot(5151531)
calculateCubeRoot(48646854218611651681)
calculateCubeRoot(641541563156314561534135135135153135165841534135135)
calculateCubeRoot(15313513515315845843541321586413515313513513513515341658416583416354563415341534153454)
calculateCubeRoot(15565641848651)