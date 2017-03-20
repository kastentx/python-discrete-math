from math import sqrt

def sieve(num):
    allInts = list(range(2,num+1,))
    searchMax = int(sqrt(num))

    for i in allInts:
        if i > searchMax:
            break

        for j in allInts[i:]:
            if j % i == 0 and j != i:
                allInts.remove(j)

    return allInts
