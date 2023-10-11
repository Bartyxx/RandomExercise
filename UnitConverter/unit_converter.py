"""
    Unit converter
    
    V - 1. Make a program that let the users insert the unit of measure of
           number inserted, the unit of transformation and of course the number
           to covert.
           To that for:
               V - temperature
               V - volume
               V - currency
               V - mass
"""

"""
This program let the user choose between varius convertion.
Every convertion propose three different unit of measure and it's possible 
to convert from a unit of measure to another.
A list of the unit of measure propose for every category:
-------------------------------------------------------------------------------
Temperature
-------------------------------------------------------------------------------
- Celsius
- Fahrenheit
- Kelvin

-------------------------------------------------------------------------------
Volume
-------------------------------------------------------------------------------
- Liter
- Cubic meter
- Milliliter

-------------------------------------------------------------------------------
Currency
-------------------------------------------------------------------------------
- Euro
- Dollar
- Renmibi

-------------------------------------------------------------------------------
Mass 
-------------------------------------------------------------------------------
- Gram
- Kilogram
- Pound

"""
print("Welcolme in this program wich the pourpose it's to convert unit.\n"
      "Insert the unit you want to convert considering the following menu.\n"
      "- Temperature: t\n"
      "- Volume:      v\n"
      "- Currency:    c\n"
      "- Mass:        m\n"
      )

list_possibility = "t","v","c","m"
while True:
    choice = input("---> ")
    if choice.lower() not in list_possibility:
        print("Insert only one of the possible option")
    else:
        break

# ============================================================================
# ============================================================================
# Temperature
# ============================================================================
# ============================================================================
if choice.lower() == "t":
    print("Choose the unit of measure of the number inserted:\n"
          "- Celsius:    c\n"
          "- Fahrenheit: f\n"
          "- Kelvin:     k\n")
    
    list_p_t = ["c","f","k"]
    while True:
        choice_t = input("---> ")
        if choice_t.lower() not in list_p_t:
            print("Insert one of the possible option")
        else:
            break

    print("Choose the unit of measure of conversion:\n"
          "- Celsius:    c\n"
          "- Fahrenheit: f\n"
          "- Kelvin:     k\n")
    
    while True:
        choice_tt = input("---> ")
        if choice_tt.lower() not in list_p_t:
            print("Insert one of the possible option")
        else:
            break
    
    print("Insert the number that need to be converted")
    while True:
        num_t = input("---> ")
        if num_t.isdecimal() == False:
            print("Insert only number!")
        else:
            break
        
    if choice_t == "c":
        degree_t = "Celsius"
    elif choice_t == "f":
        degree_t = "Fahrenheit"
    elif choice_t == "k":
        degree_t = "Kelvin"
    
    if choice_tt == "c":
        degree_tt = "Celsius"
    elif choice_tt == "f":
        degree_tt = "Fahrenheit"
    elif choice_tt == "k":
        degree_tt = "Kelvin"
        
    num_t = int(num_t)
    if choice_t == choice_tt:
        print(f"{num_t} {degree_t} correspond to {num_t} {degree_tt}")
    elif choice_t == "c" and choice_tt == "f":
        print(f"{num_t} {degree_t} correspond to {(num_t * (9/5)) + 32} {degree_tt}")
    elif choice_t == "c" and choice_tt == "k":
        print(f"{num_t} {degree_t} correspond to {num_t + 273,15} {degree_tt}")
    elif choice_t == "f" and choice_tt == "c":
        print(f"{num_t} {degree_t} correspond to {(num_t - 32) * (5/9)} {degree_tt}")
    elif choice_t == "f" and choice_tt == "k":
        print(f"{num_t} {degree_t} correspond to {(num_t - 32) * (5/9) + 273,15} {degree_tt}")
    elif choice_t == "k" and choice_tt == "c":
        print(f"{num_t} {degree_t} correspond to {num_t - 273,15} {degree_tt}")
    elif choice_t == "k" and choice_tt == "f":
        print(f"{num_t} {degree_t} correspond to {(num_t - 273,15) * (9/5) + 32} {degree_tt}")
        
# ============================================================================
# ============================================================================        
# Volume    
# ============================================================================
# ============================================================================  
elif choice.lower() == "v":
    print("Choose the unit of measure of the number inserted:\n"
          "- Liter:       l\n"
          "- Cubic meter: c\n"
          "- Milliliter:  m\n")
    
    list_p_v = "l","c","m"
    while True:
        choice_v = input("---> ")
        if choice_v.lower() not in list_p_v:
            print("Insert one of the possible option")
        else:
            break
        
    print("Choose the unit of measure of conversion::\n"
          "- Liter:       l\n"
          "- Cubic meter: c\n"
          "- Milliliter:  m\n")
    
    while True:
        choice_vv = input("---> ")
        if choice_vv.lower() not in list_p_v:
            print("Insert one of the possible option")
        else:
            break
    
    print("Insert the number that need to be converted")
    while True:
        num_v = input("---> ")
        if num_v.isdecimal() == False:
            print("Insert only number!")
        else:
            break
        
    if choice_v == "l":
        volume_v = "Liter"
    elif choice_v == "c":
        volume_v = "Cubic meter"
    elif choice_v == "m":
        volume_v = "Milliliter"
    
    if choice_vv == "l":
        volume_vv = "Liter"
    elif choice_vv == "c":
        volume_vv = "Cubic meter"
    elif choice_vv == "m":
        volume_vv = "Milliliter"
        
    num_v = int(num_v)
    if choice_v == choice_vv:
        print(f"{num_v} {volume_v} correspond to {num_v} {volume_vv}")
    elif choice_v == "l" and choice_vv == "c":
        print(f"{num_v} {volume_v} correspond to {num_v / 1000} {volume_vv}")
    elif choice_v == "l" and choice_vv == "m":
        print(f"{num_v} {volume_v} correspond to {num_v * 1000} {volume_vv}")
    elif choice_v == "c" and choice_vv == "l":
        print(f"{num_v} {volume_v} correspond to {num_v * 1000} {volume_vv}")
    elif choice_v == "c" and choice_vv == "m":
        print(f"{num_v} {volume_v} correspond to {num_v * 1000000000} {volume_vv}")
    elif choice_v == "m" and choice_vv == "l":
        print(f"{num_v} {volume_v} correspond to {num_v / 1000} {volume_vv}")
    elif choice_v == "m" and choice_vv == "c":
        print(f"{num_v} {volume_v} correspond to {num_v / 1000000000} {volume_vv}")
        
