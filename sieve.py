from isPrime import isPrime

def sieve(num):
    allIntegers = list(range(1,num+1))
    print(allIntegers)
    if (isPrime(num)):
        print('number is prime')

myNum = int(input('Enter an integer: '))
sieve(myNum)

