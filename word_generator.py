

def generate_random_word():
    import string
    import random
    with open("/usr/share/dict/words") as opened_file:
        list_of_words = opened_file.read()

    list_of_words = list_of_words.lower()
    for x in string.punctuation:
        list_of_words = list_of_words.replace(x, '')

    words_list = (list_of_words).split()
    return(random.choice(words_list))
