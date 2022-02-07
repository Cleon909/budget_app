from budget import Budget

from os.path import exists

Budget.load_or_not()

working = True
while working == True:
    choice = ""
    while choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
        choice = input("\n\n\nWhat do you want to do?\nInput 1 to create a budget.\nInput 2 to deposit to a budget.\nInput 3 to withdraw from a budget.\nInput 4 to transfer from one budget to another.\nInput 5 to print out the current balance of a budget.\nInput 6 to print out a list of all balances.\nInput 7 to print out an individual budget history.\nInput 8 to print out a history of all budgets.\nInput 9 to print sum of all balances.\nInput 10 to exit program:  ")
        match choice:
            case "1" : Budget.create_budget()
            case "2" : Budget.get_input_for_deposit()
            case "3" : Budget.get_input_for_withdraw()
            case "4" : Budget.get_transfer_details()
            case "5" : Budget.balance_of_budget()
            case "6" : Budget.print_all_balances()
            case "7" : Budget.get_input_for_history()
            case "8" : Budget.print_total_history()
            case "9" : Budget.print_total_balance()
            case "10" : 
                Budget.save_state()
                working = False
                print("Goodbye!")

        
        
        
        
        
        
        
        