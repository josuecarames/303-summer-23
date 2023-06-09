# alphabet = "abcdefghijklmnopqrstuvwxyz"
# input_text = input("Enter the text you want to encode: ")
# shift = int(input("Please enter the shift you want to use to encode the entered text: "))

# def encode(input_text, shift):
#     encoded_string = ""
#     for char in input_text:
#         if char in alphabet:
#             encoded_index = (alphabet.find(char) + shift - 1) % 26
#             encoded_char = alphabet[encoded_index]
#             encoded_string += encoded_char
#         else:
#             encoded_string += char
#     return encoded_string

# def decode(encoded_string, shift):
#     decoded_string = ""
#     for char in encoded_string:
#         if char in alphabet:
#             decoded_index = (alphabet.find(char) - shift + 1) % 26
#             decoded_char = alphabet[decoded_index]
#             decoded_string += decoded_char
#         else:
#             decoded_string += char
#     return decoded_string

# encoded_text = encode(input_text, shift)

# print("The list of letters encoded are: " + str(tuple(encoded_text)) + " The encoded text is: " + str(encoded_text))

# decoded_text = decode(encoded_text, shift)

# print("The list of letters decoded are: " + str(tuple(decoded_text)) + " The encoded text is: " + str(decoded_text))


#2 Classes

# # Import modules

import datetime
from datetime import date
# from dateutil.relativedelta import relativedelta

class BankAccount:
    def __init__(self, name="Clocks", ID="123", creation_date=date.today(), balance=0):
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance
        if self.creation_date > date.today():
            raise Exception("Invalid creation date")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def view_balance(self):
        return self.balance

# c) There are two subclasses to BankAccount: a SavingsAccount and a CheckingAccount.
# • SavingsAccount: only allows withdrawals after 6 months has passed since the creation of
# the account. Does not allow overdrafts. For simplicity assume that each month is 30 days
# long.
# • CheckingAccount: allows overdraft, but adds a $30 penalty fee each time a withdrawal
# results in a negative balance.

class SavingsAccount(BankAccount):
    # def __init__(self):
    #     super().__init__()

    def withdraw(self, amount):
        date_difference = relativedelta(date(creation_date), datetime.date.today())  
        if date_difference.months >= 6 or date_difference.year > 0:
            super().withdraw(amount)
        else:
            print("You cannot make a withdrawal before your account has reached 6 months maturity")

class CheckingAccount(BankAccount):
    # def __init__(self):
    #     super().__init__()

    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= (amount + 30)
        else:
            super().withdraw(amount)

# • Method Names - deposit(self, amount), withdraw(self, amount), view_balance(self)


test = BankAccount(name="test", ID="321", creation_date=date(), balance=10)

print(test.name, test.ID, test.creation_date, test.balance)