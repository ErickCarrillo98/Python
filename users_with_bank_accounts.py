class BankAccount:

        def __init__(self, name, balance, int_rate):
                self.name = name
                self.balance =balance
                self.int_rate = int_rate

        def deposit(self, amount):
                self.balance += amount

        def withdrawl(self, amount):
                self.balance -= amount

        def display_account_info(self):
                self.balance().name()


        def yield_interest(self):
                self.balance += (self.balance *self.int_rate)

account1 = BankAccount('Erick Carrillo', 1000, .02)
account2 = BankAccount('Billy Bob', 5000, .10)


class User(BankAccount):		
        def __init__(self, name, email):
            self.name = name
            self.email = email
            self.account_balance = 0

        def method_example(self):
            self.account.deposit(100)
            print(self.account.balance)
        def method_example2(self):
            self.account.withdrawl(10)

        def display_user_balance(self):
            self.account


        def transfer_money(self, user, amount):
            self.account -= amount
            user.account += amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty python", "monty@python.com")
erick = User("Erick Carrillo", "Erick.carrillo@hotmail.com")

print(guido.name)
print(monty.name)
print(erick.name)



