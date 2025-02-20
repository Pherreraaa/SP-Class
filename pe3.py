import datetime
import string

# Caesar Cipher Functions
def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    shifted_text = ""

    for char in input_text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            shifted_text += char  # Keep non-alphabet characters unchanged

    return (alphabet, shifted_text)

def decode(input_text, shift):
    decoded_text = ""

    for char in input_text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decoded_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decoded_text += char  # Keep non-alphabet characters unchanged

    return decoded_text

# BankAccount Class
class BankAccount:
    def __init__(self, name="Rainy", account_number="1234", creation_date=datetime.date.today(), balance=0):
        if creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future.")
        self.name = name
        self.account_number = account_number
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
        print(f"Deposit successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")

    def view_balance(self):
        print(f"Current balance: ${self.balance}")

# SavingsAccount Class
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        days_since_creation = (datetime.date.today() - self.creation_date).days
        if days_since_creation < 180:
            raise Exception("Withdrawals are only permitted after 180 days.")
        if amount > self.balance:
            raise ValueError("Insufficient funds. No overdraft allowed in SavingsAccount.")
        super().withdraw(amount)

# CheckingAccount Class
class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= (amount + 30)  # Apply overdraft fee
            print(f"Overdraft! A $30 fee has been charged. New balance: ${self.balance}")
        else:
            super().withdraw(amount)

