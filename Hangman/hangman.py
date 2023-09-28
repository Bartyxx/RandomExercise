"""
    Hangman
        V - 1. Create a version of the hangman using list.
        V - 2. Ask in input for the word and the chances.
        V - 3. If the letter is incorrect notice that to the users.
        V - 4. If the letter is correct replace the position in the word.
        V - 5. Show the chance left.
    
    Extension
        V - 1. If they guess a lettere that they have alredy guessed the users 
               shouldn't lose a life.
 
"""

print("This is the Hangman game.\n")

print("Insert the word that the player have to guess")

# Ask for the word
while True:
    word = input("---> ")
    if word.isalpha() == False:
        print("Please insert only letter")
    elif len(word) == 1:
        print("Insert more than one letter")
    else:
        break
    
print("Insert the number of chances")

# Ask for the chances
while True:
    chances = input("---> ")
    if chances.isnumeric() == False:
        print("Please insert only number")
    elif chances == 0:
        print("Please insert a number greater than 0 ")
    else:
        break
    
# Cast the str to a list
l_word = list(word)

# =============================================================================
# =============================================================================
# =============================================================================

wrong_letter = list()
right_letter = list()
to_guess = list()

print("\n")
print("=" * 84)
print("Now the game begin!\n"
      f"The len of the word you have to guess is {len(word)}, you have "
      f"{chances} chances\n\n"
      "Insert a letter")
print("=" * 84)

# Create a list with the same len of the word but with _ instead of the letter
for i in range(0, len(l_word)):
    to_guess.append("_")
    
# =============================================================================
# Ask for the letter in input and relatives control.
# =============================================================================
while True:
    print(f"\nThe remaining chances are: {chances}")
    letter = input("---> ")
    # Control if the value in input of the users are right.
    if len(letter) > 1:
        print("Insert only one letter")
    elif letter.isalpha() == False:
        print("Insert only letter")
    else:
        # Populate the list if the letter chose is right with no duplication
        if letter in l_word:
            print("The letter is right!")
            if letter not in right_letter:
                right_letter.append(letter)
            print(f"The right letter are: {right_letter}")
                    
            for index, i in enumerate(l_word):
                if i == letter:
                    to_guess[index] = letter
            
            print(to_guess) 
            
        # Populate the list with the wrong letter if it's wrong with no 
        # duplication
        elif letter not in l_word:
            print("The letter was wrong, you have lost one life!")
            if letter not in wrong_letter:
                wrong_letter.append(letter)
                chances = int(chances) - 1
            print(f"The wrong letter are: {wrong_letter}")
        
        # Lose 
        if chances == 0:
            print("You have lose!")
            break
        
        # Win
        if "_" not in to_guess:
            print("=" * 84)
            print("\nYou have won!\n")
            print("=" * 84)
            break
    print("=" * 84)