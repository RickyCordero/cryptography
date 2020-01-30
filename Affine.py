from math import gcd
import collections
import itertools
import operator


# we will decode these cyphertexts
substitution_ciphertext = "EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCKQPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCGOIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZUGFZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNSACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUEKUZCSOCFZCCNCIACZEJNCSHFZEJZEGMXCYHCJUMGKUCY"

vigenere_ciphertext = "KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST"

affine_ciphertext = "KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUPKRIOFKPACUZQEPBKRXPEIIEABDKPBCPFCDCCAFIEABDKPBCPFEQPKAZBKRHAIBKAPCCIBURCCDKDCCJCIDFUIXPAFFERBICZDFKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERKIVKSCPICBRKIJPKABI"

unknown_ciphertext = "BNVSNSIHQCEELSSKKYERIFJKXUMBGYKAMQLJTYAVFBKVTDVBPVVRJYYLAOKYMPQSCGDLFSRLLPROYGESEBUUALRWXMMASAZLGLEDFJBZAVVPXWICGJXASCBYEHOSNMULKCEAHTQOKMFLEBKFXLRRFDTZXCIWBJSICBGAWDVYDHAVFJXZIBKCGJIWEAHTTOEWTUHKRQVVRGZBXYIREMMASCSPBNLHJMBLRFFJELHWEYLWISTFVVYFJCMHYUYRUFSFMGESIGRLWALSWMNUHSIMYYITCCQPZSICEHBCCMZFEGVJYOCDEMMPGHVAAUMELCMOEHVLTIPSUYILVGFLMVWDVYDBTHFRAYISYSGKVSUUHYHGGCKTMBLRX"


# table of letter frequencies in order
true_freq_list = sorted({"e": 13.11, "t": 10.47, "a": 8.15, "o": 8.00, "n": 7.1, "r": 6.83, "i": 6.35,
                                      "s": 6.10, "h": 5.26, "d": 3.79, "l": 3.39, "f": 2.92, "c": 2.76, "m": 2.54,
                                      "u": 2.46, "g": 1.99, "y": 1.98, "p": 1.98, "w": 1.54, "b": 1.44, "v": .92,
                                      "k": 0.42, "x": 0.17, "j": 0.13, "q": 0.12, "z": 0.08}.items(), key=operator.itemgetter(1), reverse=True)


def index(a):
    """
    Returns the integer representation of the given English character, otherwise returns the string
    representation of the given integer, e.g. a => 0, b => 1, c => 2, ...
    """
    sigma = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if isinstance(a, str):
        return sigma.index(a.lower())
    if isinstance(a, int):
        return sigma[a]


def index_convert(plaintext):
    """
    Returns a list containing the integer representations of each character over Z_26 in the given 
    plaintext string
    """
    return [index(character) for character in plaintext]


def e(a, b):
    """
    Returns the encryption function given the key k = (a,b) in Z_26
    """
    return lambda x: (a*x + b) % 26


def d(a, b):
    """
    Returns the decryption function given the key k = (a,b) in Z_26
    """
    return (lambda x: inv(a)*(x-b) % 26) if (a in inv_zn(26)) else ("("+str(a)+", "+str(b)+") is an invalid decryption key")


def inv(x):
    """
    Returns the inverse of x in Z_26 if x is invertible
    """
    return inv_n(x, 26)


def inv_n(x, n):
    """
    Returns the inverse of x in Z_n if x is invertible
    """
    for i in range(n):
        if i * x % n == 1:
            return i
    return str(x) + " = " + str(x % 26) + " is not invertible in Z_" + str(n)\
        if x >= n else str(x) + " is not invertible in Z_"+str(n)


def inv_zn(n):
    """
    Returns the set of coprime integers less than n in Z_26
    """
    return [x for x in range(n) if gcd(x, 26) == 1]


def phi(n):
    """
    Returns the number of coprime integers less than n in Z_26
    """
    return len(inv_zn(n))


