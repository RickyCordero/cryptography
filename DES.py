from bitarray import bitarray
import numpy

hex_bin_dict = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

ip = [58, 50 , 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

ip_inv = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

e = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

p = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

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
    # num_of_bits = len(hexstring)
    # bitstring = bin(int(hexstring, 16))[2:].zfill(16)
    # return ' '.join(bitstring[i:i + 4] for i in range(0, 32, 4))
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
        op += c[index]
    return op


# expands the given 32-bit string into a 48 bit-string
# by permuting the given string and adding 16 twice repeating bits
def expand(r_i):
    op = ""
    j = 0
    for i in range(j, len(r_i)):
        op += r_i[e[i]]
        i += 1
        j = i

    for i in range(j, 30):
        j = i
        op += r_i[e[i]]

    return op


# Given a 48-bit string partitions it into 8 6-bit substrings and for each substring returns a 4-bit string
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

    for b_j in bs:
        decimal_row = int(b_j[0]+b_j[5], 2)  # concatenate b_j_1 and b_j_6, then convert to binary
        decimal_col = int(b_j[1:5], 2)  #
        c = ""  # a 32-bit string
        for i in range(8):
            c += int(s_boxes[i][decimal_row][decimal_col], 2)  # find the value in the s-boxes table of s-matrices and convert to binary
    return c


# takes a 32-bit string, and a 48-bit round key, then outputs a 32-bit string
def f(r_i, k):
    a = expand(r_i)  # expands the 32-bit string to a 48-bit string
    b = bitarray(a) ^ k  # xor the resultant 48-bit string with the 48-bit key
    c = s_box(b)
    p_c = p_permute(c)
    return p_c


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


# Given a 64-bit binary bitstring returns a permuted 64-bit binary bitstring using the ip table
def ip_permute(bitstring):
    op = ""
    for index in ip:
        op += bitstring[index-1]
    return op


# given a 56-bit binary key and an integer round number returns the current round key
def curr_key(key, round):
    pass


# max bits > 0 == width of the value in bits (e.g., int_16 -> 16)
# Rotate left: 0b1001 --> 0b0011
def rotate_left(val, r_bits, max_bits):
    return (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

# given a binary bitstring, circularly shifts it by the given shift length
def shift_left(bitstring, shift_length):
    return bin(rotate_left(int(bitstring, 2), shift_length, len(bitstring)))[2:].zfill(len(bitstring))

# generates the 24-bit left and right halves of the nth round key
def gen_n(c, n):
    if n == 16:
        shift_length = 1
        return shift_left(c, shift_length)
    if n in [1,2,9]:
        shift_length = 1
        return gen_n(shift_left(c, shift_length), n+1)
    else:
        shift_length = 2
        return gen_n(shift_left(c, shift_length), n+1)

# given the initial left and right 28-bit binary strings, generates the key schedule list by permuting the
# concatenation of the current left and right
def collect_keys(c0, d0):
    round_keys = []
    for n in range(1, 16):
        c_n = gen_n(c0, n)  # passes the round as the second parameter
        d_n = gen_n(d0, n)
        k_n = pc2_permute(c_n+d_n)
        round_keys.append(k_n)
    return round_keys

# given the initial 64-bit key, converts it to a 56-bit binary string by permuting it under PC1, then
# splits the result into two 28-bit binary strings, and generates the key schedule with those two strings
def generate_keys(key):
    pc1_k = pc1_permute(hexstring_to_binary_string(key))  # a permuted 56-bit binary keystring
    c0 = pc1_k[0:28]  # a 28-bit binary keystring
    d0 = pc1_k[28:56]  # a 28-bit binary keystring
    return collect_keys(c0, d0)

def do_stuff(l, r, round_keys):
    if len(round_keys)==0:
        return l+r
    else:
        l_n = r
        k = round_keys[0]
        r_n = bitarray(l) ^ f(r, k) # xor
        return do_stuff(l_n, r_n, round_keys[1:len(round_keys)])


# given a 64-bit hex plaintext string, and a 64-bit hex key, produces a 64-bit hex ciphertext
def DES(plaintext, key):
    round_keys = generate_keys(key)
    ip = ip_permute(hexstring_to_binary_string(plaintext)) # a 64-bit permutation of the given plaintext
    l_0 = ip[0:32]  # left initial permuted 32-bit string
    r_0 = ip[32:64] # right initial permuted 32-bit string

    x = do_stuff(l_0, r_0, round_keys)
    for i in range(len(round_keys)):



    return



# given a 64-bit hex plaintext string, a 56-bit hex key, produces a 64-bit hex ciphertext
def g(w, key, round):
    return
    # round_key = curr_key(hex_to_binary(key), round)
    # left = hex_to_binary(w)[0:32]  # convert the left side of the 32-bit hex string to binary
    # right = hex_to_binary(w)[32:64]  # convert the right side of the 32-bit hex string to binary
    # key = hex_to_binary(key)  # convert the hex key to binary

    # if round == 0:  # initial case
    #     left = hex_to_binary(w)[0:32]  # convert the left side of the 32-bit hex string to binary
    #     right = hex_to_binary(w)[32:64]  # convert the right side of the 32-bit hex string to binary
    #     key = hex_to_binary(keys[round])  # convert the hex key to binary
    #     init_permutation = ip_permute(left+right)  # permutes the concatenated left and right 32-bit binary strings of the given plaintext
    #     left = init_permutation[0:32]  # stores this round's left 32-bit binary string
    #     right = init_permutation[32:64]  # stores this round's right 32-bit binary string
    #     op = bitarray(left) ^ f(right, key[round])
    #     return DES(op, keys[round+1:len(keys)], round+1)
    # elif round == 15:  # base case
    #     pass
    # else:
    #     # new_left = init_permutation[0:32]  # stores this round's left 32-bit binary string
    #     # new_right = init_permutation[32:64]  # stores this round's right 32-bit binary string
    #     output = bitarray(left) ^ f(right, key[round])  # xor this round's left with the function output
    #
    #     final_left = output[0:32]  # stores this round's final left 32-bit binary string
    #     final_right = output[32:64]  # stores this round's final right 32-bit binary string
    #     return DES(final_left)


x = "0123456789ABCDEF"

k = "133457799BBCDFF1"


def test_pc1_permute():
    test_key_1 = "0001001100110100010101110111100110011011101111001101111111110001"

    op_key_1 = "11110000110011001010101011110101010101100110011110001111"

    # a = pc1_permute(test_key_1)
    # print(test_key_1)
    # print(len(test_key_1))
    # print(op_key_1)
    # print(len(op_key_1))

    # print(a)
    # print(len(a))
    return pc1_permute(test_key_1) == op_key_1 # true


def test_rotate_left():
    bit1 = "0101"
    intbit1 = int(bit1, 2)
    print(bit1)
    bit2 = "1010"
    op = bin(rotate_left(intbit1, 1, 4))[2:].zfill(4)
    return op == bit2

def test_pc2_permute():


# print(test_rotate_left())

