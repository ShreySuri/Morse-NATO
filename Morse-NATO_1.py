input_1 = 0
accepted_val = ["1", "2", "3", "4", "5"]
counter = None
while counter == None :
    print("")
    print("To get the full Morse Code Alphabet, enter '1'. ")
    print("To get the full NATO Phonetic Alphabet, enter '2'. ")
    print("To encode a string into Morse Code, enter '3'. ")
    print("To decode a Morse Code message into a string, enter '4'. ")
    input_1 = input("To encode a string into the NATO Alphabet, enter '5'. ")            
    for i in range (0, 5):
        if accepted_val[i] == input_1:
            counter = i + 1
        else:
            toggle = True

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "."]
if counter == 1 or counter == 3 or counter == 4:
    code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "//", "////"]
elif counter == 2 or counter == 5:
    code = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu", "//", "////"]
else:
    print("Something went wrong.")


if counter == 1:
    print("")
    for i in range (0, 28):
        x = alphabet[i]
        x = x.upper()
        y = code[i]
        string = "'%s'   %s" % (x, y)
        print(string)
        
elif counter == 2:
    print("")
    for i in range (0, 28):
        x = alphabet[i]
        x = x.upper()
        y = code[i]
        string = "'%s' --  %s" % (x, y)
        print(string)
        
elif counter == 3 or counter == 5:
    input_2 = ""
    while len(input_2) == 0:
        input_2 = input("Enter your message. Use spaces and periods as neccesary. Do not use any other punctuation. ")
        input_2 = input_2.lower()
        
    message_list = list(input_2)
    length = len(message_list)
    final_message = ""

    for i in range (0, length):
        check = False
        for j in range (0, 28):
            if message_list[i] == alphabet[j]:
                final_message = "%s%s " % (final_message, code[j])
                check = True
            else:
                toggle = True

        if check == False:
            final_message = "%s%s " % (final_message, "[unknown character]")
        else:
            toggle = False

    print(final_message)

elif counter == 4:

    check = False
    final_message = ""
    while check == False:
    
        print("")
        input_3 = input("Enter your message. Use ' ', '//', and '////' as neccesary. ")
        input_3 = input_3.lower()
        input_3 = input_3.split(" ")
        length = len(input_3)

        check_count = 0
        for i in range (0, length):
            for j in range (0, 28):
                if input_3[i] == code[j]:
                    check_count = check_count + 1
                else:
                    toggle = True

        if check_count == length:
            check = True
        else:
            print("")
            print("Sorry, you have entered one or more unknown/incorrect characters. Please try again.") 
            toggle = False

    for i in range (0, length):
        for j in range (0, 28):
            if input_3[i] == code[j]:
                x = alphabet[j]
                final_message = "%s%s" % (final_message, x)
            else:
                toggle = True

    print(final_message)


            

   

            
