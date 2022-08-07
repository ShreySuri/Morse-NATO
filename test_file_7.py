

counter = 4

elif counter == 4:

    check = False
    final_message = ""
    while check == False:
        print("")
        input_3 = input("Enter your message. Use ' ', '//', and '////' as neccesary. ")
        input_3 = input_3.lower()
        input_3 = input_3.split(" ")
        length = len(input_3)

        for i in range (0, length):
            
