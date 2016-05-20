import random
with open("/usr/share/dict/words") as opened_file:
    list_of_words = opened_file.read()
list_of_words = list_of_words.lower()
words_list = (list_of_words).split()


def evil_mode():
