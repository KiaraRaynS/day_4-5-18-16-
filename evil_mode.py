from user_response import coin_flip
from user_response import generate_word_length
from user_response import get_user_response
from user_response import begin_game
from user_response import greatest_index_list


with open("/usr/share/dict/words") as opened_file:
    list_of_words = opened_file.read()
list_of_words = list_of_words.lower()
words_list = (list_of_words).split()


def evil_mode():
    word_length = generate_word_length()
    for word in words_list:
        possible_words = []
        if len(word) == word_length:
            possible_words = possible_words.append(word)
            return possible_words

    begin_word = list("_" * word_length)
    begin_count = 0
    correct_answers = []
    incorrect_answers = []
    while begin_count < 10:
        print(begin_word)
        response = get_user_response()
        coin_flip()
        if "_" not in begin_word:
            print("Congradulations! You defeated evil mode.")
        elif response in correct_answers:
            print("You already guessed that.")
        elif response in incorrect_answers:
            print("You aready guessed that.")
        elif coin_flip == True:
            for word in words_list:
                if response in word:
                    del(word)
                    return words_list
            print("Sorry, incorrect guess.")
            begin_count += 1
            incorrect_answers = incorrect_answers.append(response)
            return incorrect_answers
        else:
            new_list = []
            for word in words_list:
                if response in word:
                    new_list.append(word)
            response_index = greatest_index_list()



begin_game()
