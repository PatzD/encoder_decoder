import random
import re


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


    if check_special_character(word) == False or len(word) <= 3:  # if word contains a special character
        return word

    while True:
        first_letter, last_letter, inner_letters = (
            word[0],  # getting first
            word[len(word) - 1],  # getting last
            list(word[1 : len(word) - 1]),  # and middle letters of the word
        )
        random.shuffle(inner_letters)  # shuffling the middle letters

        scrambled_word = "".join(
            inner_letters
        )  # joining the letters from list to string
        scrambled_word = (
            first_letter + scrambled_word + last_letter
        )  # adding first and last letters back to string

        if scrambled_word != word:
            return scrambled_word


def encode_sentance(sentence):
    """Takes sentence, encodes each word in sentence where possible,
    returns encoded sentence andn original sentence sorted alphebetically"""

    sep = "\n-weird-\n"

    # lists to hold scrambled words and original words
    scrambled = []
    originals = []
    split_sentence = sentence.split(" ")

    for word in split_sentence:
        scrambled.append(scramble_word(word))
        originals.append(word)

    joined_sc = " ".join(scrambled)
    joined_or = " ".join(sorted(originals, key=str.lower))

    return sep, joined_sc, sep, joined_or


def decoder(encode, og_sorted):
    """Takes encoded sentence and original sorted sentence in string format,
    returns decoded sentence"""

    # splitting of strings into lists
    encoded = encode.split(" ")
    original_sorted = og_sorted.split(" ")

    # list to hold decoded words
    decoded_sentence = []

    # looping through encoded words and checking it the
    # encoded words have any matches in the original sorted words
    for word in encoded:
        for word2 in original_sorted:
            if len(word) == len(word2) and sorted(word) == sorted(word2):
                decoded_sentence.append(word2)
                original_sorted.remove(word2)

    decoded = " ".join(decoded_sentence)
    return decoded

print(encode_sentance("hello how are you doing"))
