from evil_mode import evil_mode


def coin_flip():
    import random
    flip_coin = random.ranrange(1)
    return flip_coin


def generate_word_length():
    import random
    length_of_word = random.randrange(1, 13)
    return length_of_word


def get_user_response():
    response = input("Guess a letter: ")
    return response


def begin_game():
    user_response = input("Would you like to play Evil Hangman? Y/N ")
    user_response = user_response.lower()
    begin = "y"
    if user_response == begin:
        evil_mode()


def greatest_index_list():
    import operator
    occurances = {}
    for word in new_list:
        for idx, letter in enumerate(word):
            if response == letter:
                if idx in occurances.keys():
                    occurances[idx] += 1
                else:
                    occurances[idx] = 1
    sorted_index = sorted(occurances.items(), key=operator.itemgetter(1))
    common_index = sorted_index[:-2:-1]
    common_index_list = [k for k in common_index]
    true_index_tuple = common_index_list[0]
    index_final = true_index_tuple[0]
    return index_final
