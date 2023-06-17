# 1. Functions

import string

all_chars = tuple(string.ascii_letters + string.digits + string.punctuation.replace('\\', '') + ' ') # modified alphabet for all_chars to include all most useful characters. However, I needed to also get rid of \ in string.punctuation to avoid escaping characters

def encode(input_text, shift):
    encoded_chars = []
    for char in input_text:
        if char in all_chars:
            encoded_index = (all_chars.index(char) + shift) % len(all_chars)
            encoded_char = all_chars[encoded_index]
            encoded_chars.append(encoded_char)
        else:
            encoded_chars.append(char)
    return encoded_chars, ''.join(encoded_chars)

def decode(encoded_string, shift):
    decoded_chars = []
    for char in encoded_string:
        if char in all_chars:
            decoded_index = (all_chars.index(char) - shift) % len(all_chars)
            decoded_char = all_chars[decoded_index]
            decoded_chars.append(decoded_char)
        else:
            decoded_chars.append(char)
    return decoded_chars, ''.join(decoded_chars)

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

