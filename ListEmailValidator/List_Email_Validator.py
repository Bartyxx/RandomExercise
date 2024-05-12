"""
    V - 2. Allow the users to select a file with a list of mail and ceck every mail in the file.
    
    Variable:
    list_mail -> List of the mail in a csv file.
    mail      -> A single mail in the list.\
    list_result -> The flag Correct/Incorrect.
    result    -> List of the mail + the flag Correct/Incorrect.
 
"""

# Open the csv file with the mail.
f = open("test.csv", "r")
list_mail = list()
for line in f:
    list_mail.append(line.rstrip("|n"))
    print(line.rstrip('\n'))

f.close()


list_result = list()

for mail in list_mail:
    countdot = 0
    countat = 0   
    iscorrect = True
        
    # Control the number of at in the mail.
    for i in mail:
        if i == "@":
            countat += 1
    
    # If the number of at is == 1 split the mail when the at is encoutered.
    if countat == 1:
        splitted_mail = mail.split("@")
        first_half = splitted_mail[0]
        second_half = splitted_mail[1]
        # Count the number of dot in the part after the at.
        for i in second_half:
            if i == ".":
                countdot += 1
                
    # If after the @ a dot exist the mail is splitted when the dot is
    # encountered.
    if countdot == 1:
        dot_split = second_half.split(".")
    
    
    # Control the presence of the at and the total len of the mail and the
    # len of every single part of the mail.
    if countat > 1:
        print("The mail contain more than one @ so it's invalid.")
        iscorrect = False
    elif countat < 1:
        print("The mail don't contain any @ so it's invalid.")
        iscorrect = False
    elif len(mail) < 3:
         print("The mail len us less than 3 so it's invalid.")
         iscorrect = False
    elif len(mail) > 319:
        print("The mail len is greater than 319 so it's invalid.")
        iscorrect = False
    if countat >= 1:
        if len(first_half) > 64:
            print("The mail username is greater than 64 so it's invalid.")
            iscorrect = False
        if len(second_half) > 254:
            print("The mail domain is greater tha 254 so it's invalid.")
            iscorrect = False
        if len(first_half) < 1:
            print("The mail username is shorter than 1 so it's invalid.")
            iscorrect = False
        if len(second_half) < 1:
            print("The mail domain is shorter than 1 so it's invalid.")    
            iscorrect = False
        if "." not in splitted_mail[1]:
            print("There is no dot after the @ so the mail is invalid")
            iscorrect = False

    # Control the presence before and after the dot.
    if countdot > 2:
        print("The mail contain two dot after the @ so it's invalid.")
        iscorrect = False
    if countdot >= 1:
        if len(dot_split[0]) < 1:
            print("The mail domain doesn't exist so the mail is invalid.")
            iscorrect = False
        if len(dot_split[1]) < 1:
            print("The mail co-damain have to exist.")
            iscorrect = False
        if len(dot_split[1]) > 5:
            print("The mail co-domain have to be shorter than 5.")
            iscorrect = False
         
    # Control withe space.               
    if " " in mail:
        print("The mail contain a wite space so it's invalid.")
        iscorrect = False
        
    if iscorrect == False:
        #print("The mail is incorrect")
        list_result.append("Incorrect")
        
    else:
        #print("The mail is correct")
        list_result.append("Correct")


result = zip(list_mail, list_result)
    
    
f = open("mail_ceck.txt", "r+")
list_str_mail = list()
f.write("Mail, ")
f.write("Status \n")
for i in result:
    j = str(i)    
    f.write(j)
    f.write("\n")
    print(i)

   
f.close()
