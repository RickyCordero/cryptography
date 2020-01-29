from functools import reduce
import operator


def freq(ciphertext):
    """
    Returns the frequency table in list form for the given ciphertext string
    """
    unsorted_table = {character.lower(): ciphertext.count(character) for character in set(ciphertext)}
    return sorted(unsorted_table.items(), key=operator.itemgetter(1), reverse=True)


