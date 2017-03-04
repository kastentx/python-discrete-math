# Using the Euclidean Algorithm to 
# find the Greatest Common Denominator
# a = bq + r

def gcd(a, b):
   while (b != 0):
       (a, b) = (b, a % b)
   return a

# get input
a = int(input('Enter an integer for a: '))
b = int(input('Enter an integer for b: '))

# display results
print('a: ', a, 'b: ', b)
print('gcd: ', gcd(a, b))
