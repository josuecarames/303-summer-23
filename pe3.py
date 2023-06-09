# 1. Functions

alphabet = "abcdefghijklmnopqrstuvwxyz"
input_text = input("Enter the text you want to encode: ").lower() # If text is not converted into lower case, the encryption doesn't work
shift = int(input("Please enter the shift you want to use to encode the entered text: "))

def encode(input_text, shift):
    encoded_string = ""
    for char in input_text:
        if char in alphabet:
            encoded_index = (alphabet.find(char) + shift) % 26
            encoded_char = alphabet[encoded_index]
            encoded_string += encoded_char
        else:
            encoded_string += char
    return encoded_string

def decode(encoded_string, shift):
    decoded_string = ""
    for char in encoded_string:
        if char in alphabet:
            decoded_index = (alphabet.find(char) - shift) % 26
            decoded_char = alphabet[decoded_index]
            decoded_string += decoded_char
        else:
            decoded_string += char
    return decoded_string

encoded_text = encode(input_text, shift)

print("The list of letters encoded are: " + str(tuple(encoded_text)) + " The encoded text is: " + str(encoded_text))

decoded_text = decode(encoded_text, shift)

print("The list of letters decoded are: " + str(tuple(decoded_text)) + " The decoded text is: " + str(decoded_text))


# Review why the first letter is not encoding

#2 Classes

# # Import modules

import datetime
from datetime import date, timedelta

class BankAccount:
    def __init__(self, name="Clocks", ID="123", creation_date=datetime.date.today(), balance=0):
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance
        if self.creation_date > date.today():
            raise Exception("creation_date cannot be in the future")
        self.maturity_date = self.creation_date + timedelta(days=180)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def view_balance(self):
        return self.balance

class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        current_date = datetime.date.today()  
        if current_date >= self.maturity_date:
            super().withdraw(amount)
        else:
            print("You cannot make a withdrawal before your account has reached 6 months maturity")

class CheckingAccount(BankAccount):

    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= (amount + 30)
        else:
            super().withdraw(amount)


# test = BankAccount(name="test", ID="321", creation_date=date(2023, 6, 9), balance=0) # BankAccount class works

# test = BankAccount(name="test", ID="321", creation_date=date(2023, 9, 9), balance=0) # Future date raises Exception

# test.withdraw(25)

# print("Updated balance: ", test.view_balance())

# test = CheckingAccount(name="test", ID="321", creation_date=date(2023, 6, 9), balance=0) # Overdraft +$30

# test = SavingsAccount(name="test", ID="321", creation_date=datetime.date(2023, 1, 1), balance=100) # Account maturity older than 6 months 

# print(test.name, test.ID, test.creation_date, test.balance)

# test.withdraw(25)

# print("Updated balance: ", test.view_balance())

# test = SavingsAccount(name="test", ID="321", creation_date=datetime.date.today(), balance=100) # Account maturity younger than 6 months doesn't withdraw from balance

# print(test.name, test.ID, test.creation_date, test.balance)

# test.withdraw(25)

# print("Updated balance: ", test.view_balance())