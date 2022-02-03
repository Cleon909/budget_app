from budget import Budget
from os.path import exists

Budget.load_or_not()

working = True
while working == True:
    choice = ""
    while choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
        choice = input("\n\n\nWhat do you want to do?\nInput 1 to create a budget.\nInput 2 to deposit to a budget.\nInput 3 to withdraw from a budget.\nInput 4 to transfer from one budget to another.\nInput 5 to print out the current balance of a budget.\nInput 6 to print out a list of all balances.\nInput 7 to print out an individual budget history.\nInput 8 to print out a history of all budgets.\nInput 9 to print sum of all balances.\nInput 10 to exit program:  ")
        if choice == "1": #create a budget
            Budget.create_budget()
        elif choice == "2": #deposit to budget 
            Budget.get_input_for_deposit()
        elif choice == "3": #withdraw from budget
            Budget.get_input_for_withdraw()
        elif choice == "4": # transfer between accounts
            Budget.get_transfer_details()
        elif choice == "5": # balance of budget
            Budget.balance_of_budget()
        elif choice == "6": # print all balances
            Budget.print_all_balances()
        elif choice == "7": # history of budget
            Budget.get_input_for_history()
        elif choice == "8": # history of all budgets
            Budget.print_total_history()
        elif choice =="9": #add up balance of all budgets
            Budget.print_total_balance()
        elif choice == "10": # kill program and save state
            Budget.save_state()
            working = False
            print("Goodbye!")

