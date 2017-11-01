from bitarray import bitarray
import numpy

hex_bin_dict = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

ip = [58, 50 , 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

ip_inv = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

e = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

p = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

s1 = numpy.matrix("14 4 13 1 2 15 11 8 3 10 6 12 5 9 0 7;"
                  "0 15 7 4 14 2 13 1 10 6 12 11 9 5 3 8;"
                  "4 1 14 8 13 6 2 11 15 12 9 7 3 10 5 0;"
                  "15 12 8 2 4 9 1 7 5 11 3 14 10 0 6 13")


s2 = numpy.matrix("15 1 8 14 6 11 3 4 9 7 2 13 12 0 5 10;"
                  "3 13 4 7 15 2 8 14 12 0 1 10 6 9 11 5;"
                  "0 14 7 11 10 4 13 1 5 8 12 6 9 3 2 15;"
                  "13 8 10 1 3 15 4 2 11 6 7 12 0 5 14 9")

s3 = numpy.matrix("10 0 9 14 6 3 15 5 1 13 12 7 11 4 2 8;"
                  "13 7 0 9 3 4 6 10 2 8 5 14 12 11 15 1;"
                  "13 6 4 9 8 15 3 0 11 1 2 12 5 10 14 7;"
                  "1 10 13 0 6 9 8 7 4 15 14 3 11 5 2 12")

s4 = numpy.matrix("7 13 14 3 0 6 9 10 1 2 8 5 11 12 4 15;"
                  "13 8 11 5 6 15 0 3 4 7 2 12 1 10 14 9;"
                  "10 6 9 0 12 11 7 13 15 1 3 14 5 2 8 4;"
                  "3 15 0 6 10 1 13 8 9 4 5 11 12 7 2 14")

s5 = numpy.matrix("2 12 4 1 7 10 11 6 8 5 3 15 13 0 14 9;"
                  "14 11 2 12 4 7 13 1 5 0 15 10 3 9 8 6;"
                  "4 2 1 11 10 13 7 8 15 9 12 5 6 3 0 14;"
                  "11 8 12 7 1 14 2 13 6 15 0 9 10 4 5 3")

s6 = numpy.matrix("12 1 10 15 9 2 6 8 0 13 3 4 14 7 5 11;"
                  "10 15 4 2 7 12 9 5 6 1 13 14 0 11 3 8;"
                  "9 14 15 5 2 8 12 3 7 0 4 10 1 13 11 6;"
                  "4 3 2 12 9 5 15 10 11 14 1 7 6 0 8 13")

s7 = numpy.matrix("4 11 2 14 15 0 8 13 3 12 9 7 5 10 6 1;"
                  "13 0 11 7 4 9 1 10 14 3 5 12 2 15 8 6;"
                  "1 4 11 13 12 3 7 14 10 15 6 8 0 5 9 2;"
                  "6 11 13 8 1 4 10 7 9 5 0 15 14 2 3 12")

s8 = numpy.matrix("13 2 8 4 6 15 11 1 10 9 3 14 5 0 12 7;"
                  "1 15 13 8 10 3 7 4 12 5 6 11 0 14 9 2;"
                  "7 11 4 1 9 12 14 2 0 6 10 13 15 3 5 8;"
                  "2 1 14 7 4 10 8 13 15 12 9 0 3 5 6 11")


s_boxes = [s1, s2, s3, s4, s5, s6, s7, s8]


# converts a hexstring to a binary string
def hexstring_to_binary_string(hexstring):
    op = ''
    for char in hexstring:
        op += hex_bin_dict[char]
    return op


# converts a hexadecimal string to a bitarray object
def hex_to_binary(hexstring):
    return bitarray(hexstring_to_binary_string(hexstring))


# given a 32-bit string returns a permuted 32-bit string under the p permutation
def p_permute(c):
    op = ""
    for index in p:
        op += c[index-1]
    return op


# given a 64-bit binary keystring returns a permuted 56-bit binary keystring
def pc1_permute(keystring):
    k = ""
    for index in pc1:
        k += keystring[index-1]
    return k


# given a 56-bit binary key string permutes it using the pc2 table and returns a 48-bit binary round keystring
def pc2_permute(keystring):
    k = ""
    for index in pc2:
        k += keystring[index-1]
    return k


# given a 64-bit binary bitstring returns a permuted 64-bit binary bitstring using the ip table
def ip_permute(bitstring):
    op = ""
    for index in ip:
        # print(index)
        op += bitstring[index-1]
    return op


# given a 64-bit binary bitstring returns a permuted 64-bit binary bitstring using the ip inverse table
def ip_inv_permute(bitstring):
    op = ""
    for index in ip_inv:
        op += bitstring[index-1]
    return op


# max bits > 0 == width of the value in bits (e.g., int_16 -> 16)
# Rotate left: 0b1001 --> 0b0011
def rotate_left(val, r_bits, max_bits):
    return (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))


