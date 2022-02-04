from os.path import exists
import ast
import pdb

class Budget():

    budgets_history = []
    budgets = []
    menu_list = []

    def __init__(self, name, balance=0, history=None):
        self.name = name
        self.balance = round(balance,2)
        self.history = history
        

    def create_budget():
        Budget.list_budgets()
        name = input("\nchoose name for budget: ")
        while name in (x.name for x in Budget.budgets):
            print("\nname taken")
            name = input("\nchoose name for budget: ")
        amount = round(float(input("\nInitial amount in budget: ")),2)
        name = Budget(name,amount)
        name.history = []
        name.history.append(["created", name.balance])
        Budget.budgets.append(name)
        Budget.budgets_history.append([name.name,name.balance, "created"])

    def __repr__(self):
        return f"\nThere is £{self.balance} in the {self} budget. If you want a print of the history use history method."

    def get_input_for_deposit():
        Budget.list_budgets()
        which_budget = str(int(input("\nWhich budget do you want to deposit to? Input number, or 0 to go back to main menu: "))-1)
        if which_budget == "-1":
            return
        elif which_budget not in Budget.menu_list:
            print("\nbudget doesn't exist")
        else:
            how_much = round(float(input("\nHow much do you want to deposit?: ")),2)
            Budget.budgets[int(which_budget)].deposit(how_much)
    
    def deposit(self, amount):
        amount = round(amount,2)
        if amount < 0:
            print("\nNegative amount not allowed, use withdraw instead")
        elif amount == 0:
            print("\nno change")
        else:
            self.balance += amount
            if isinstance(self.history, type(None)):
                self.history = []
            self.history.append([self.balance, amount])
            Budget.budgets_history.append([self.name,self.balance, amount])
            print(f"\nYou have deposited £{amount} into {self.name}. The new balance is £{self.balance}")
            Budget.save_state()
 

    def get_input_for_withdraw():            
        Budget.list_budgets()
        which_budget = str(int(input("\nWhich budget do you want to withdraw from? Input number or input 0 to back to main menu: "))-1)
        if which_budget == "-1":
            return
        elif which_budget not in Budget.menu_list:
            print("\nbudget doesn't exist")
        else:
            how_much = round(float(input("\nHow much do you want to withdraw?: ")),2)
            Budget.budgets[int(which_budget)].withdraw(how_much)


    def withdraw(self, amount):
        amount = round(amount,2)
        if amount < 0:
            print("\nNegative amount not allowed, use a positive integer")
        elif amount == 0:
            print("\nno change")
        else:
            self.balance -= amount
            if isinstance(self.history, type(None)):
                self.history = []
            self.history.append([self.balance, -amount])
            Budget.budgets_history.append([self.name,self.balance,f"amount"])
            print(f"\nYou have withdrawn £{amount} from {self.name}. The new balance is £{self.balance}", "blue")
            Budget.save_state()
  
    

    def get_transfer_details():
        Budget.list_budgets()
        which_budget_from = str(int(input("\nWhich budget do you want to transfer from? Input number or 0 to return to main menu: "))-1)
        if which_budget_from == "-1":
            return
        elif which_budget_from not in Budget.menu_list:
            print("\nbudget doesn't exist")
        else:
            which_budget_to = str(int(input("Which budget do you want to transfer to? Input number or input 0 to return to main menu"))-1)
            if which_budget_to == "-1":
                return
            elif which_budget_to not in Budget.menu_list:
                print("\nbudget doesn't exist")
            else:
                how_much = round(float(input("\nHow much do you want to transfer8?: ")),2)
                if how_much <= 0:
                    print("\nMust be a positive amount")
                Budget.transfer(Budget.budgets[int(which_budget_from)], Budget.budgets[int(which_budget_to)], how_much)
                

    def transfer(budget_from, budget_to, amount):
        amount = round(amount,2)
        budget_from.balance -= amount
        budget_to.balance += amount
        if isinstance(budget_from.history, type(None)):
            budget_from.history = []
        budget_from.history.append([budget_from.balance, -amount])
        if isinstance(budget_to.history, type(None)):
            budget_to.history = []
        budget_to.history.append([budget_to.balance, amount])
        Budget.budgets_history.append([budget_from.name,budget_from.balance, -amount])
        Budget.budgets_history.append([budget_to.name,budget_to.balance, amount])
        print(f"\nYou have transferred £{amount} from {budget_from.name} to {budget_to.name}.\nBalance after transfer:\n\t{budget_from.name}:£{budget_from.balance}\n\t{budget_to.name}:£{budget_to.balance}")
        Budget.save_state()

    def balance_of_budget():
        Budget.list_budgets()
        which_budget = str(int(input("\nWhich budget do you want the balance of? type in number next to name or 0 to return to main menu: "))-1)
        if which_budget == "-1":
            return
        elif which_budget not in Budget.menu_list:
            print("\nbudget doesn't exist")
        else:
            Budget.budgets[int(which_budget)].print_balance()    


    def get_input_for_history():
        Budget.list_budgets()
        which_budget = str(int(input("\nWhich budget do you want to get a history for? Type in number next to name or 0 to return to menu: "))-1)
        if which_budget == "-1":
            return        
        elif which_budget not in Budget.menu_list:
            print("\nbudget doesn't exist")
        else:
            Budget.budgets[int(which_budget)].print_history()


    def print_history(self):
        print(f"\nHistory of {self.name}\n")
        i = 1
        for x in self.history:
            if self.history.index(x) == 0:
                print(f"{i} - \t{self.name} was created with balance of £{x[1]}\n")
            else:
                print(f"{i} - \tChange: £{x[1]}\n\tbalance: £{x[0]}\n")
            i += 1
        
    def print_balance(self):
        print(f"\nYour balance of {self.name} is £{self.balance}")
    
    def print_total_history(budgets_history=budgets_history):
        i = 1
        print = "\n"
        pdb.set_trace()
        for x in Budget.budgets_history:
            if x[2] =="created":
                print(f"{i} - Account {x[0]}, was created with a balance of £{x[1]}")
            else:
                print(f"{i} - Account: {x[0]}. Amount changed: £{x[2]}. Balance after: £{x[1]}")
            i += 1

    def print_all_balances():
        print("\nList of all current balances")
        print("\n")
        for x in Budget.budgets:
            print(f"Balance of {x.name} is currently £{x.balance}\n")   


    def print_total_balance(budgets=budgets):
        bal = sum([x.balance for x in budgets])
        print(f"\nThe balance across all budgets is £{bal}")

    def check_for_save_file():
        if exists("save.txt"):
            save = open("save.txt", "r")
            details = save.readlines()
            Budget.budgets_history = ast.literal_eval(details[0])
            i = 1
            for line in details[1:]:
                line = line.split("/")
                name = line[0]
                balance = round(float(line[1]),2)
                history = line[2]
                history = ast.literal_eval(history)
                create_object = f'a{i} = Budget(name, balance, history)'
                append_object = f'Budget.budgets.append(a{i})'
                exec(create_object)
                exec(append_object)
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
        Budget.menu_list = []
        print("\nList of existing budgets:\n")
        for x,b in enumerate(Budget.budgets):
            Budget.menu_list.append(str(x))
            print(f"{x+1}.  {b.name}")
    
    def load_or_not():
        load = ""
        while load not in ("1", "2"):
            load = input("Do you want to load a file?\n1 for yes 2 for no: ")            
            if load == "1":
                Budget.check_for_save_file()
 
    
    

