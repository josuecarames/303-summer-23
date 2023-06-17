# 1. Functions

import string

alphabet_list = [chr(ord('a') + i) for i in range(26)]

def encode(input_text, shift):
    shifted_alphabet_list = []
    input_text = input_text.lower()
    for character in input_text:
        if character not in alphabet_list:
            shifted_character = character
            shifted_alphabet_list.append(shifted_character)
        else:
            shifted_character = alphabet_list[(alphabet_list.index(character) + shift) % 26]
            shifted_alphabet_list.append(shifted_character)
    shifted_alphabet_str = ''.join(shifted_alphabet_list)
    return (alphabet_list, shifted_alphabet_str)

def decode(input_text, shift):
    shifted_alphabet_list = []
    input_text = input_text.lower()
    for character in input_text:
        if character not in alphabet_list:
            shifted_character = character
            shifted_alphabet_list.append(shifted_character)
        else:
            shifted_character = alphabet_list[(alphabet_list.index(character) - shift + 26) % 26]
            shifted_alphabet_list.append(shifted_character)
    shifted_alphabet_str = ''.join(shifted_alphabet_list)
    return shifted_alphabet_str

# 2 Classes

import datetime

class BankAccountExceptions(Exception):
    pass
    
class BankAccount():
    def __init__(self, name='Clocks', ID='123', creation_date=datetime.date.today(), balance=0):
        if not isinstance(creation_date, datetime.date):
            raise BankAccountExceptions("creation_date should be the type of datetime.date.")
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance
        self.validate_creation_date()

    def validate_creation_date(self):
        current_date = datetime.date.today()
        if self.creation_date > current_date:
            raise BankAccountExceptions("creation_date cannot be a future date.")

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount >= 0:
            self.balance -= amount
        return self.balance

    def view_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        one_day = datetime.timedelta(days=1)
        if datetime.date.today() + one_day * 30 * 6 >= self.creation_date and self.balance - amount >= 0 and amount >= 0:
            self.balance -= amount
        return self.balance

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount >= 0 and amount >= 0:
            self.balance -= amount
        else:
            self.balance -= amount + 30
        return self.balance
