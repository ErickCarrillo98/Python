#make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
#display_user_balance(self) - have this method print the user's name and account balance to the terminal
#eg. "User: Guido van Rossum, Balance: $150
#BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance




class User:		# here's what we have so far
        def __init__(self, name, email):
            self.name = name
            self.email = email
            self.account_balance = 0

        def make_deposit(self, amount):
            self.account_balance += amount

        def make_withdrawl(self, amount):
            self.account_balance -= amount

        def display_user_balance(self):
            self.account_balance


        def transfer_money(self, user, amount):
            self.account_balance -= amount
            user.account_balance += amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty python", "monty@python.com")
erick = User("Erick Carrillo", "Erick.carrillo@hotmail.com")

print(guido.name)
print(monty.name)
print(erick.name)

guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_withdrawl(200)
print(guido.account_balance)

monty.make_deposit(200)
monty.make_deposit(200)
monty.make_withdrawl(50)
monty.make_withdrawl(50)
print(monty.account_balance)


erick.make_deposit(500)
erick.make_withdrawl(50)
erick.make_withdrawl(50)
erick.make_withdrawl(50)
print(erick.account_balance)


guido.transfer_money(erick, 20)
print(guido.account_balance)
print(erick.account_balance)

