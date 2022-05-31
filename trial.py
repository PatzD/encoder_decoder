import random
import re
from tabnanny import check

sentence = "There are a lot of (leaves) on a tree"
word = "spaghetti'"


def check_special_character(word):
    """check if word contains special characters and
    returns either true or false"""

    regex = re.compile("[@!#$%^&*()<>?/|}{~:]")  # special characters to check for
    if regex.search(word) == None:
        return True  # accept string, special characcterr not found

    else:
        return False  # special character present, return False


def scramble_word(word):
    """Takes in a word, and returns the word with the
    inner letters reordered randomly leaving two outermost
    letters in their original position if possible"""

    if check_special_character(word) == False:
        return word

    if len(word) > 3:
        first_letter, last_letter, word = (
            word[0],
            word[len(word) - 1],
            list(word[1 : len(word) - 1]),
        )
        random.shuffle(word)

        word = "".join(word)
        word = first_letter + word + last_letter

        return word

    return word


def encode_sentance(sentence):
    """Takes sentence, encodes each word in sentence where possible,
    returns encoded sentence andn original sentence sorted alphebetically"""

    scrambled = []
    originals = []
    split_sentence = sentence.split(" ")

    for word in split_sentence:
        scrambled.append(scramble_word(word))
        originals.append(word)

    return scrambled, sorted(originals, key=str.lower)


encoded = ["Three", "are", "a", "lot", "of", "leaves", "on", "a", "tree"]
or_sorted = ["a", "a", "are", "leaves", "lot", "of", "on", "There", "tree"]


def decoder(encoded, original_sorted):

    decoded_sentence = []
    for word in encoded:
        for word2 in original_sorted:
            if len(word) == len(word2) and sorted(word) == sorted(word2):
                decoded_sentence.append(word2)
                original_sorted.remove(word2)
    return decoded_sentence


print(decoder(encoded, or_sorted))
# a = ["as", "asd", "sdsd"]
# a = "".join(a)
# print(a)
