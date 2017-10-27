import operator
import re
from functools import reduce
from math import gcd


def sigex(a):
    sigma = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if isinstance(a, str):
        return sigma.index(a.lower())
    if isinstance(a, int):
        return sigma[a]


def ek(key, plaintext):
    m = len(key)
    y = ""
    print("|p|="+str(len(plaintext)))
    print("|k|="+str(m))
    for i in range(len(plaintext)):
        ki = key[i % m]
        print("ki:" + ki)
        xi = plaintext[i]
        print("xi:"+xi)
        y += sigex((sigex(xi)+sigex(ki)) % 26)
        print("y:"+y+"\n")
    return y.upper()


# returns a list representation of the frequency table for the given ciphertext string
# sorted in ascending order by occurrence number
def freq(ciphertext):
    unsorted_table = {character.lower(): ciphertext.count(character) for character in set(ciphertext)}
    return sorted(unsorted_table.items(), key=operator.itemgetter(1), reverse=True)


def IC(x):
    frequency_table = freq(x)
    n = reduce(lambda a, b: a+b, [f_i[1] for f_i in frequency_table])
    return reduce(lambda a, b: a+b, [f_i[1]*(f_i[1]-1) for f_i in frequency_table])/(n*(n-1))


# returns a dictionary of all {substring: frequency} pairs found in the given ciphertext string
# for all substrings of length n
def most_common_substrings_length_n(ciphertext, n):
    f = {}
    for i in range(len(ciphertext)-(n-1)):
        curr = ciphertext[i:i+n]
        if curr in f.keys():
            f[curr] = f[curr]+1
        else:
            f[curr] = 1
    return f


# returns a list of all (substring,frequency) pairs sorted in ascending order by frequency over the entire ciphertext
def most_common_substrings(ciphertext):
    f = {}
    for i in range(1, len(ciphertext)):
        d = most_common_substrings_length_n(ciphertext, i)
        for k in d.keys():
            if k in f.keys():
                f[k] = f[k]+d[k]
            else:
                f[k] = d[k]
    return sorted(f.items(), key=operator.itemgetter(1), reverse=True)


# y = most_common_substrings(vigenere_ciphertext)
# print(y)
# for i in range(1, 30):
#     print(str(y[i]))
# print(str(len(y))+" distinct substrings")


def find_indices_of_most_common(findme, ciphertext):
    return [match.start() for match in re.finditer(findme, ciphertext)]

# print(find_indices_of_most_common(most_common, vigenere_ciphertext))


def find_key_length(most_common, ciphertext):
    indices_of_occurrence = find_indices_of_most_common(most_common, ciphertext)
    if len(indices_of_occurrence) <= 1:
        return "no maximal frequency"
    else:
        print(indices_of_occurrence)
        return reduce(gcd, [indices_of_occurrence[i]-indices_of_occurrence[0]
                            for i in range(1, len(indices_of_occurrence)-1)]) if len(indices_of_occurrence) > 2 else gcd(indices_of_occurrence[0], indices_of_occurrence[1])


def kasiski(ciphertext, n):
    ngram_freq = sorted(most_common_substrings_length_n(ciphertext, n).items(), key=operator.itemgetter(1),
               reverse=True)
    print(str(n)+"-grams = " + str(ngram_freq))
    print(str(len(ngram_freq)) + " distinct substrings of length " + str(n))
    most_common_ngram = ngram_freq[0][0]
    y = find_key_length(most_common_ngram, ciphertext)
    return y
    # print("m = " + str(y))




ciphertext1 = "Thisisenglishtext"  # should have an IC value closer to 0.065
ciphertext2 = "fkejshfcjlsieiohb"  # should have an IC value closer to 0.038

# ic1 = IC(ciphertext1)
# ic2 = IC(ciphertext2)

# print(ic1)
# print(ic2)

vigenere_ciphertext = "KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST"

unknown_ciphertext = "BNVSNSIHQCEELSSKKYERIFJKXUMBGYKAMQLJTYAVFBKVTDVBPVVRJYYLAOKYMPQSCGDLFSRLLPROYGESEBUUALRWXMMASAZLGLEDFJBZAVVPXWICGJXASCBYEHOSNMULKCEAHTQOKMFLEBKFXLRRFDTZXCIWBJSICBGAWDVYDHAVFJXZIBKCGJIWEAHTTOEWTUHKRQVVRGZBXYIREMMASCSPBNLHJMBLRFFJELHWEYLWISTFVVYFJCMHYUYRUFSFMGESIGRLWALSWMNUHSIMYYITCCQPZSICEHBCCMZFEGVJYOCDEMMPGHVAAUMELCMOEHVLTIPSUYILVGFLMVWDVYDBTHFRAYISYSGKVSUUHYHGGCKTMBLRX"


# kasiski(vigenere_ciphertext, 3)
# kasiski(unknown_ciphertext, 3)


n = len(vigenere_ciphertext)
m = kasiski(vigenere_ciphertext, 3)
print(n/m)

for i in range(m):
    y = ""
    for j in range(int(n/m)):
        y+= vigenere_ciphertext[i]

