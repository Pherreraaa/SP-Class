import string
import datetime

# ------------------------
# Caesar Cipher Functions
# ------------------------

def encode(input_text: str, shift: int):
    """
    Encodes a given text using Caesar cipher with the specified shift.
    Returns a tuple of (alphabet, encoded text).
    """
    alphabet = list(string.ascii_lowercase)  # Full lowercase alphabet
    shifted_text = []

    for char in input_text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            shifted_text.append(char)  # Preserve non-alphabetic characters

    return (alphabet, ''.join(shifted_text))

def decode(input_text: str, shift: int):
    """
    Decodes a given text using Caesar cipher with the specified shift.
    Returns only the decoded text.
    """
    return encode(input_text, -shift)[1]  # Use negative shift for decoding


# ------------------------
# BankAccount Class
# ------------------------

class BankAccount:
    def __init__(self, name="Rainy", account_number="1234", creation_date=None, balance=0):
        """
        Initializes a BankAccount instance.
        """
        if creation_date is None:
            creation_date = datetime.date.today()
        
        if creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future.")
        
        self.name = name
        self.account_number = account_number
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits an amount into the bank account.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        
        self.balance += amount
        print(f"Deposit successful. New balance: ${self.balance}")
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws an amount from the bank account.
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")
        return self.balance

    def view_balance(self):
        """
        Returns the current balance of the account.
        """
        return self.balance


# ------------------------
# SavingsAccount Class
# ------------------------

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        """
        Withdraw from savings account only if it has been open for 180+ days.
        """
        days_since_creation = (datetime.date.today() - self.creation_date).days
        if days_since_creation < 180:
            raise Exception("Withdrawals are only permitted after 180 days.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")
        return self.balance


# ------------------------
# CheckingAccount Class
# ------------------------

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        """
        Allows overdrafts but applies a $30 overdraft fee.
        """
        if amount > self.balance:
            self.balance -= (amount + 30)  # Apply overdraft fee
            print(f"Overdraft! A $30 fee has been charged. New balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: ${self.balance}")
        return self.balance

