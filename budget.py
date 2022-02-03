from os.path import exists
import ast
import pdb

class Budget():

    budgets_history = []
    budgets = []

    def __init__(self, name, balance=0, history=None):
        self.name = name
        self.balance = round(balance,2)
        self.history = history
        self.__class__.budgets.append(self)
   
    def create_budget():
        Budget.list_budgets()
        name = input("choose name for budget: ")
        while name in (x.name for x in Budget.budgets):
            print("name taken")
            name = input("choose name for budget: ")
        amount = round(float(input("Initial amount in budget: ")),2)
        name = Budget(name,amount)

    def __repr__(self):
        return f"There is £{self.balance} in the {self} budget. If you want a print of the history use history method."

    def deposit_to_budget():
        Budget.list_budgets()
        which_budget = input("Which budget do you want to deposit to?: ")
        if which_budget not in [x.name for x in Budget.budgets]:
            print("budget doesn't exist")
        else:
            how_much = round(float(input("How much do you want to deposit?: ")),2)
            for b in Budget.budgets:
                if which_budget == b.name:
                    b.deposit(how_much)
    
    def deposit(self, amount):
        amount = round(amount,2)
        pre_deposit = self.balance
        if amount < 0:
            print("Negative amount not allowed, use withdraw instead")
        elif amount == 0:
            print("no change")
        else:
            self.balance += amount
            if isinstance(self.history, type(None)):
                self.history = []
            self.history.append([self.balance, amount])
            Budget.budgets_history.append([self.name,self.balance,amount])
            print(f"You have deposited £{amount} into {self.name}. The balance before was £{pre_deposit} and the new balance is £{self.balance}")
            Budget.save_state()
            return [round(amount,2), self.balance]

    def withdraw_from_budget():            
        Budget.list_budgets()
        which_budget = input("Which budget do you want to withdraw from?: ")
        if which_budget not in [x.name for x in Budget.budgets]:
            print("budget doesn't exist")
        else:
            how_much = round(float(input("How much do you want to withdraw?: ")),2)
            for b in Budget.budgets:
                if which_budget == b.name:
                    b.withdraw(how_much)


    def withdraw(self, amount):
        amount = round(amount,2)
        pre_withdraw = self.balance
        if amount < 0:
            print("Negative amount not allowed, use a positive integer")
        elif amount == 0:
            print("no change")
        else:
            self.balance -= amount
            if isinstance(self.history, type(None)):
                self.history = []
            self.history.append([self.balance, -amount])
            Budget.budgets_history.append([self.name,self.balance,amount])
            print(f"You have withdrawn £{amount} from {self.name}. The balance before the withdrawal was {pre_withdraw} and the new balance is £{self.balance}")
            Budget.save_state()
            return [amount, self.balance]
    

    def transfer_between_account():
        Budget.list_budgets()
        which_budget_from = input("Which budget do you want to transfer from?: ")
        if which_budget_from not in [x.name for x in Budget.budgets]:
            print("budget doesn't exist")
        else:
            which_budget_to = input("Which budget do you want to transfer to?: ")
            if which_budget_to not in [x.name for x in Budget.budgets]:
                print("budget doesn't exist")
            else:
                how_much = round(float(input("How much do you want to deposit?: ")),2)
                for b in Budget.budgets:
                    if which_budget_from == b.name:
                        which_budget_from = b
                for g in Budget.budgets:
                    if which_budget_to == g.name:
                        which_budget_to = g
                Budget.transfer(which_budget_from,which_budget_to,how_much)
                

    def transfer(budget_from, budget_to, amount):
        amount = round(amount,2)
        pre_withdraw = budget_from.balance
        pre_deposit = budget_to.balance
        if amount <= 0:
            print("Must be a positive number")
        else:
            budget_from.balance -= amount
            budget_to.balance += amount
            if isinstance(budget_from.history, type(None)):
                budget_from.history = []
            budget_from.history.append([budget_from.balance, -amount])
            if isinstance(budget_to.history, type(None)):
                budget_to.history = []
            budget_to.history.append([budget_to.balance, amount])
            Budget.budgets_history.append([budget_from.name,budget_from.balance,-amount])
            Budget.budgets_history.append([budget_to.name,budget_to.balance,amount])
            print(f"You have transferred £{amount} from {budget_from.name} to {budget_to.name}.\nBalance before transfer:\n\t{budget_from.name}:£{pre_withdraw}\n\t{budget_to.name}:£{pre_deposit}\nBalance after transfer:\n\t{budget_from.name}:£{budget_from.balance}\n\t{budget_to.name}:£{budget_to.balance}")
            Budget.save_state()

    def balance_of_budget():
        Budget.list_budgets()
        which_budget = input("Which budget do you want the balance of?: ")
        if which_budget not in [x.name for x in Budget.budgets]:
            print("budget doesn't exist")
        else:
            for b in Budget.budgets:
                if which_budget == b.name:
                    b.print_balance()    


    def history_of_budget():
        Budget.list_budgets()
        which_budget = input("Which budget do you want to get a history for?: ")
        if which_budget not in [x.name for x in Budget.budgets]:
            print("budget doesn't exist")
        else:
            for b in Budget.budgets:
                if which_budget == b.name:
                    b.print_history()


    def print_history(self):
        print(f"History of {self.name}")
        i = 1
        for x in self.history:
            print(f"{i} - \tChange: £{x[1]}\n\tbalance: £{x[0]}")
            i += 1
        
    def print_balance(self):
        print(f"Your balance of {self.name} is £{self.balance}")
    
    def print_total_history(budgets_history=budgets_history):
        i = 1
        for x in budgets_history:
            print(f"{i} - Account: {x[0]}, Balance after Transfer: £{x[1]}, amount: £{x[2]}")
            i += 1

    def print_all_balances():
        print("List of all current balances")
        for x in Budget.budgets:
            print(f"Balance of {x.name} is currently £{x.balance}\n")   


    def print_total_balance(budgets=budgets):
        bal = sum([x.balance for x in budgets])
        print(f"The balance across all budgets is £{bal}")

    def check_for_save_file():
        if exists("save.txt"):
            save = open("save.txt", "r")
            details = save.readlines()
            budgets_history = ast.literal_eval(details[0])
            i = 1
            for line in details[1:]:
                line = line.split("/")
                name = line[0]
                balance = round(float(line[1]),2)
                history = line[2]
                history = ast.literal_eval(history)
                create_object = 'i = Budget(name, balance, history)'
                exec(create_object)
                i += 1
            save.close()
        else:
            print("no save file found")
            save = open("save.txt", "w")
            save.close()

    def save_state():
        save = open("save.txt", "w")
        save.write(str(Budget.budgets_history) + "\n")
        for b in Budget.budgets:
            save.write(f"{b.name}/ {b.balance}/ {b.history}\n")
        save.close()
        
    def list_budgets():
        print("List of existing budgets:")
        for b in Budget.budgets:
            print(f"{b.name}")
    
    def load_or_not():
        load = ""
        while load not in ("1", "2"):
            load = input("Do you want to load a file?\n1 for yes 2 for no: ")            
            if load == "1":
                Budget.check_for_save_file()