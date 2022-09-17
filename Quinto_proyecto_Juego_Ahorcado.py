# Initialize the game
def initialize_game():
    title1 = 'hangman game'.title()
    print(title1.center(50, " "))
    print(("-"*25).center(47, " "))
    print("\tYou have only 5 lives... :D")
    print("\tGuess the secret word. Good luck !!\n")


# Asking an option
def asking_option():
    option = 'z'
    while option not in "abc":
        option = input('Enter a letter to choose a secret word [a] [b] [c]: ')
    return option


# Selecting secret word
def selecting_sword(option):
    dict_words = {'a': 'gabriel', 'b': 'santana', 'c': 'martinez'}
    secret_word = dict_words[option]
    secret_word2 = list("_" * len(secret_word))
    secret_word2 = "".join(secret_word2)
    return secret_word, secret_word2


# Asking a letter
def asking_letter(secret_word_, lives_f):
    print(f"\n\nLives: {lives_f}")
    print("Your secret word is:\n\t\t" + secret_word_)
    user = input("Enter a letter: ")
    return user


# Creating word
def creating_word(letter_cw, s_word_f, s2_word_f):
    # print("sword ", s_word_f)
    # print("letter: " + letter_cw)
    # print("s2 word ", s2_word_f)
    for pos, letter2 in enumerate(s_word_f):
        if letter2 == letter_cw:
            s2_word_f = list(s2_word_f)
            s2_word_f[pos] = letter_cw
            s2_word_f = "".join(s2_word_f)
    return s2_word_f


# Testing letter
def testing_letter(s2_word, s2_word_, letter_tl, lives_f):

    s2_word = list(s2_word)
    if letter_tl in s2_word:
        if letter_tl in letter_used:
            print("letter duplicated")
            pass
        else:
            s2_word_ = creating_word(letter_tl, s2_word, s2_word_)
            letter_used.append(letter_tl)
            print(f"Letters used: {letter_used}")
    else:
        if letter_tl in letter_used:
            print("letter duplicated")
            pass
        else:
            letter_used.append(letter_tl)
            print(f"Letters used: {letter_used}")
            lives_f -= 1
    return lives_f, s2_word_


initialize_game()
s_word, s_word_ = selecting_sword(asking_option())
lives = 5
letter_used = []
while lives > 0:

    letter = asking_letter(s_word_, lives)
    lives, s_word_ = testing_letter(s_word, s_word_, letter, lives)
    # print("Testing" + s_word_)
    if lives == 0:
        print(f"\nLives: {lives}")
        print("YOU HAVE NO MORE LIVES  :(")
        print("\n\t\tGAME OVER.\n\t\tYOU LOOSED THE GAME\n\t\tTRY AGAIN :D")
    if "_" in s_word_:
        pass
    else:
        print("\n\t\t¡¡¡ YOU WIN THE GAME !!!")
        print(f"\n\t\tYour word was:\n\t\t\t{s_word_}")
        print(f"\n\t\t¡¡¡  CONGRATULATIONS  !!!\n\t\tLives: {lives}")
        lives = 0
