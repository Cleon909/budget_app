from os.path import exists
from ast import literal_eval
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
        amount = input("\nInitial amount in budget: ")
        while amount.replace(".","",1).isdigit() == False: 
            print("\nNot a valaid amount")
            amount = input("\nInitial amount in budget: ")
        while float(amount) <= 0:
            print("\nNot a valaid amount")
            amount = input("\nInitial amount in budget: ")
        amount = round(float(amount),2)
        name = Budget(name,amount)
        name.history = []
        name.history.append(["created", name.balance])
        Budget.budgets.append(name)
        Budget.budgets_history.append([name.name,name.balance, "created"])
        Budget.save_state()

    def __repr__(self):
        rep = f"There is £{self.balance:.2f} in the {self.name} budget. If you want a print of the history use history method."
        return rep

    def get_input_for_deposit():
        Budget.list_budgets()
        which_budget = input("\nWhich budget do you want to deposit to? Input number, or 0 to go back to main menu: ")
        while which_budget.isdigit() == False:
            print("\nInvalid input")
            which_budget = input("\nWhich budget do you want to deposit to? Input number, or 0 to go back to main menu: ")
        which_budget = str(int(which_budget)-1)
        if which_budget == "-1":
            return
        elif which_budget not in Budget.menu_list:
            print("\nbudget doesn't exist")
        else:
            how_much = input("\nHow much do you want to deposit? (must be a positive amount): ")
            while how_much.replace(".","",1).isdigit() == False:
                print("\nNot a valid amount.")
                how_much = input("\nHow much do you want to deposit? (must be a positive amount): ")
            while float(how_much) <= 0:
                print("\nNot a valid amount.")
                how_much = input("\nHow much do you want to deposit? (must be a positive amount): ")
            how_much = round(float(how_much),2)
            Budget.budgets[int(which_budget)].deposit(how_much)
    
    def deposit(self, amount):
        amount = round(amount,2)
        self.balance += amount
        if isinstance(self.history, type(None)):
            self.history = []
        self.history.append([self.balance, amount])
        Budget.budgets_history.append([self.name,self.balance, amount])
        print(f"\nYou have deposited £{amount:.2f} into {self.name}. The new balance is £{self.balance:.2f}")
        Budget.save_state()
 

    def get_input_for_withdraw():            
        Budget.list_budgets()
        which_budget = input("\nWhich budget do you want to withdraw from? Input number, or 0 to go back to main menu: ")
        while which_budget.isdigit() == False:
            print("\ninvalid input")
            which_budget = input("\nWhich budget do you want to withdraw from? Input number, or 0 to go back to main menu: ")
        which_budget = str(int(which_budget)-1)
        if which_budget == "-1":
            return
        elif which_budget not in Budget.menu_list:
            print("\nbudget doesn't exist")
        else:
            how_much = input("\nHow much do you want to withdraw? (must be a positive amount): ")
            while how_much.replace(".","",1).isdigit() == False: 
                print("\nNot a valid amount")
                how_much = input("\nHow much do you want to withdraw? (must be a positive amount): ")
            while float(how_much) <= 0:
                print("\nNot a valid amount")
                how_much = input("\nHow much do you want to withdraw? (must be a positive amount): ")
            how_much = round(float(how_much),2)
            Budget.budgets[int(which_budget)].withdraw(how_much)


    def withdraw(self, amount):
        amount = round(amount,2)
        self.balance -= amount
        if isinstance(self.history, type(None)):
            self.history = []
        self.history.append([self.balance, -amount])
        Budget.budgets_history.append([self.name,self.balance,-amount])
        print(f"\nYou have withdrawn £{amount:.2f} from {self.name}. The new balance is £{self.balance:.2f}", "blue")
        Budget.save_state()
  
    

    def get_transfer_details():
        Budget.list_budgets()
        which_budget_from = input("\nWhich budget do you want to transfer from? Input number, or 0 to go back to main menu: ")
        while which_budget_from.isdigit() == False:
            print("\ninvalid input")
            which_budget_from = input("\nWhich budget do you want to transfer from? Input number, or 0 to go back to main menu: ")
        which_budget_from = str(int(which_budget_from)-1)
        if which_budget_from == "-1":
            return
        elif which_budget_from not in Budget.menu_list:
            print("\nbudget doesn't exist")
        else:
            which_budget_to = input("\nWhich budget do you want to transfer to? Input number, or 0 to go back to main menu: ")
            while which_budget_to.isdigit() == False:
                print("\nInvalid input")
                which_budget_to = input("\nWhich budget do you want to transfer to? Input number, or 0 to go back to main menu: ")
            which_budget_to = str(int(which_budget_to)-1)
            if which_budget_to == "-1":
                return
            elif which_budget_to not in Budget.menu_list:
                print("\nbudget doesn't exist")
            else:
                how_much = input("\nHow much do you want to transfer? (must be a postive amount): ")
                while how_much.replace(".","",1).isdigit() == False: 
                    print("\nNot a valid amount")
                    how_much = input("\nHow much do you want to transfer? (must be a postive amount): ")
                while float(how_much) <= 0:
                    print("\nNot a valid amount")
                    how_much = input("\nHow much do you want to transfer? (must be a postive amount): ")
                how_much = round(float(how_much),2)
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
        print(f"\nYou have transferred £{amount:.2f} from {budget_from.name} to {budget_to.name}.\nBalance after transfer:\n\t{budget_from.name}:£{budget_from.balance:.2f}\n\t{budget_to.name}:£{budget_to.balance:.2f}")
        Budget.save_state()

    def balance_of_budget():
        Budget.list_budgets()
        which_budget = input("\nWhich budget do you want the balance of? type in number next to name or 0 to return to main menu: ")
        while which_budget.isdigit() == False:
            print("\nInvalid Input")
            which_budget = input("\nWhich budget do you want the balance of? type in number next to name or 0 to return to main menu: ")
        which_budget = str(int(which_budget)-1)
        if which_budget == "-1":
            return
        elif which_budget not in Budget.menu_list:
            print("\nbudget doesn't exist")
        else:
            Budget.budgets[int(which_budget)].print_balance()    


    def get_input_for_history():
        Budget.list_budgets()
        which_budget = input("\nWWhich budget do you want to get a history for? Type in number next to name or 0 to return to menu: ")
        while which_budget.isdigit() == False:
            print("\nInvalid input")
            which_budget = input("\nWWhich budget do you want to get a history for? Type in number next to name or 0 to return to menu: ")
        which_budget = str(int(which_budget)-1)
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
                print(f"{i} - \t{self.name} was created with balance of £{x[1]:.2f}\n")
            else:
                print(f"{i} - \tChange: £{x[1]:.2f}\n\tbalance: £{x[0]:.2f}\n")
            i += 1
    
    def print_total_history():
        (str(1))
        i = 1
        print("\n")
        for x in Budget.budgets_history:
            if x[2] =="created":
                print(f"{i} - Account {x[0]} was created with a balance of £{x[1]:.2f}")
            else:
                print(f"{i} - Account: {x[0]}. Amount changed: £{x[2]:.2f}. Balance after: £{x[1]:.2f}")
            i += 1

    def print_balance(self):
        print(f"\nYour balance of {self.name} is £{self.balance:.2f}")
    
    def print_all_balances():
        print("\nList of all current balances")
        print("\n")
        for x in Budget.budgets:
            print(f"Balance of {x.name} is currently £{x.balance:.2f}\n")   


    def print_total_balance(budgets=budgets):
        bal = sum([x.balance for x in budgets])
        print(f"\nThe balance across all budgets is £{bal:.2f}")

    def check_for_save_file():
        if exists("save.txt"):
            save = open("save.txt", "r")
            details = save.readlines()
            Budget.budgets_history = literal_eval(details[0])
            i = 1
            for line in details[1:]:
                line = line.split("/")
                name = line[0]
                balance = round(float(line[1]),2)
                history = line[2]
                history = literal_eval(history)
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
 
    
    

