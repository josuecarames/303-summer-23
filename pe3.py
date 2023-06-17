# 1. Functions

alphabet = "abcdefghijklmnopqrstuvwxyz"
input_text = input("Enter the text you want to encode: ").lower() # If text is not converted into lower case, the encryption doesn't work
shift = int(input("Please enter the shift you want to use to encode the entered text: "))

def encode(input_text, shift):
    encoded_string = ""
    for char in input_text:
        if char in alphabet:
            encoded_index = (alphabet.find(char) + shift) % 26 #Adding modulo 26 ensures that the shift for the encoded letter stays within range
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

#2 Classes

import datetime
from datetime import date, timedelta

class BankAccount:
    def __init__(self, name="Clocks", ID="123", creation_date=date.today(), balance=0):
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance
        if self.creation_date > date.today():
            raise Exception("creation_date cannot be a future date")
        self.maturity_date = self.creation_date + timedelta(days=180) # We need to add 'self.' to maturity_date because it needs to be accessed within the 'SavingsAccount' class.

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


# Test to see if BankAccount class works

test = BankAccount(name="test", ID="321", creation_date=date(2023, 6, 9), balance=0) # BankAccount class works

print(test.name, test.ID, test.creation_date, test.balance)

# First test to see if overdraft works in CheckingAccount

test1 = CheckingAccount(name="test1", ID="321", creation_date=date(2023, 6, 9), balance=0) # Overdraft +$30

print("Balance before withdrawal: ", test1.view_balance())

test1.withdraw(25)

print("Updated balance: ", test1.view_balance())

# Second test to see if we can make a withdrawal from a SavingsAccount that is older than 6 months

test2 = SavingsAccount(name="test2", ID="321", creation_date=datetime.date(2023, 1, 1), balance=100) # Account maturity older than 6 months 

print(test2.name, test2.ID, test2.creation_date, test2.balance)

test2.withdraw(25)

print("Updated balance: ", test2.view_balance())

# Third test to see if we can make a withdrawal from a SavingsAccount that is younger than 6 months

test3 = SavingsAccount(name="test3", ID="321", creation_date=datetime.date.today(), balance=100)

print(test3.name, test3.ID, test3.creation_date, test3.balance)

test3.withdraw(25)

print("Updated balance: ", test3.view_balance())

# Fourth test to see if we can create an account with a future date for creation_date 

test4 = BankAccount(name="test4", ID="321", creation_date=date(2024, 9, 9), balance=0) # Future date raises Exception

test4.withdraw(25)

print("Updated balance: ", test4.view_balance())
