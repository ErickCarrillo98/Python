
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


account1.deposit(200).deposit(100).deposit(100).withdrawl(50).yield_interest()
print(account1.balance)

account2.deposit(20).deposit(20).withdwal(5).withdrawl(5).withdrawl(5).withdrawl(5).yield_interest()
print(account2.balance)

