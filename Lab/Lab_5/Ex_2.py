class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"deposited  ${amount} --> ${self.balance}")
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"withdrew ${amount} --> ${self.balance}")
        else:
            print("Insufficient funds.")

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"deposited: ${interest}")

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"withdrew ${amount} --> ${self.balance}")
        else:
            print("Insufficient Founds !")

savings_account = SavingsAccount(account_number="Luca", balance=1000)
savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.calculate_interest()

checking_account = CheckingAccount(account_number="Adi", balance=500, overdraft_limit=200)
checking_account.deposit(300)
checking_account.withdraw(700)
checking_account.withdraw(100)