input_1 = 0
accepted_val = ["1", "2", "3", "4", "5"]
counter = 0
while counter != 1:
    print("")
    print("To get the full Morse Code Alphabet, enter '1'. ")
    print("To get the full NATO Phonetic Alphabet, enter '2'. ")
    print("To encode a string into Morse Code, enter '3'. ")
    print("To decode a Morse Code message into a string, enter '4'. ")
    input_1 = input(print("To encode a string into the NATO Alphabet, enter '5'. "))
    counter = 0                
    for i in range (0, 5):
        if accepted_val[i] == input_1:
            counter = counter + 1
        else:
            toggle = True
        
