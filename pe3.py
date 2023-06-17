import string
import datetime
from datetime import date, timedelta

all_chars = str(string.ascii_letters + string.digits + string.punctuation.replace('\\', '') + ' ')

def encode(input_text, shift):
    encoded_chars = []
    for char in input_text:
        if char in all_chars:
            encoded_index = (all_chars.index(char) + shift) % len(all_chars)
            encoded_char = all_chars[encoded_index]
            encoded_chars.append(encoded_char)
        else:
            encoded_chars.append(char)
    return ''.join(encoded_chars)

def decode(encoded_string, shift):
    decoded_chars = []
    for char in encoded_string:
        if char in all_chars:
            decoded_index = (all_chars.index(char) - shift) % len(all_chars)
            decoded_char = all_chars[decoded_index]
            decoded_chars.append(decoded_char)
        else:
            decoded_chars.append(char)
    return ''.join(decoded_chars)

class BankAccount:
    def __init__(self, name="Clocks", ID="123", creation_date=None, balance=0):
        if creation_date is None:
            creation_date = date.today()
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance
        if self.creation_date > date.today():
            raise Exception("creation_date cannot be a future date")
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
            raise Exception("You cannot make a withdrawal before your account has reached 6 months maturity")

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= (amount + 30)
        else:
            super().withdraw(amount)
