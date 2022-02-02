from budget import Budget
from os.path import exists

Budget.check_for_save_file()

working = True
# i is the increment for the budget var names
i = 1
while working == True:
    choice = int(input("\n\n\nWhat do you want to do?\nInput 1 to create a budget.\nInput 2 to deposit to a budget.\nInput 3 to withdraw from a budget.\nInput 4 to transfer from one budget to another.\nInput 5 to print out the current balance of a budget.\nInput 6 to print out a list of all balances.\nInput 7 to print out an individual budget history.\nTo print out a history of all budgets choose 8:\nTo exit program choose 9:"))
    if choice not in range(1,10):
       choice = int(input("\n\n\nWhat do you want to do?\nInput 1 to create a budget.\nInput 2 to deposit to a budget.\nInput 3 to withdraw from a budget.\nInput 4 to transfer from one budget to another.\nInput 5 to print out the current balance of a budget.\nInput 6 to print out a list of all balances.\nInput 7 to print out an individual budget history.\nTo print out a history of all budgets choose 8:\nTo exit program choose 9:")) 
    elif choice == 1: #create budget
        Budget.list_budgets()
        name = input("choose name for budget: ")
        amount = round(int(input("Initial amount in budget ")),2)
        name = Budget(name,amount)
    elif choice ==2: #deposit to budget
        Budget.list_budgets()
        which_budget = input("Which budget do you want to deposit to?: ")
        if which_budget not in [x.name for x in Budget.budgets]:
            print("budget doesn't exist")
        else:
            how_much = round(int(input("How much do you want to deposit?: ")),2)
            for b in Budget.budgets:
                if which_budget == b.name:
                    b.deposit(how_much)
    elif choice ==3: #withdraw from budget
        Budget.list_budgets()
        which_budget = input("Which budget do you want to withdraw from?: ")
        if which_budget not in [x.name for x in Budget.budgets]:
            print("budget doesn't exist")
        else:
            how_much = round(int(input("How much do you want to withdraw?: ")),2)
            for b in Budget.budgets:
                if which_budget == b.name:
                    b.withdraw(how_much)
    elif choice ==4: # transfer between accounts
        Budget.list_budgets()
        which_budget_from = input("Which budget do you want to transfer from?: ")
        if which_budget_from not in [x.name for x in Budget.budgets]:
            print("budget doesn't exist")
        else:
            which_budget_to = input("Which budget do you want to transfer to?: ")
            if which_budget_to not in [x.name for x in Budget.budgets]:
                print("budget doesn't exist")
            else:
                how_much = round(int(input("How much do you want to deposit?: ")),2)
                for b in Budget.budgets:
                    if which_budget_from == b.name:
                        which_budget_from = b
                for g in Budget.budgets:
                    if which_budget_to == g.name:
                        which_budget_to = g
                which_budget_from.transfer_from_to(which_budget_to,how_much)
    elif choice == 5: # balance of budget
        Budget.list_budgets()
        which_budget = input("Which budget do you want the balance of?: ")
        if which_budget not in [x.name for x in Budget.budgets]:
            print("budget doesn't exist")
        else:
            for b in Budget.budgets:
                if which_budget == b.name:
                    b.print_balance()
    elif choice == 6: # print all balances
        Budget.print_all_balances()
    elif choice == 7: # history of budget
        Budget.list_budgets()
        which_budget = input("Which budget do you want to get a history for?: ")
        if which_budget not in [x.name for x in Budget.budgets]:
            print("budget doesn't exist")
        else:
            for b in Budget.budgets:
                if which_budget == b.name:
                    b.print_history()
    elif choice == 8: # history of all budgets
        Budget.print_total_history()
    elif choice == 9: # kill program and save state
        print("Goodbye!")
        Budget.save_state()
        working = False

