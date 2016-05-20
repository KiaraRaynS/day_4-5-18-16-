from word_generator import generate_random_word
random_word = generate_random_word()
print_number = len(random_word)


def get_user_response():
    user_answer = input("Guess a letter: ")
    return user_answer


def hang_man_game():
    begin_game_word = list("_" * print_number)
    count = 0
    incorrect_guesses = []
    correct_guesses = []
    while count <= 8:
        print("".join(begin_game_word))
        user_answer = get_user_response()
        remaining_guesses = "You have {} guesses remaining.".format(7 - count)
        print(incorrect_guesses)
        print(remaining_guesses)
        if len(user_answer) > 1:
            print("You may only guess single letters.")
        elif '_' not in begin_game_word:
            print("CONGRADULATIONS!")
            print("{} correctly guessed".format("".join(begin_game_word)).title())
            break
        elif user_answer in correct_guesses:
            print("You already guessed that")
        elif user_answer in incorrect_guesses:
            print("You already guessed that")
        elif user_answer in random_word:
            for letter_index, random_letter in enumerate(random_word):
                if random_letter == user_answer:
                    begin_game_word[letter_index] = user_answer
            print("Correct guess!")
            correct_guesses.append(user_answer)
        elif count == 7:
            print("Sorry, you did not guess all the word letters.")
            print(random_word)
            response = input("Would you like to play again? Y/N ")
            response = response.upper()
            play_again = "Y"
            if response == play_again:
                hang_man_game()
            break
        else:
            print("Sorry, that is incorrect")
            incorrect_guesses.append(user_answer)
            count += 1

play_question = input("Would you like to play a letter guessing game? Y/N ")
play_question = play_question.upper()
begin_game = "Y"
if play_question == begin_game:
    hang_man_game()
