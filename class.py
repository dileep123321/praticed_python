class amazon_employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")
employee1 = amazon_employee("Dileep", "Software Engineer", 75000)
employee2 = amazon_employee("Bhara", "Data Scientist", 85000)
employee1.display_info()
employee2.display_info()


class bank_account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
account = bank_account("Dileep", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)