def user_choice():

    # Variables
    choice = 'WRONG'
    acceptable_range = range(1,11)
    within_range = False

    # Two conditions to check
    while choice.isdigit() == False or within_range == False:
        choice = input('Enter a number between 1 and 10: ')

        # check digit
        if choice.isdigit() == False:
            print("not a digit")

        # range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Out of acceptable range")
                within_range = False
        return int(choice)

user_choice()
