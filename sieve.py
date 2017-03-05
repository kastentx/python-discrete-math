from isPrime import isPrime

def sieve(num):
    allIntegers = list(range(1,num+1))
    print(allIntegers)
    newList = {e for e in allIntegers if e % 2 != 0 or e == 2}
    print(newList)

myNum = int(input('Enter an integer: '))
sieve(myNum)

