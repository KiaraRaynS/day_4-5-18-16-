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
