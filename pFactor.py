# Prime Factorization
from sieve2 import sieve

def pFactorize(num):
    primeFactors = list()
    factorization = list()

    # build list of prime factors
    for e in sieve(num):
        if num % e == 0:
            primeFactors.append(e)

    # divide by factors to build factorization
    for prime in primeFactors:
        while num % prime == 0:
            factorization.append(prime)
            num = num / prime
    
    # format output
    return ' x '.join(map(str, factorization))

# get input
while 1<2:
    myNum = int(input('Enter a number to see its prime factorization: '))
    print('factorized:', pFactorize(myNum))
