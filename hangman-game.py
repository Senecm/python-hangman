# Created Wed Dec 30 17:00 2020
# Author: Christian Laranjeira


import random

#dictionary = open("three_letter_words.txt", "r") # this clause is redundant
play = True
word_indicator = "_ "
lives = 6 # having this as a global variable with avoid trouble later

while play: # here, you dont need to put an '==' while play is equivilent
    #dictionary_list = open("hangman-dictionary.txt").readlines() # see below
    dict = open("three_letter_words.txt").readlines()
    line_num = int(len(dict))
    print(line_num)
    word_selection = random.randint(0,line_num)
    word = dict[word_selection]
    word_length = len(word)

    print("Guess the following word.\n Guess the correct letters and they will appear in in the spaces below.")
    print(word_indicator * word_length)
    player_guess = input("Please enter a vowel or consonant to see if it is in the word. ")
    
    
    # check = word_length
    # char_num = 0
    # guesses_left = word_length
    
    # while check > 0:
    #     if player_guess in word[char_num]:
    #         word_length -= char_num + 1
    #         print ()
           
    
    # if player_guess in word[0]:
    #     word_length -= 1
    #     print(word[0], word_indicator * word_length)
    # elif player_guess in word[1]:
    #     word_length -= 2
    #     print("_",word[1], word_indicator * word_length)
    # elif player_guess in word[2]:
    #     word_length -= 3
    #     print("_ _",word[2], word_indicator * word_length)


    #########################ADDITION##############################
    # The Proposed Logic (replacing above)
    if player_guess == word[0]:
        player_guess_two = input("Make a second guess: ")
        if player_guess_two == word[1]:
            player_guess_three = input("Make a third guess")
    elif player_guess == word[1]:
        player_guess_two = input("Make a second guess: ")
    elif player_guess == word[2]:
        player_guess_two = input("Make a second guess: ")
    elif player_guess == word[3]:
        player_guess_two = input("Make a second guess: ")
    else:
        lives - 1
    # for this to work, the player must define beforehand the word length
    

    play_check = input("Would you like to play again? (Y/N) ")
    if play_check == "n" or play_check == "N":
       play = False