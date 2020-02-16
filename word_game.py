import random

word_doc = 'names.txt'


def open_word_list(text_file):
    """
    This functions input is a text file and returns a list of names
    from the text file.
    """
    global names, word_list
    print("\n=========== WORD GAME STARTED ==========\n")
    print("Reading Word List...Done!\n")
    try:
        word_list = open(text_file)
        names = word_list.read().split('\n')
    except FileNotFoundError as err:
        print("Word List not found :", err)
    finally:
        word_list.close()
    return names


def name_chooser(words):
    """
    :param list of words:
    :return random choice from list:
    """
    return random.choice(list(words))


def display_to_string(one_word):
    """
    Takes input a list
    returns a string
    """
    s_word = ""
    for char in one_word:
        s_word = s_word + char + ' '
    return s_word[:-1]


def trials_of_guess(guess, word, trials, blank_name):
    if guess not in word:
        for trial in range(trials-1, 0, -1):
            guess = input("Incorrect! You have " + str(trial) + " more chance :)\n")
            if guess in word:
                break
        print("Game Over \nYou Loose :(")
    else:
        while "_" in blank_name:
            print("Correct :)\n")
            index_of_guessed = word.find(guess)
            blank_name[index_of_guessed] = word[index_of_guessed]
            print(display_to_string(blank_name))
            guess = input("Enter Another Guess to continue:\n")
            if guess not in word:
                for trial in range(trials - 1, 0, -1):
                    guess = input("Incorrect! You have " + str(trial) + " more chance :)\n")
                    if guess in word:
                        break
                print("Game Over \nYou Loose :(")
            else:
                pass
    #print("You Win")


def start_game():
    trials = 3
    word = name_chooser(open_word_list(word_doc))
    print("\nI am thinking of a {} letter name\n".format(len(word)))
    blank_name = ("_ " * len(word)).split(' ')
    random_index = random.randint(0, len(word) - 1)
    blank_name[random_index] = word[random_index]
    print(display_to_string(blank_name))
    guess = input("Input guess of a letter in the word :)\n")
    trials_of_guess(guess, word, trials, blank_name)





start_game()
