tbal = []
thist = []

class Budget():
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = round(balance,2)
        self.history = []
        tbal.append(self)

    def __repr__(self):
        return f"There is £{self.balance} in the {self.name} budget. If you want a print of the history use history method."
    
    def deposit(self, amount):
        amount = round(amount,2)
        if amount < 0:
            print("Negative amount not allowed, use wtihdraw instead")
        elif amount == 0:
            print("no change")
        else:
            self.balance += amount
            self.history.append((self.balance, amount))
            thist.append((self,self.balance,amount))
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
            thist.append((self,self.balance,amount))
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
            thist.append((self,self.balance,-amount))
            thist.append((budget_to,budget_to.balance,amount))
            print(f"You have transferred £{amount} from {self.name} to {budget_to.name}.\nBalance after transfer:\n\t{self.name}:£{self.balance}\n\t{budget_to.name}:£{budget_to.balance}")
            return [self.balance, amount]
        
    def transfer_to_from(self, budget_from, amount):
        amount = round(amount,2)
        if amount <= 0:
            print("Must be a positive number")
        else:
            self.balance += amount
            budget_from.balance -= amount
            self.history.append((self.balance, amount))
            budget_from.history.append((budget_from.history, -amount))
            thist.append((self,self.balance,amount))
            thist.append((budget_from,budget_from.balance,-amount))
            print(f"You have transferred £{amount} from {self.name} to {budget_from.name}.\nBalance after transfer:\n\t{self.name}:£{self.balance}\n\t£{budget_from.name}:£{budget_from.balance}")
            return [self.balance, amount]

    def print_history(self):
        print(f"History of {self.name}")
        i = 1
        for x in self.history:
            print(f"{i} - \tChange: £{x[1]}\n\tbalance: £{x[0]}")
            i += 1
        
    def print_balance(self):
        print(f"Your balance of {self.name} is £{self.balance}")
    
    def print_total_history(total_history):
        for x in total_history:
            print(f"Account: {x[0]}, Balance after Transfer: {x[1]}, amount: {x[2]}")
    
    def print_total_balance(total_balance):
        bal = sum([x.balance for x in total_balance])
        print(f"The balance across all budgets is £{bal}")
    
    

