alphabet = "abcdefghijklmnopqrstuvwxyz"
input_text = input("Enter the text you want to encode: ")
shift = int(input("Please enter the shift you want to use to encode the entered text: "))

def encode(input_text, shift):
    encoded_string = ""
    for char in input_text:
        if char in alphabet:
            encoded_index = (alphabet.find(char) + shift - 1) % 26
            encoded_char = alphabet[encoded_index]
            encoded_string += encoded_char
        else:
            encoded_string += char
    return encoded_string

def decode(encoded_string, shift):
    decoded_string = ""
    for char in encoded_string:
        if char in alphabet:
            decoded_index = (alphabet.find(char) - shift + 1) % 26
            decoded_char = alphabet[decoded_index]
            decoded_string += decoded_char
        else:
            decoded_string += char
    return decoded_string

encoded_text = encode(input_text, shift)

print("The list of letters encoded are: " + str(tuple(encoded_text)) + " The encoded text is: " + str(encoded_text))

decoded_text = decode(encoded_text, shift)

print("The list of letters decoded are: " + str(tuple(decoded_text)) + " The encoded text is: " + str(decoded_text))


#2 Classes

import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

# Create a class called BankAccount.

class BankAccount:

# a) The class is initialized with the owner’s name (name), alphanumeric ID (ID), date of creation
# (creation date), and balance. Ensure that creation date is of type datetime.date. The date
# of creation can be the current date or a past date, but not a date in the future. If a creation
# date in the future is supplied as the creation date value, the program must raise an exception
# of class Exception.

    def __init__(self, name, ID, creation_date, balance):
        name = self.name
        ID = self.ID
        creation_date = self.creation_date
        balance = self.balance

    def func():
        creation_date = datetime.date(creation_date)
        if creation_date > datetime.date.today():
            raise ValueError("The creation_date cannot have a future date and time")
        else:
            #TBD
    
    Exception



# b) It has 3 instance methods: deposit(amount), withdraw(amount), and view balance().

deposit_amount = deposit(self, amount)

withdrawal_amount = withdraw(self, amount)

view_balance = view_balance(self)

# c) There are two subclasses to BankAccount: a SavingsAccount and a CheckingAccount.
# • SavingsAccount: only allows withdrawals after 6 months has passed since the creation of
# the account. Does not allow overdrafts. For simplicity assume that each month is 30 days
# long.
# • CheckingAccount: allows overdraft, but adds a $30 penalty fee each time a withdrawal
# results in a negative balance.

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        # self.TBD

    # def allow_withdrawal():
    #   date_difference = relativedelta(date(creation_date), datetime.date.today())  
    #   if date_difference.months >= 6 or date_difference.year > 0:
        #     TBD
        # else:
        #     TBD



class CheckingAccount(BankAccount):
    def __init__(self):
        super().__init__()
        # self.TBD

    def 

# d) Make sure your names are precisely consistent with the following:
# • Class names - BankAccount, CheckingAccount, SavingsAccount
# • Method Names - deposit(self, amount), withdraw(self, amount), view_balance(self)



# e) The BankAccount class should have default values for all the arguments as follows: name:
# ”Clocks”, id: ”123”, creation date: date.today(), balance: 0.
# • The creation date should be of type datetime.date
