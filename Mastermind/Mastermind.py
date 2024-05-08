"""
   Mastermind
   V - 1. Generate a random four digit number. 
   V - 2. The player has to keep inputting four digit numbers until they guess
          the randomly generated number. 
   V - 3. After each unsuccessful try it should say how many numbers they got 
      correct, but not which position they got right. 
   V - 4. At the end of the game should congratulate the user and say how many 
      tries it took.
      
   Extensions:
   V - 1. Let the user pick an easy mode which shows the user which position 
          that they guessed correctly
   V - 2. Let the user pick a hard mode that gives five digits instead of four
   V - 3. After the game is finished, ask the user for their name and input 
          their score into a table. Show them the high score at the start of 
          the game so that it gives a sense of competition.
"""
# ============================================================================
# ============================================================================
# ============================================================================
# ============================================================================
import random
import pandas as pd

print("-" * 97)
print("-" * 97)
print("-" * 97)
print("Welcome to the game!")
print("-" * 97)
print("-" * 97)
print("-" * 97)      
print("The pourpose it's to guess the right number in one of three possible difficulties")
   
# Select the top plaer, so the one with the hightest score == 1      
score_result = pd.read_csv("score.txt", sep = ",", names=["Users", "Score"], on_bad_lines='skip')
ordered_score = score_result.sort_values(by=["Score"])
    
top = score_result["Score"] == 1
filtered = score_result[top]

# ============================================================================

print("-" * 97)      
print("Here they are the best score ever recorded in this game!")

# Print the Player with the highest score
print(filtered)

# Choose the three game difficulties
print("""
Choose the mode you woul'd like to play:
Easy   --> press a
Normal --> press b
Hard   --> press c
      """)
print("When you are inside the game print stop for exit the game")
print("-" * 45)

while True:
    choice = input()
    option = ["a", "b", "c", "A", "B", "C"]
    if choice not in option:
        print("Insert a valid option")
    if choice in option:
        break
# ============================================================================
# ============================================================================
# ============================================================================

if choice == "a" or choice == "A":
# Easy mode, in thi case the number that the user's have to guess have only 4
# digits and the program suggest the right or wrong position.
    num = random.randint(1000,9999)
    attempts = 0
    
    while True:
        attempts += 1
        print("Guess the number! -->")
        answer = input() 
        answer = int(answer)
        if answer == "stop":
            finish = False
            break
        if answer < 1000:
            print("Insert number greater then 1000")
        answer = str(answer)
        if answer.strip().isdigit() == False:
            print("Insert only number!")
        elif len(answer) != 4:
            print("The len of the number have to be 4")
        elif answer.strip().isdigit() == True and len(answer) == 4:
            answer = int(answer)
            if num == answer:
                print("Nice, the number you have inserted is equal to the random number! Good job!")
                print(f"Number of attempts {attempts}")
                finish = True
                break
            else:
                print("The number is different!")
                num_str = str(num)
                answer_str = str(answer)
                count = 0
                countglob = 0
                num_list = list(num_str)
                answer_list = list(answer_str)
                for i, j in zip(num_list, answer_list):
                    countglob += 1
                    if i == j:
                        count += 1
                        print(f"The number match in {countglob} position")
                print(f"The right digits are: {count}")

if choice == "b" or choice == "B":
# Normal mode, in this case the number that the user's have to guess have 
# only 4 digits and the program don't suggest the right or wrong position.
    num = random.randint(1000,9999)
    attempts = 0

    while True:
        attempts += 1
        print("Guess the number! -->")
        answer = input()  
        answer = int(answer)
        if answer == "stop":
            finish = False
            break
        if answer < 1000:
            print("Insert number greater then 1000")
        answer = str(answer)
        if answer.strip().isdigit() == False:
            print("Insert only number!")
        elif len(answer) != 4:
            print("The len of the number have to be 4")
        elif answer.strip().isdigit() == True and len(answer) == 4:
            answer = int(answer)
            if num == answer:
                print("Nice, the number you have inserted is equal to the random number! Good job!")
                print(f"Number of attempts {attempts}")
                finish = True
                break
            else:
                print("The number is different!")
                num_str = str(num)
                answer_str = str(answer)
                count = 0
                num_list = list(num_str)
                answer_list = list(answer_str)
                for i, j in zip(num_list, answer_list):
                    if i == j:
                        count += 1
                print(f"The right digits are: {count}")
        
if choice == "c" or choice == "C":
# Hard mode, in this case the number that the user's have to guess have 5  
# digits and the program don't seggest the right or wrong position.
    num = random.randint(10000,99999)
    attempts = 0
    print(num)
    while True:
        attempts += 1
        print("Guess the number! -->")
        answer = input()
        answer = int(answer)
        if answer == "stop":
            finish = False
            break
        if answer < 10000:
            print("Insert number greater than 10000")
        answer = str(answer)
        if answer.strip().isdigit() == False:
            print("Insert only number!")
        elif len(answer) != 5:
            print("The len of the number have to be 5")
        elif answer.strip().isdigit() == True and len(answer) == 5:
            answer = int(answer)
            if num == answer:
                print("Nice, the number you have inserted is equal to the random number! Good job!")
                print(f"Number of attempts {attempts}")
                finish = True
                break
            else:
                print("The number are different!")
                num_str = str(num)
                answer_str = str(answer)
                count = 0
                num_list = list(num_str)
                answer_list = list(answer_str)
                for i, j in zip(num_list, answer_list):
                    if i == j:
                        count += 1
                print(f"The right digits are: {count}")

# ============================================================================
# When the game is win the complete list of the players is printed.       
if finish == True:
    print(choice)
    if choice == "a" or choice == "A":
        choice = "Easy"
    elif choice == "b" or choice == "B":
        choice = "Medium"
    elif choice == "c" or choice == "C":
        choice = "Hard"
        
    # Open a file and insert the three information of username, score and 
    # difficulties selected in the game.
    name = input("Insert your name -> ")
    f = open("score.txt", "a")
    a = str(attempts)
    f.write(f"{name}, ")
    f.write(f"{a},")
    f.write(f"{choice} \n")
    f.close()
    
    # Ask for printing the result with the leatest game
    while True:
        ask = input("Do you want to visualize the new top score? y/n ")
        if ask != "y" or ask != "Y" or ask != "n" or ask != "N":
            print("Inset a valid option")
        if ask == "y" or ask == "Y":
            print(filtered)
            break
        if ask == "n" or ask == "N":
            break
