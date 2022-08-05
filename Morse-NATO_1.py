input_1 = 0
accepted_val = ["1", "2", "3", "4", "5"]
counter = None
while counter == None :
    print("")
    print("To get the full Morse Code Alphabet, enter '1'. ")
    print("To get the full NATO Phonetic Alphabet, enter '2'. ")
    print("To encode a string into Morse Code, enter '3'. ")
    print("To decode a Morse Code message into a string, enter '4'. ")
    input_1 = input(print("To encode a string into the NATO Alphabet, enter '5'. "))            
    for i in range (0, 5):
        if accepted_val[i] == input_1:
            counter = i + 1
        else:
            toggle = True

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
if counter == 1 or counter == 3 or counter == 4:
    code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
elif counter == 2 or counter == 5:
    code = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
else:
    print("Something went wrong.")


if counter == 1:
    print("")
    for i in range (0, 26):
        x = alphabet[i]
        x = x.upper()
        y = code[i]
        string = "%s    %s" % (x, y)
        print(string)
        
elif counter == 2:
    print("")
    for i in range (0, 26):
        x = alphabet[i]
        x = x.upper()
        y = code[i]
        string = "%s  --  %s" % (x, y)
        print(string)
        
elif counter == 3:
    input_2 = ""
    while len(input_2) == 0:
        input_2 = input(print("Enter your message. "))
        input_2 = input_2.lower()
        word_count = len(input_2)
        message_string = ""
        
    for i in range (0, word_count):
        word = input_2[i]
        word = list(word)
        letter_count = len(word)
            
        for j in range (0, letter_count):
            check = False
            for k in range (0, 26):
                if word[j] == alphabet[k] or word[j] == alphabet[k].upper():
                    message_string = "%s%s " % (message_string, code[k])
                    check = True
                else:
                    toggle = True
                        
            if check == False:
                message_string = "%s%s " % (message_string, "[unknown character]")
            else:
                toggle = False

    if i + 1 < word_count:
        message_string = "%s%s " % (message_string, "//")
    else:
        message_string = "%s%s" % (message_string, "////")
        print(message_string)
