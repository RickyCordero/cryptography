from math import gcd

p = 43

#
# # returns the set of coprime integers less than n in Z_26
# def inv_zn(n):
#     return [x for x in range(n) if gcd(x, p) == 1]
#
#
# # returns the number of coprime integers less than n in Z_26
# def phi(n):
#     return len(inv_zn(n))


# phi_p = phi(p)
phi_p = 42
# prime_divisors_of_phi_p = [2, 7]
prime_divisors_of_phi_p = [2, 3, 7]


# Determines if the given integer element in Z_42 is a primitive element
def is_primitive_element(element):
    for divisor in prime_divisors_of_phi_p:
        power = pow(element, int((phi_p/divisor)), p)
        print(element, power)
        if power == 1:
            return False
    return True

z_p = [i for i in range(1, p)]
primitive_elements = list(filter(is_primitive_element, z_p))

# print(z_p)
# print(len(z_p))
# print(primitive_elements)
# print(len(primitive_elements))