# given a binary bitstring, circularly shifts it by the given shift length
def shift_left(bitstring, shift_length):
    return bin(rotate_left(int(bitstring, 2), shift_length, len(bitstring)))[2:].zfill(len(bitstring))


# given the initial 24-bit left or right half, c_0 or d_0, generates the respective nth round half c_n, or d_n
def generate_cn_or_dn(c, n):
    if n == 0:
        return c
    else:
        return generate_cn_or_dn_recurse(c, n, 0)


# given the initial 24-bit left or right half, c_0 or d_0, generates the respective nth round half c_n, or d_n by
# accumulating on the integer n which begins with value 1
def generate_cn_or_dn_recurse(c, n, i):
    if i == n:
        return c
    if i+1 == 16:
        shift_length = 1
        return shift_left(c, shift_length)
    if i+1 in [1, 2, 9]:
        shift_length = 1
        return generate_cn_or_dn_recurse(shift_left(c, shift_length), n, i+1)
    else:
        shift_length = 2
        return generate_cn_or_dn_recurse(shift_left(c, shift_length), n, i+1)


# returns the list of all half bitstrings for each round key prior to PC2 permuting
def collect_cn_or_dn(c):
    return [generate_cn_or_dn(c, n) for n in range(1, 17)]


# given the initial left and right 28-bit binary strings, generates the key schedule list by permuting the
# concatenation of all left and right corresponding pairs
def collect_keys(c0, d0):
    c_n = collect_cn_or_dn(c0)  # evaluates each c_n into a list
    d_n = collect_cn_or_dn(d0)  # evaluates each d_n into a list
    round_keys = [pc2_permute(x[0]+x[1]) for x in zip(c_n, d_n)]  # permutes the concatenation of each respective c_n, d_n
    return round_keys


# given the initial 64-bit key, converts it to a 56-bit binary string by permuting it under PC1, then
# splits the result into two 28-bit binary strings, and generates the key schedule with those two strings
def generate_keys(key):
    pc1_k = pc1_permute(hexstring_to_binary_string(key))  # shortens the key into a permuted 56-bit binary string
    c0 = pc1_k[0:28]  # a 28-bit binary keystring representing the left half
    d0 = pc1_k[28:56]  # a 28-bit binary keystring representing the right half
    return collect_keys(c0, d0)


# given the initial 32-bit left and right permuted key string partitions and the round key schedule
# performs 16 rounds of encryption and returns a 64-bit string
def loop(l, r, round_keys):
    def format_spaces(string):
        op = ""
        for i in range(0, len(string), 4):
            op += string[i:i + 4] + " "
        return op

    if len(round_keys) == 0:
        return ip_inv_permute(r+l)  # swap L16 with D16 returning a 64-bit string
    else:
        print("Round " + str(17 - len(round_keys)) + ": " + format_spaces(str(round_keys[0])))


        l_n = r
        k = round_keys[0]
        r_n = (bitarray(l) ^ bitarray(f(r, k))).to01()  # xor the previous left with the result of the feistel network
        return loop(l_n, r_n, round_keys[1:len(round_keys)])


