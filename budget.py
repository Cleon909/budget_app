
class Budget():

    budgets_history = []
    budgets = []

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = round(balance,2)
        self.history = []
        self.__class__.budgets.append(self)
     

    def __repr__(self):
        return f"There is £{self.balance} in the {self.name} budget. If you want a print of the history use history method."
    
    def deposit(self, amount):
        amount = round(amount,2)
        if amount < 0:
            print("Negative amount not allowed, use withdraw instead")
        elif amount == 0:
            print("no change")
        else:
            self.balance += amount
            self.history.append((self.balance, amount))
            self.budgets_history.append((self.name,self.balance,amount))
            print(f"You have deposited £{amount} into {self.name}. The new balance is £{self.balance}")
            return [round(amount,2), self.balance]

    def withdraw(self, amount):
        amount = round(amount,2)
        if amount < 0:
            print("Negative amount not allowed, use a positive integer")
        elif amount == 0:
            print("no change")
        else:
            self.balance -= amount
            self.history.append((self.balance, -amount))
            self.budgets_history.append((self.name,self.balance,amount))
            print(f"You have withdrawn £{amount} from {self.name}. The new balance is £{self.balance}")
            return [amount, self.balance]
    
    def transfer_from_to(self, budget_to, amount):
        amount = round(amount,2)
        if amount <= 0:
            print("Must be a positive number")
        else:
            self.balance -= amount
            budget_to.balance += amount
            self.history.append((self.balance, -amount))
            budget_to.history.append((budget_to.history, amount))
            self.budgets_history.append((self.name,self.balance,-amount))
            self.budgets_history.append((budget_to.name,budget_to.balance,amount))
            print(f"You have transferred £{amount} from {self.name} to {budget_to.name}.\nBalance after transfer:\n\t{self.name}:£{self.balance}\n\t{budget_to.name}:£{budget_to.balance}")
            return [self.balance, amount]
        

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
            print(f"{i} - Account: {x[0]}, Balance after Transfer: {x[1]}, amount: £{x[2]}")
            i += 1
    def print_all_balances():
        print("List of all current balances")
        for x in budgets:
            print(f"Balance of {x.name} is currently £{x.balance}\n")   


    def print_total_balance(budgets=budgets):
        bal = sum([x.balance for x in budgets])
        print(f"The balance across all budgets is £{bal}")
    
 

    
    

