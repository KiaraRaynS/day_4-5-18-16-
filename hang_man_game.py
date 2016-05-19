from word_generator import generate_random_word
random_word = generate_random_word()
print_number = len(random_word)
random_word = random_word.split()


def get_user_response():
    user_answer = input("Guess a letter: ")
    return user_answer


def hang_man_game():
    begin_game_word = ("_ " * print_number)
    count = 0
    while count <= 8:
        incorrect_guesses = []
        correct_guesses = []
        print(begin_game_word)
        user_answer = get_user_response()
        remaining_guesses = "You have {} guesses remaining.".format(7 - count)
        print(incorrect_guesses)
        print(remaining_guesses)
        if user_answer in random_word:
            for letter in random_word:
                letter_index = random_word.index(user_answer)
                begin_game_word[letter_index] = user_answer
            print("Correct guess!")
            correct_guesses = correct_guesses.append(user_answer)
        elif user_answer in correct_guesses:
            print("You already guessed that")
        elif user_answer in incorrect_guesses:
            print("You already guessed that")
        elif count == 7:
            print("Sorry, you did not guess all the word letters.")
            print(random_word)
            break
        else:
            print("Sorry, that is incorrect")
            incorrect_guesses = incorrect_guesses.append(user_answer)
            count += 1

hang_man_game()
