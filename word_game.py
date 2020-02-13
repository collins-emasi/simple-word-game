import random

word_doc = 'names.txt'


def open_word_list(text_file):
    """
    This functions input is a text file and returns a list of names
    from the text file.
    """
    global names, word_list
    print("\n=========== WORD GAME STARTED ==========")
    print("Reading Word List...Done!")
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


def get_input():
    char = input("Enter a Character: ")
    return char


def start_game():
    word = name_chooser(open_word_list(word_doc))
    print("\nI am thinking of a {} letter name".format(len(word)))
    blank_name = ("_ " * len(word)).split(' ')
    random_index = random.randint(0, len(word) - 1)
    blank_name[random_index] = word[random_index]
    print(display_to_string(blank_name))
    print("Fill in Black Spaces in the mysterious name")
    for times in range(len(word)):
        for i in range(4):
            char = get_input()
            if char in word:
                print('Correct :)')
                char_index = word.find(char)
                blank_name[char_index] = char
                display_to_string(blank_name)
            else:
                print("Incorrect :(")
                print("You have {} more chances".format(i))
            break

start_game()
