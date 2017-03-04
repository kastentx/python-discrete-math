import math

def isPrime(num):
    # 0, 1, and 2 are special cases, so first handle those
    if num <= 1:
        return False
    elif num == 2:
        return True
    
    # we only need to go up to the square root
    # of the number we are testing
    testMax = int(math.sqrt(num)) + 1

    # loop runs from 2 up to but NOT including
    # the value of testMax
    for i in range(2,testMax):
        if num % i == 0:
            return False
    return True

