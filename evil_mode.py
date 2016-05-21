from user_response import coin_flip
from user_response import generate_word_length
from user_response import get_user_response


with open("/usr/share/dict/words") as opened_file:
    list_of_words = opened_file.read()
list_of_words = list_of_words.lower()
words_list_a = (list_of_words).split()
words_list = words_list_a

def evil_mode():
    word_length = generate_word_length()
    for word in words_list:
        possible_words = []
        if len(word) == word_length:
            possible_words = possible_words.append(word)
            return possible_words
    words_list = possible_words

    begin_word = list("_" * word_length)
    begin_count = 0
    correct_answers = []
    incorrect_answers = []
    while begin_count < 10:
        print(begin_word)
        print(correct_answers)
        print(incorrect_answers)
        response = get_user_response()
        coin_flip()
        if "_" not in begin_word:
            print("Congradulations! You defeated evil mode.")
        elif begin_count == 9:
            print("Sorry, you failed to guess the word.")
            print("Possible words left: {}".format(words_list))
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
            import operator
            new_list = []
            list_with_index = []
            for word in words_list:
                if response in word:
                    new_list.append(word)
            occurances = {}
            for word in new_list:
                for idx, letter in enumerate(word):
                    if response == letter:
                        if idx in occurances.keys():
                            occurances[idx] += 1
                        else:
                            occurances[idx]
            sorted_index = sorted(occurances.items(), key=operator.itemgetter(1))
            common_index = sorted_index[:-2:-1]
            common_index_list = [k for k in common_index]
            true_index_tuple = common_index_list[0]
            index_final = true_index_tuple[0]
            response_index = index_final

            for word in new_list:
                if response in word[response_index]:
                    list_with_index.append(word)
                    return list_with_index
                words_list = list_with_index
                begin_word = begin_word[response_index].append(response)


begin_game = 'y'
user_response = input("Would you like to play Evil Mode? Y/N ").lower
if user_response == begin_game:
    evil_mode()