def freq(ciphertext):
    """
    Returns a list representation of the frequency table for the given ciphertext string sorted in ascending
    order by occurrence number
    """
    unsorted_table = {character.lower(): ciphertext.count(character) for character in set(ciphertext)}
    return sorted(unsorted_table.items(), key=operator.itemgetter(1), reverse=True)


def frequency_analysis(ciphertext):
    """
    Performs a brute force attack on the ciphertext by first finding all potential keys starting with the most
    frequently occurring sample letters then testing each key by applying the decryption function on the
    ciphertext and printing the results to see if anyone of them is intelligible
    """
    f = freq(ciphertext)
    for i in range(len(f)-2):
        if i == 0:
            max_occurring_character_integer = f[len(f) - (i + 1)][1]  # let this character be "e"
            all_max = [x for x in f if x[1]==max_occurring_character_integer]
            for pair in all_max:
                x = index(true_freq_list[i][0])
                y = index(pair[0])
                keys = [(a, b) for a, b in itertools.product(inv_zn(x), [x in range(26)]) if e(a, b)(x) == y]

        elif 1 <= i <= 8:

            # T, A, O, N, R, I, S, H
            max_occuring_character = f[len(f)-(i+1)][1]

        elif 9 <= i <= 10:
            # D, L
            max_occuring_character = f[len(f) - (i + 1)][1]

        elif 11 <= i <= 19:
            # F, C, M, U, G, Y, P, W, B
            max_occuring_character = f[len(f) - (i + 1)][1]
        else:
            # V, K, X, J, Q, Z
            max_occuring_character = f[len(f) - (i + 1)][1]


def keys(x, y):
    """
    Returns the list of all keys k = (a, b) from U(Z_26) x Z_26 such that e(a, b)(x) = y
    """
    return [(a, b) for a, b in [key for key in itertools.product(inv_zn(26), [n for n in range(26)])] if e(a, b)(x) == y]


def brute_force(ciphertext):
    """
    Constructs and prints multiple plaintext strings using each key in keys by concatenating the result of the
    decryption function on each ciphertext character
    """
    frequency_list = freq(ciphertext)
    print("sample frequencies:")
    print(frequency_list)
    print(len(frequency_list))
    for i in range(len(frequency_list)):
        if i == 0:
            max_occurring_true_characters = ["e"]
        elif 1 <= i <= 8:
            # T, A, O, N, R, I, S, H
            max_occurring_true_characters = ["t", "a", "o", "n", "r", "i", "s", "h"]
        elif 9 <= i <= 10:
            # D, L
            max_occurring_true_characters = ["d", "l"]
        elif 11 <= i <= 19:
            # F, C, M, U, G, Y, P, W, B
            max_occurring_true_characters = ["f", "c", "m", "u", "g", "y", "p", "w", "b"]
        elif 20 <= i <= 26:
            # V, K, X, J, Q, Z
            max_occurring_true_characters = ["v", "k", "x", "j", "q", "z"]

        print("max occurring true characters: " + str(max_occurring_true_characters))
        max_occurring_sample_character = frequency_list[i][0]
        print("max occurring sample character: " + max_occurring_sample_character)
        all_max = [x for x in frequency_list if x[1] == index(max_occurring_sample_character)]
        for true_char in max_occurring_true_characters:
            for pair in all_max:
                print("level = " + str(i))
                x = index(true_char)
                y = index(pair[0])
                key_list = keys(x, y)
                for key in key_list:
                    op = ""
                    for character in ciphertext:
                        op += index(d(key[0], key[1])(index(character)))
                    print(str(key) + ": " + str(op))
            i += 1


def decrypt(ciphertext):
    """
    Decrypts a ciphertext string using k = (19, 4)
    """
    op = ""
    for character in ciphertext:
        op += index(d(19, 4)(index(character)))
    return op


if __name__ == "__main__":
    # Decrypt the canadian national anthem in french
    plaintext = decrypt(affine_ciphertext)
    print(plaintext)
