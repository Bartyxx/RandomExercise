"""
    RPG Character/Pokemon stat creator
    V - 1. Make a program that create random value for the stat set by the users.
       The stat are:
           1. Class
           2. Gender
           3. Strenght/magic/dexterity
           4. Extra abilities or trades
    V - 2. Print the result into a file.
    
    Extension
    V - 1. Make a mytical name generator.
        1. Randomize different name parts.
        2. Associate every name to a character.

    Variables:
    c_class --> Class choose by the users.
    c_gender --> Gender choose by the users.
"""

# ============================================================================
# ============================================================================
# ============================================================================
import random

# Ask the users they preferencies.
print("Welcome in this new adventure traveler! Before begin with this magic "
      "and new adventure I have to ask you some question for create you "
      "character! Please answer correctily and remember that every character " 
      "can be usefoul in it's own way!\n")
print("=" * 84)

while True:
    # Define the class
    print("Do you valuate more phisical strenght, agility or intellectual power?\n"
          "s --> strenght\n"
          "a --> agility\n"
          "i --> intellectual power")
    c_class = input("--->  ")
    p_class = ["s","S","a","A","i","I"]
    if c_class in p_class:
        break
    else:
        print("\n\nInsert only one of the possible option!")
print("=" * 84)

while True:
    # Gender
    print("\nIn what you identify? Male, Female or Other?\n"
          "m --> male\n"
          "f --> female\n"
          "o --> other")
    c_gender = input("--->  ")
    p_gender = ["m","M","f","F","o","O"]
    if c_gender in p_gender:
        break
    else:
        print("\n\nInsert only one of the possible option")
        
           
w_poss = ["s","S"]
r_poss = ["a","A"]
m_poss = ["i","I"]
        
m_poss = ["m","M"]
f_poss = ["f","F"]
o_poss = ["o","O"]        
        
# ============================================================================
# ============================================================================
# ============================================================================
# Assign the name of the class and the gender and the relative bonus.

strenght = 0
dexterity = 0
magic = 0
s_ability = False
d_ability = False
m_ability = False
   
if c_class in w_poss:
    strenght += 15
    ch_class = "Warrior"
elif c_class == "a" or c_class == "A":
    dexterity += 15
    ch_class = "Ranger"
elif c_class == "i" or c_class == "I":
    magic += 15
    ch_class = "Mage"
    
if c_gender == "m" or c_gender == "M":
    strenght += 10
    gender = "Male"
if c_gender == "f" or c_gender == "F":
    dexterity += 10
    gender = "Female"
if c_gender == "o" or c_gender == "O":
    dexterity += 10
    gender = "Other"
    
# ============================================================================
# Assign a random value at every indicator, and assign the special ability if
# the indicator is >= 70.
    
ming = 0
maxg = 45
if c_class in w_poss and c_gender in m_poss:
    ming += 10
    maxg += 10
    s_adder = random.randint(ming, maxg)
else:
    s_adder = random.randint(ming, maxg)
strenght += s_adder    
    
if c_class in r_poss and c_gender in f_poss:
    ming += 10
    maxg += 10    
    d_adder = random.randint(ming, maxg)
else:
    d_adder = random.randint(ming, maxg)
dexterity += d_adder    
    
if c_class in m_poss and c_gender in o_poss:
    ming += 10
    maxg += 10
    m_adder = random.randint(ming, maxg)
else:
    m_adder = random.randint(ming, maxg)
magic += m_adder

if strenght >= 70:
    s_ability = True
if dexterity >= 70:
    d_ability = True
if magic >= 70:
    m_ability = True    
    
# ============================================================================
# Random name generator
    
list_name_first = ["o", "a", "se", "ne", "s"]
list_name_second = ["di", "de", "i", "ze"]
list_name_third = ["no", "po", "do", "u"]
first_choice  = random.randint(0, len(list_name_first)-1)
second_choice = random.randint(0, len(list_name_second)-1)
third_coiche  = random.randint(0, len(list_name_third)-1)

name = list_name_first[first_choice] + list_name_second[second_choice] + list_name_third[third_coiche]
    
print("\n")
   
extension = ".txt"


f = open(name + extension, "w")
f.write(f"Name: {name}\n"
        f"Class: {ch_class}\n"
        f"Gender: {gender}\n"
        f"Strenght: {strenght}\n"
        f"Dexterity: {dexterity}\n"
        f"Magic: {magic}\n"
        f"Strenght ability: {s_ability}\n"
        f"Dexterity ability: {d_ability}\n"
        f"Magic ability: {m_ability}")
f.close()


print(f"Congraturation! You have just build a character!\n"
      f"The name is: {name}\n"
      "The stats are:\n"
      f"Class: {ch_class}\n"
      f"Gender: {gender}\n"
      f"Strenght: {strenght}\n"
      f"Dexterity: {dexterity}\n"
      f"Magic: {magic}\n"
      f"Strenght ability: {s_ability}\n"
      f"Dexterity ability: {d_ability}\n"
      f"Magic ability: {m_ability}"      )


