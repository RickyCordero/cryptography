from bitarray import bitarray



x = "26B7"  # represents the hex plaintext
N_r = 5  # represents the number of rounds to iterate
K_0 = "A1D5FB08F"  # represents the initial key

s = {0: "E", 1: "A", 2: "0", 3: "5", 4: "2", 5: "C", 6: "F", 7: "3", 8: "7", 9: "9", 10: "8", 11: "D", 12: "1", 13: "B", 14: "6", 15: "4"}
p = {0: "12", 1: "9", 2: "0", 3: "1", 4: "15", 5: "8", 6: "11", 7: "13", 8: "7", 9: "2", 10: "3", 11: "14", 12: "4", 13: "5", 14: "6", 15: "10"}


def s_box(z):
    """
    Permute z under s
    """
    return s[z]


def p_box(z):
    """
    Permute z under p
    """
    return p[z]


def hexstring_to_binary_string(hexstring):
    """
    Converts a hexstring to a binary string
    """
    num_of_bits = len(hexstring)
    bitstring = bin(int(hexstring, 16))[2:].zfill(16)
    # return ' '.join(bitstring[i:i + 4] for i in range(0, 32, 4))
    return bitstring


def hex_to_binary(hexstring):
    """
    Converts a hexadecimal string to a bitarray object
    """
    return bitarray(hexstring_to_binary_string(hexstring))


def key_schedule(init_key, r):
    """
    Shift the init_key by 4 bits
    """
    return (init_key << 4)[0:15]


def SPN(plaintext, pi_s, pi_p, key_schedule, N_r):
    """
    Returns the SPN-iterated block-cipher of the given plaintext
    """
    w_0 = hex_to_binary(plaintext)
    for r in range(key_schedule-1):

        u_r = SPN()


w_0 = hex_to_binary(x)
k_0 = hex_to_binary(K_0)

print(w_0)

print(k_0)


# print(b)
# print(type(b))

# print(c)
# print(type(c))