# ============================================================================
# ============================================================================  
# Currency
# ============================================================================
# ============================================================================
elif choice.lower() == "c":
    print("Choose the unit of measure of the number inserted:\n"
          "- Euro:    e\n"
          "- Dollar:  d\n"
          "- Renmibi: r\n")
    
    list_p_c = ["e","d","r"]
    while True:
        choice_c = input("---> ")
        if choice_c.lower() not in list_p_c:
            print("Insert one of the possible option")
        else:
            break
        
    print("Choose the unit of measure of conversion:\n"
          "- Euro:    e\n"
          "- Dollar:  d\n"
          "- Renmibi: r\n")
    
    while True:
        choice_cc = input("---> ")
        if choice_cc.lower() not in list_p_c:
            print("Insert one of the possible option")
        else:
            break
    
    print("Insert the number that need to be converted")
    while True:
        num_c = input("---> ")
        if num_c.isdecimal() == False:
            print("Insert only number!")
        else:
            break
        
    if choice_c == "e":
        curr_c = "Euro"
    elif choice_c == "d":
        curr_c = "Dollar"
    elif choice_c == "r":
        curr_c = "Renmibi"
    
    if choice_cc == "e":
        curr_cc = "Euro"
    elif choice_cc == "d":
        curr_cc = "Dollar"
    elif choice_cc == "r":
        curr_cc = "Renmibi"
        
    num_c = int(num_c)
    if choice_c == choice_cc:
        print(f"{num_c} {curr_c} correspond to {num_v} {curr_cc}")
    elif choice_c == "e" and choice_cc == "d":
        print(f"{num_c} {curr_c} correspond to {num_c * 1.11} {curr_cc}")
    elif choice_c == "e" and choice_cc == "r":
        print(f"{num_c} {curr_c} correspond to {num_c * 8} {curr_cc}")
    elif choice_c == "d" and choice_cc == "e":
        print(f"{num_c} {curr_c} correspond to {num_c * 0.90} {curr_cc}")
    elif choice_c == "d" and choice_cc == "r":
        print(f"{num_c} {curr_c} correspond to {num_c * 7.18} {curr_cc}")
    elif choice_c == "r" and choice_cc == "e":
        print(f"{num_c} {curr_c} correspond to {num_c * 0.13} {curr_cc}")
    elif choice_c == "r" and choice_cc == "d":
        print(f"{num_c} {curr_c} correspond to {num_c * 0.14} {curr_cc}")
        
# ============================================================================
# ============================================================================   
# Mass
# ============================================================================
# ============================================================================
elif choice.lower() == "m":
    print("Choose the unit of measure of the number inserted:\n"
          "- Gram:      g\n"
          "- Kilogram:  k\n"
          "- Pound:     p\n")
    
    list_p_m = "g","k","p"
    while True:
        choice_m = input("---> ")
        if choice_m.lower() not in list_p_m:
            print("Insert one of the possible option")
        else:
            break
        
    print("Choose the unit of measure of conversion:\n"
          "- Gram:      g\n"
          "- Kilogram:  k\n"
          "- Pound:     p\n")
    
    while True:
        choice_mm = input("---> ")
        if choice_mm.lower() not in list_p_m:
            print("Insert one of the possible option")
        else:
            break
    
    print("Insert the number that need to be converted")
    while True:
        num_m = input("---> ")
        if num_m.isdecimal() == False:
            print("Insert only number!")
        else:
            break
        
    if choice_m == "g":
        mass_m = "Gram"
    elif choice_m == "k":
        mass_m = "Kilogra"
    elif choice_m == "p":
        mass_m = "Pound"
    
    if choice_mm == "g":
        mass_mm = "Gram"
    elif choice_mm == "k":
        mass_mm = "Kilogram"
    elif choice_mm == "p":
        mass_mm = "Pound"
        
    num_m = int(num_m)
    if choice_m == choice_mm:
        print(f"{num_m} {mass_m} correspond to {num_v} {mass_mm}")
    elif choice_m == "g" and choice_mm == "k":
        print(f"{num_m} {mass_m} correspond to {num_m / 1000} {mass_mm}")
    elif choice_m == "g" and choice_mm == "p":
        print(f"{num_m} {mass_m} correspond to {num_m / 453.6} {mass_mm}")
    elif choice_m == "k" and choice_mm == "g":
        print(f"{num_m} {mass_m} correspond to {num_m * 1000} {mass_mm}")
    elif choice_m == "k" and choice_mm == "p":
        print(f"{num_m} {mass_m} correspond to {num_m * 2.205} {mass_mm}")
    elif choice_m == "p" and choice_mm == "g":
        print(f"{num_m} {mass_m} correspond to {num_m * 453.6} {mass_mm}")
    elif choice_m == "p" and choice_mm == "k":
        print(f"{num_m} {mass_m} correspond to {num_m / 2.205} {mass_mm}")
