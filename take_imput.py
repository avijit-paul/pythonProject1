def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2','3']:
        choice = input('Please choose a input (0,1,2,3): ')
        if choice not in ['0','1','2','3']:
            print('Please choose a input (0,1,2,3): ')
        elif choice in ['0','1','2','3']:
            print("You have choosen a correct input")

    return choice

position_choice()