# expands the given 32-bit string into a 48 bit-string
# by permuting the given string and adding 16 twice repeating bits
def expand(r_i):
    op = ""
    j = 0
    for i in range(j, len(r_i)):
        op += r_i[e[i]-1]
        i += 1
        j = i

    for i in range(j, 48):
        j = i
        op += r_i[e[i]-1]

    return op


# given a 48-bit string, partitions it into 8 6-bit substrings and for each substring returns a 4-bit string
def s_box(b_i):

    b1 = b_i[0:6]
    b2 = b_i[6:12]
    b3 = b_i[12:18]
    b4 = b_i[18:24]
    b5 = b_i[24:30]
    b6 = b_i[30:36]
    b7 = b_i[36:42]
    b8 = b_i[42:48]

    bs = [b1, b2, b3, b4, b5, b6, b7, b8]
    # bs = [b_i[i:i+6] for i in range(0,48,6)]
    s = ""  # a 32-bit string representing the concatenation S1(B1)S2(B2)...S8(B8) to be returned
    for i in range(8):
        decimal_row = int(bs[i][0] + bs[i][5], 2)  # concatenate b_j_1 and b_j_6, then converts the result to decimal number
        decimal_col = int(bs[i][1:5], 2)  # concatenate b_j_2, b_j_3, b_j_4, b_j_5, then convert the result to decimal number
        s += bin(s_boxes[i][decimal_row, decimal_col])[2:].zfill(4)  # find the value in the s-boxes table of s-matrices and convert to binary
    return s


# takes a 32-bit string, and a 48-bit round key, then outputs a 32-bit string
def f(r_i, k):
    a = expand(r_i)  # expands the 32-bit string to a 48-bit string using the e table
    b = (bitarray(a) ^ bitarray(k)).to01()  # xor the resultant 48-bit string with the 48-bit key and convert to string
    c = s_box(b)
    p_c = p_permute(c)
    return p_c


# given a 64-bit hex plaintext string, and a 64-bit hex key, produces a 64-bit hex ciphertext
def DES(plaintext, key):
    round_keys = generate_keys(key)
    ip = ip_permute(hexstring_to_binary_string(plaintext))  # a 64-bit permutation of the given plaintext
    l_0 = ip[0:32]  # left initial permuted 32-bit string
    r_0 = ip[32:64]  # right initial permuted 32-bit string

    x = loop(l_0, r_0, round_keys)

    return x


# ----------------------------------------------------------------------------------------------------------------------

x = "0123456789ABCDEF"

k_original = "133457799BBCDFF1"

k = "1122334455667788"


def test_rotate_left():
    bit1 = "0101"
    intbit1 = int(bit1, 2)
    bit2 = "1010"
    op = bin(rotate_left(intbit1, 1, 4))[2:].zfill(4)
    return op == bit2

# print(test_rotate_left())


def test_shift_left():
    c1 = "0000000011110000110011001011"
    result = shift_left(c1, 1)
    expected = "0000000111100001100110010110"
    return result == expected

# print(test_shift_left())


def test_hexstring_to_binary_string():
    key = "1122334455667788"
    result = hexstring_to_binary_string(key)
    expected = "0001000100100010001100110100010001010101011001100111011110001000"
    return result == expected

# print(test_hexstring_to_binary_string())


def test_halves():
    key = "1122334455667788"
    pc1 = pc1_permute(hexstring_to_binary_string(key))
    result1 = pc1[0:28]
    result2 = pc1[28:56]
    expected1 = "1000000001111000011001100101"
    expected2 = "0110011001111000100000000101"
    return result1 == expected1 and result2 == expected2

# print(test_halves())


def test_pc1_permute():
    key = "1122334455667788"
    result = pc1_permute(hexstring_to_binary_string(key))
    expected = "10000000011110000110011001010110011001111000100000000101"
    return result == expected

# print(test_pc1_permute())


