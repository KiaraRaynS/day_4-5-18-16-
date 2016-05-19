import string
import random


def generate_random_word():
    with open("/usr/share/dict/words") as opened_file:
        list_of_words = opened_file.read()

    list_of_words = list_of_words.lower()
    for x in string.punctuation:
        list_of_words = list_of_words.replace(x, '')

    words_list = (list_of_words).split()
    print(words_list)
    random_word = (random.choice(words_list))
