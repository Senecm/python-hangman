# Created Wed Dec 30 17:00 2020
# Author: Christian Laranjeira


import random

dictionary = open("hangman-dictionary.txt", "r")
play = True
word_indicator = "_ "

while play == True:
    dictionary_list = open("hangman-dictionary.txt").readlines()
    line_num = int(len(dictionary_list))
    word_selection = random.randint(0,line_num)
    word = dictionary_list[word_selection]
    word_length = len(word)
    guess_num = 6

    print("Guess the following word.\n Guess the correct letters and they will appear in in the spaces below.")
    print(word_indicator * word_length)
    player_guess = input("Please enter a vowel or consonant to see if it is in the word. ")
    
    '''
    check = word_length
    char_num = 0
    guesses_left = word_length
    
    while check > 0:
        if player_guess in word[char_num]:
            word_length -= char_num + 1
            print ()
    '''        
 
    if player_guess in word[0]:
        word_length -= 1
        print(word[0], word_indicator * word_length)
    elif player_guess in word[1]:
        word_length -= 2
        print("_",word[1], word_indicator * word_length)
    elif player_guess in word[2]:
        word_length -= 3
        print("_ _",word[2], word_indicator * word_length)
    

    play_check = input("Would you like to play again? (Y/N) ")
    if play_check == "n" or play_check == "N":
       play = False