def test_pc2_permute():
    # key = "1122334455667788"
    key = "133457799BBCDFF1"
    pc1 = pc1_permute(hexstring_to_binary_string(key))
    c0 = pc1[0:28]
    d0 = pc1[28:56]
    cn = collect_cn_or_dn(c0)
    dn = collect_cn_or_dn(d0)
    cndn = [x[0]+x[1] for x in zip(cn, dn)]  # list of concatenated left and right halves, c_n+d_n for 1 <= n <= 16
    keys = [pc2_permute(x) for x in cndn]  # the key schedule
    print(cndn)
    print(keys)


# test_pc2_permute()

def test_p_permute():
    s = "01011100100000101011010110010111"
    result = p_permute(s)
    expected = "00100011010010101010100110111011"
    return result == expected

# print(test_p_permute())


def test_collect_keys():
    key = "1122334455667788"
    pc1 = pc1_permute(hexstring_to_binary_string(key))
    c0 = pc1[0:28]
    d0 = pc1[28:56]
    result = collect_keys(c0, d0)
    # return result == expected
    print(result)
    print(type(result))
    print(len(result))

# test_collect_keys()


def test_generate_cn_or_dn():
    key = "1122334455667788"
    pc1 = pc1_permute(hexstring_to_binary_string(key))
    c0 = pc1[0:28]
    d0 = pc1[28:56]

    result1 = generate_cn_or_dn(c0, 16)
    print(result1)
    result2 = generate_cn_or_dn(d0, 16)
    print(result2)

    result3 = generate_cn_or_dn(c0, 15)
    print(result3)
    result4 = generate_cn_or_dn(d0, 15)
    print(result4)

    expected1 = "1000000001111000011001100101"  # c16
    expected2 = "0110011001111000100000000101"  # d16
    expected3 = "1100000000111100001100110010"  # c15
    expected4 = "1011001100111100010000000010"  # d15
    return result1 == expected1 and result2 == expected2 and result3 == expected3 and result4 == expected4

# print(test_generate_cn_or_dn())


def test_collect_cn_or_dn():
    key = "1122334455667788"
    pc1 = pc1_permute(hexstring_to_binary_string(key))
    c0 = pc1[0:28]
    d0 = pc1[28:56]
    c_n = collect_cn_or_dn(c0)
    d_n = collect_cn_or_dn(d0)
    print(c_n)
    print(len(c_n))
    print(d_n)
    print(len(d_n))

# test_collect_cn_or_dn()


def test_expand():
    r_0 = "11110000101010101111000010101010"
    print(len(r_0))
    result = expand(r_0)
    print(result)
    print(len(result))
    expected = "011110100001010101010101011110100001010101010101"
    print(expected)
    print(len(expected))
    return result == expected

# print(test_expand())


def test_f():
    r_0 = "11110000101010101111000010101010"
    k1 = "000110110000001011101111111111000111000001110010"

    e = bitarray(expand(r_0))
    print(e)
    k = bitarray(k1)
    print(k)
    result = (e ^ k).to01()
    print(result)

    expected = "011000010001011110111010100001100110010100100111"
    print(expected)

    return result == expected

# print(test_f())


def test_s_box():
    r_0 = "11110000101010101111000010101010"
    k1 = "000110110000001011101111111111000111000001110010"

    e = bitarray(expand(r_0))
    k = bitarray(k1)
    xored = (e ^ k).to01()
    print(xored)
    result = s_box(xored)
    expected = "01011100100000101011010110010111"
    return result == expected

# print(test_s_box())


def DES_test():
    x = "00AABBCCDDEEFF99"
    key = "1122334455667788"
    x_original = "0123456789ABCDEF"
    k_original = "133457799BBCDFF1"
    result_original = DES(x_original, k_original)
    expected_original = "1000010111101000000100110101010000001111000010101011010000000101"
    # result = DES(x, key)
    # expected = ""
    return result_original == expected_original

# print(DES_test())


def print_round_keys():

    x_original = "0123456789ABCDEF"
    k_original = "133457799BBCDFF1"
    # result_original = DES(x_original, k_original)
    x = "00AABBCCDDEEFF99"
    key = "1122334455667788"
    result = DES(x, key)


print(print_round_keys())

