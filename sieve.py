import math

def sieve(num):
    allInts = [2]
    allInts.extend(range(3,math.ceil(math.sqrt(num)),2))

    for i in allInts:
        for j in allInts[i:]:
            if j % i == 0 and j != i:
                allInts.remove(j)

    return allInts
