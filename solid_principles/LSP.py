# class Account:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return True
#         return False


# class SavingsAccount:
    
#     if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

#     else:
#             print("Insufficient funds!")


# class CheckingAccount(Account):
#     def __init__(self, balance, overdraft_limit):
#         super().__init__(balance)
#         self.overdraft_limit = overdraft_limit

#     def withdraw(self, amount):
#         if self.balance + self.overdraft_limit >= amount:
#             self.balance -= amount
#             return True
#         return False


# def main():
#     savings_account = SavingsAccount(1000)
#     checking_account = CheckingAccount(2000, overdraft_limit=1000)

#     # Deposit and withdraw from savings account
#     savings_account.deposit(500)
#     print("Savings Account Balance:", savings_account.balance)

#     result = savings_account.withdraw(700)
#     print("Savings Account Withdrawal Result:", result)
#     print("Savings Account Balance:", savings_account.balance)

#     # Deposit and withdraw from checking account
#     checking_account.deposit(800)
#     print("Checking Account Balance:", checking_account.balance)

#     result = checking_account.withdraw(3000)
#     print("Checking Account Withdrawal Result:", result)
#     print("Checking Account Balance:", checking_account.balance)


# if __name__ == "__main__":
#     main()




class SavingsAccount():
    def __init__(self, balance) -> None:
        self.balance = balance

    def withdraw(self, amount):
        # Savings account does not allow overdrafts
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

        else:
            print("Insufficient funds!")

class CheckingAccount(SavingsAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Checking account allows overdrafts but with a limit
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")

def perform_bank_actions(account):
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)

if __name__ == "__main__":
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    perform_bank_actions(savings_account)
    perform_bank_actions(checking_account)