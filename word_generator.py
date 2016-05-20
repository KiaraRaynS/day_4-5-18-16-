

def generate_random_word():
    import string
    import random
    with open("/usr/share/dict/words") as opened_file:
        list_of_words = opened_file.read()

    list_of_words = list_of_words.lower()
    for x in string.punctuation:
        list_of_words = list_of_words.replace(x, '')
    words_list = (list_of_words).split()

    user_mode = input("Would you like to play on Easy, Normal, or Hard? ")
    user_mode = user_mode.lower()
    easy = "easy"
    normal = "normal"
    hard = "hard"
    if user_mode == easy:
        words_list = [word for word in words_list if 4 < len(word) < 6]
        return(random.choice(words_list))
    elif user_mode == normal:
        words_list = [word for word in words_list if 6 < len(word) < 10]
        return(random.choice(words_list))
    elif user_mode == hard:
        words_list = [word for word in words_list if 10 < len(word)]
        return(random.choice(words_list))
