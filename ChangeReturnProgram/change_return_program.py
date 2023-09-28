"""
    Penny(p)     -> 1, 2, 5, 10, 20, 50, £ 1, £ 2
    Banknotes(£) -> 5, 10, 20, 50

    V - 1. The users have to insert the price and the money given. 
    V - 2. Return the change with the minimun number of piece given to the client.
    
    Extension:
    V - 1. Figure out the change for the United States.
    V - 2. Creat a test part of the application that propose a random value for the
       price and the money given by the client. Next sum this two number for
       ceck if the program is correct.
       
"""
import copy
import random

# Ask for the two possible option of the program, the test enviroment wich 
# randomly generate the price and the money or the personal area that allows
# you to insert price and money given

print("This program allows you to calculate the change given to a client.\n"
      "The change is calculated using the less possible piece of money given.\n"
      "The program allows the usage of two enviroment, the test and the "
      "personal area.\n\n"
      "Personal area    : allows the users to input the price and the money given.\n"
      "Test enviroment  : generate randomly the price and the money given.\n")
    



print("Choose one of the two possible option:\n"
      "s : select your price\n"
      "t : test environment")

list_choice = ["T","t","S","s"]
while True:
    choice = input("---> ")
    if choice not in list_choice:
        print("Insert only one of the possible option")
    else:
        break

# =============================================================================
# Personal Area
# =============================================================================
if choice.lower() == "s":

    print("Insert the price of the product.")
    
    while True:
        price = input("---> ")
        if price.isnumeric() == False:
            print("Insert only number!")
        else:
            break
    
    print("Insert the money given")
    
    while True:
        money = input("---> ")
        if money.isnumeric() == False:
            print("Insert only number!")
        elif int(price) > int(money):
            print("Insert a number greater than the price!")
        else:
            break
# =============================================================================
# Test enviroment
# =============================================================================
if choice.lower() == "t":
    price = random.randint(0, 9999)
    while True:
        money = random.randint(0, 9999)
        if money > price:
            break
    
    print(f"The price of the product is: {price}")
    print(f"The money given are: {money}")
    
    

price = int(price)
money = int(money)
    
if price == money:
    print("There is no change!")
else:
    change = money - price
    change_final = copy.copy(change)

# Create a list with all the possible pieces of money.
list_cash = [50,20,10,5,2,1]
list_change = list()

# Select the number of pieces required for the change
for index, i in enumerate(list_cash):
    while True:
        if change >= list_cash[index]:
            change = change - list_cash[index]
            list_change.append(list_cash[index])
        else:
            break
        
count_50 = 0
count_20 = 0
count_10 = 0
count_5 = 0
count_2 = 0
count_1 = 0
    
for i in list_change:
    if i == list_cash[0]:
        count_50 = count_50 + 1
    if i == list_cash[1]:
        count_20 = count_20 + 1
    if i == list_cash[2]:
        count_10 = count_10 + 1
    if i == list_cash[3]:
        count_5 = count_5 + 1
    if i == list_cash[4]:
        count_2 = count_2 + 1
    if i == list_cash[5]:
        count_1 = count_1 + 1
    
print("\nThe change is composed by: \n"
      f"50 --> {count_50}\n"
      f"20 --> {count_20}\n"
      f"10 --> {count_10}\n"
      f"5  --> {count_5}\n"
      f"2  --> {count_2}\n"
      f"1  --> {count_1}\n"
      f"For a total of {change_final}\n")

# =============================================================================
# Convertion in dollar and money usage.
# =============================================================================
"""
Quarters : 25 cent (USA)
Dimes    : 10 cents(USA)
Nickels  : 5 cents (USA)
Pennies  : 1 cents (ENG)
"""

d_change = change_final * 0.78
print(f"The change of {change_final}£ correspond to {d_change}$ \n")

quarters = d_change / 0.25
dimes = d_change / 0.10
nickels = d_change / 0.05
pennies = change_final / 0.01

print("Here are some calculation with the dollar change and the pennies. Those"
      " are the number of that coin need for pay the change.\n"
      f"Quarters (USA) --> {quarters}\n"
      f"Dimes    (USA) --> {dimes}\n"
      f"Nickels  (USA) --> {nickels}\n"
      f"Pennies  (ENG) --> {pennies}")