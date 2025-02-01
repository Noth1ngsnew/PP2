class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено: {amount}. Новый баланс: {self.balance}.")
        else:
            print("Сумма для депозита должна быть положительной.")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снято: {amount}. Новый баланс: {self.balance}.")
        else:
            print("Ошибка! Недостаточно средств на счете.")
    
    def get_balance(self):
        return self.balance


account = Account("Иван", 100)

account.deposit(50)  
account.deposit(30)  

account.withdraw(70)  
account.withdraw(200)


print("Текущий баланс:", account.get_balance())