import random
from random_word import RandomWords
r = RandomWords()
import string
def get_valid_words(r):
    word = random.choice(r) #random chooses something from list
    while '-' in word or ' 'in word: #while word has dash or space, its True, will keep choosing a word until it is not True
        word = random.choice(r)

    return word
def hangman():
    word = get_valid_words(r)
    word_letters = set(r) #saves all letters in the word as a set, help keep track what has already been guessed
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #empty set to keep track of what users have guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives>0:
        #letters used
        #.join(used_letters) -> seperate the used letters in a string with a space
        print("You have", lives, "lives left and you have used these letters: ',' ".join(used_letters))

        #tell user what current word is (W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", " ".join(word_list))

        user_letter = input("Guess a letter: ")
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives-1 #take away a life
                print("Letter is not in word.")


        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    #gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("Sorry you died, the word was", word)
    else:
        print("You guessed the word", word, "correctly!")

    