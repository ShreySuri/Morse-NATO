elif counter == 4:

    repeat = True
    final_message = ""
    while repeat == True:

        check = False
        while check == False:
            print("")
            input_3 = input("Enter your message one letter at a time. Use '//', '////', and ' ' as needed. Enter 'done' when finished. ")
            input_3 = input_3.lower()

            for i in range (0, 28):
                if code[i] == input_3:
                    check = True
                    num = i
                else:
                    toggle = True

            if check == True:
                toggle = False
            elif input_3 == "done":
                check = True
            else:
                print("")
                print("Error - '%s' is not an accepted input. Please try again. " % input_3)

        if input_3 != "done":
            x = alphabet[num]
            final_message = "%s%s" % (final_message, x)
        else:
            repeat = False

    print(final_message)
        

        
