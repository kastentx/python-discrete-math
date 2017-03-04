a = 8
b = 24


def gcd(a,b):
    r = b%a
    while r!=0:
        rNew = a%r
        a = r
        r = rNew
    gcd = a
    return gcd
    
print("gcd(a,b) = ", gcd(a, b))

def areRelativePrime(a,b):
    return gcd(a,b) == 1

print("Are a and b relatively prime? ", areRelativePrime(a,b))
