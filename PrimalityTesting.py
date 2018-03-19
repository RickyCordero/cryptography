from math import log
from math import gcd


# Returns the approximate number of primes less than n
def pi(n):
    return n/log(n)


# Returns the list of Fermat-witnesses of n
def fermat_witnesses(n):
    return [x for x in range(1, n) if (x**n % n) != x]


# def miller_rabin_witnesses(n):
#     return [x for x in range(1, )]


# Returns the pair k,q where n-1 = (2^k)*q
def factor(n):
    m = n-1
    k = 0
    q = 0
    while m % 2 == 0 and m/2 > 1:
        k += 1
        m = m/2
    q = int((n-1)/(2**k))
    return k, q


# Determines if the number n is composite using the Miller Rabin test with the integer a between 1 and n exclusively
def miller_rabin_composite(a, n):
    print("a = "+str(a))
    f = factor(n)
    k = f[0]
    q = f[1]
    print(k, q)
    b0 = (a ** q) % n
    if b0 == 1 or b0 == -1:
        return False
    else:
        for i in range(0, k):
            b0 = (b0 ** 2) % n
            if b0 == 1:
                return True
            elif b0 == -1:
                return False
            else:
                pass

    return True


# Determines if the given number is composite
def fermat_composite(n):
    return len(fermat_witnesses(n)) > 0

r1 = 1105
r2 = 294409
r3 = 294439

c1 = 561
c2 = 1105
c3 = 1729

# tests = lambda n: [x for x in range(1, n) if gcd(x, n) == 1]


def find_miller_rabin_witness(n):
    i = 2
    while not miller_rabin_composite(i, n):
        i += 1
    return i

# print(pi(100))
# print(factor(1729))
# print(factor(r1))
# print(fermat_witnesses(561))
# print(fermat_composite(561))

n1 = 118901509  # is prime
n2 = 118901529  # is not prime

print(factor(n1))
print(factor(n2))


# print(find_miller_rabin_witness(n1))
# print(find_miller_rabin_witness(r2))
# print(find_miller_rabin_witness(r3))

# print(miller_rabin_composite(2, n2))
# miller_rabin_composite(2, 1729)
