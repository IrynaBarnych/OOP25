# Завдання 5
# Створіть клас BankAccount з атрибутами balance та owner, а також методами deposit та withdraw для
# здійснення операцій з балансом. Реалізуйте перевірку на те, що баланс не може стати від'ємним.


class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Сума повинна бути більше 0")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Недостатньо коштів на рахунку")
        else:
            print("Сума повинна бути більше 0")

    def get_balance(self):
        return self.balance


# Створення екземпляра класу
account = BankAccount(1000, "John")
account.deposit(500)
account.withdraw(200)
print(account.get_balance())