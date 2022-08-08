

counter = 4

if counter == 4:

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


            

   

            
