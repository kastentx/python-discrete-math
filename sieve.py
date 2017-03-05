from isPrime import isPrime
from math import sqrt

def sieve(num):
    allInts = list(range(2,num+1))
    searchMax = int(sqrt(num))

    for i in allInts:
        if i > searchMax:
            break

        for j in allInts:
            if j % i == 0 and j != i:
                allInts.remove(j)

    print(allInts)

myNum = int(input('Enter an integer to get primes from the sieve: '))
sieve(myNum)

