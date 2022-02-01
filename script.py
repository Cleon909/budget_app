from budget import Budget
budgets = []

# working = True

# while working:
#     choice = int(input("To create a budget choose 1:\nto add a budget choose 2\nTo withdraw froma budget choose 3:\n to transfer from one budget to another choose 4:\nTo print out an individual budget choose 5:\To print out a history of all budgets choose 6:\nTo exit program choose 9:"))


ent = Budget("entertainment", 350)
food = Budget("Food", 200)
trav = Budget("Travel", 100)
booze = Budget("Alcohol", 500)


ent.deposit(75.50)
food.withdraw(40)
food.transfer_from_to(booze,25.25)
booze.transfer_to_from(ent,0.73)
food.print_history()
booze.print_balance()

Budget.print_total_history()
Budget.print_total_balance()