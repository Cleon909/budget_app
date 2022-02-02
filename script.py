from budget import Budget

working = 1
# i is the increment for the budget var names
i = 1
while working == 1:
    choice = int(input("What do you want to do?\nInput 1 to create a budget.\nInput 2 to add a budget.\nInput 3 to withdraw from a budget.\nInput 4 to transfer from one budget to another.\nInput 5 to print out the current balance of a budget.\nInput 6 to print out a list of all balances.\nInput 7 to print out an individual budget history.\nTo print out a history of all budgets choose 8:\nTo exit program choose 9:"))

if choice == 1:
    name = input("choose name for budget: ")
    amount = round(int(input("Initial amount in budget ")),2)
    name = Budget(input(name,amount))
    print(name)
elif choice ==2:
    which_budget = input("Which budget do you want to deposit to?: ")
    how_much = input("How much do you want to deposit?: ")
    which_budget.deposit(how_much)
elif choice ==3:
    which_budget = input("Which budget do you want to withdraw from?: ")
    how_much = input("How much do you want to withdraw?: ")
    which_budget.withdraw(how_much)
elif choice ==4:
    which_budget_from = input("Which budget do you want to transfer from?: ")
    which_budget_to = input("Which budget do you want to transfer to?: ")
    how_much = input("How much do you want to deposit?: ")
    which_budget_from.transfer_from_to(which_budget_to,how_much)
elif choice == 5:
    which_budget = input("Which budget do you want the balance of?: ")
    which_budget.print_balance()
elif choice == 6:
    Budget.print_all_balances()
elif choice == 7:   
    which_budget = input("Which budget do you want to get a history for?: ")
    which_budget.print_history()
elif choice == 8:
    Budget.print_total_history()
elif choice == 9:
    print("Goodbye!")
    Working = 0

