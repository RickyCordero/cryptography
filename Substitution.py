from functools import reduce
import operator


# returns the frequency table in list form for the given ciphertext string
def freq(ciphertext):
    unsorted_table = {character.lower(): ciphertext.count(character) for character in set(ciphertext)}
    return sorted(unsorted_table.items(), key=operator.itemgetter(1), reverse=True)


