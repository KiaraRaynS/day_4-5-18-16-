from word_generator import generate_random_word
random_word = generate_random_word()


def get_user_response():
    user_answer = input("Guess a letter: ")
    return user_answer


def hang_man_game():
    correct_guesses = []
    incorrect_guesses = []
    begin_game_word = ("_ " * len(random_word))
    count = 0
    print("_ " * len(random_word))

    while count <= 7:
        print(begin_game_word)
        get_user_response()
        remaining_guesses = "You have {} guesses remaining.".format(9 - count)
        if user_answer in random_word:
            letter_location = random_word.index(letter)
            begin_game_word.append(user_answer)[letter_location]
            print(remaining_guesses)
            print("Correct guess!")
        elif user_answer in correct_guesses:
            print("You already guessed that")
            print(remaining_guesses)
        elif user_answer in incorrect_guesses:
            print(remaining_guesses)
            print("You already guessed that")
        else:
            print("Sorry, that is incorrect")
            print(remaining_guesses)
            incorrect_guesses.append(user_answer)
            count += 1

hang_man_game()
