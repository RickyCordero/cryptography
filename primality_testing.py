from math import log
from math import gcd


def pi(n):
    """
    Returns the approximate number of primes less than n
    """
    return n/log(n)


def fermat_witnesses(n):
    """
    Returns the list of Fermat-witnesses of n
    """
    return [x for x in range(1, n) if (x**n % n) != x]


# def miller_rabin_witnesses(n):
#     return [x for x in range(1, )]


def factor(n):
    """
    Returns the pair k,q where n-1 = (2^k)*q
    """
    m = n-1
    k = 0
    q = 0
    while m % 2 == 0 and m/2 > 1:
        k += 1
        m = m/2
    q = int((n-1)/(2**k))
    return k, q


def miller_rabin_composite(a, n):
    """
    Determines if the number n is composite using the Miller Rabin test
    with the integer a between 1 and n exclusively
    """
    f = factor(n)
    k = f[0]
    q = f[1]
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


def fermat_composite(n):
    """
    Determines if the given number is composite
    """
    return len(fermat_witnesses(n)) > 0


def find_miller_rabin_witness(n):
    """
    Finds the miller rabin witnesses of the given number
    """
    i = 2
    while not miller_rabin_composite(i, n):
        i += 1
    return i

def test_pi():
    print(pi(100))

def test_factor():
    print(factor(1729))
    print(factor(1105))

def test_fermat_witnesses():
    print(fermat_witnesses(561))

def test_fermat_composite():
    print(fermat_composite(561))

def test_miller_rabin_witness():
    n1 = 118901509  # is prime
    print("n1: ",n1)
    print("miller rabin witness: ",find_miller_rabin_witness(n1))
    
def test_miller_rabin_composite():
    n2 = 118901529  # is not prime
    print("miller rabin composite: ", miller_rabin_composite(2, n2))

if __name__ == "__main__":
    test_miller_rabin_witness() 
