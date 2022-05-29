import random
import os
from hang_wordlist import words
from hang_graphics import logo , stages

newline = '\n'
print(logo)
print(f"{newline}")


#Section 1 : Generate a random word from the given wordlist.
rand_word = random.choice(words)

#Section 2 : Generate a blank list with size = no of characters in the randomly generated word.
word_length = len(rand_word)
display = []
for _ in range(word_length) :
    display += "_"
print(display)
print(f"{newline}")

#Section 3 : Main Game block.
#Ask user to guess a letter and check if the letter is in the random chosen word.
#Loop iterates through the word and compares the letters of the word with the input given by the user
#When a match is found it replaces the blank space with the letter.

lives = 6
end_game = False 
while not end_game:
    letter_guess = input("Guess a letter : ").lower()
    os.system('clear')
    print(logo)
    print(f"{newline}")
    if letter_guess in display :                                            #Warning when user guesses the same letter.
        print(f"{newline}")
        print(f"You have already guessed {letter_guess}")               
    for position in range (0 , word_length) :                               #Display the correct letter in place of blank.
        letter = rand_word[position]
        if letter == letter_guess :
            display[position] = letter
    print(display)

    if "_" not in display :                                                 # Win condition. (when all blanks are filled without errors.)
        end_game = True 
        print("You win")


#Section 4 : Keep track of lives upon incorrect guess.
    if letter_guess not in rand_word :
        print(f"{newline}")
        print(f"You guessed {letter_guess} which is not in the word.")
        lives -= 1 
        print(f"Lives left = {lives} ")
        if lives == 0 :
            end_game = True
            print("You lose")
            print(f"The word was {rand_word}")    
    print(stages[lives])