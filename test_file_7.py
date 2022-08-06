elif counter == 4:

    repeat = True
    final_message = ""
    while repeat == True:

        input_3 = ""
        while len(input_3) == 0:
            input_3 = input("Enter your message one letter at a time. Use '//' to seperate words and '////' as a period. Type 'done' when you are finished with the message.")
            input_3 = input_3.lower()

        if input_3 != "done":
            
            check = False
            for i in range (0, 28):
                if code[i] == input_3:
                    x = alphabet[i]
                    final_message = "%s%s" % (final_message, x)
                    
                    check = True
                else:
                    toggle = True

            if check == True:
                toggle = False
            else:
                final_message = "%s%s" % (final_message, "[unknown character]")
        else:
            repeat = False

    print(final_message)
