

counter = 4

if counter == 4:

    check = False
    final_message = ""
    while check == False:
        print("")
        input_3 = input("Enter your message. Use ' ' '//', and '////' as neccesary. ")
        input_3 = input_3.lower()
        input_3 = input_3.split(" ")
        length = len(input_3)

        for i in range (0, length):
            word = input_3[i]
            if word != "//" and word != "////":   
                word = list(word)
                len_word = len(word)
                for j in range (len_word):
                    for k in range (0, 28):
                        if word[j] == code[k]:
                            x = alphabet[k]
                            final_message = "%s%s" % (final_message, x)
                            check = True
                        else:
                            toggle = True

            else:
                if word == "//":
                    message_list = "%s%s" % (message_list, " ")
                    check = True
                elif word == "////":
                    message_list = "%s%s" % (message_list, ".")
                    check = True
                else:
                    print("Something went wrong. ")
    
