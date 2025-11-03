class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  
        
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(19000)
account.deposit(5000)
print("Current Balance:", account.get_balance())