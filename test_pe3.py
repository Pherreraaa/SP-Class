# this file contains tests for a file named "pe3.py" that must be located in the same dir as this test file
# run in terminal: pytest -v test_pe3.py
# 25 tests should pass, 2 should fail with "XFAIL"

import pytest
import datetime
import string
from pe3 import *

# ------------------------
# Caesar Cipher Tests
# ------------------------

@pytest.mark.parametrize("in_text, shift, out_text", [
    ("", 3, ""),
    ("a", 3, "d"),
    ("A", 3, "D"),
    ("XyZ", 3, "AbC"),
    ("X!y.Z&", 3, "A!b.C&"),
    ("Calmly we walk on this April day", 10, "Mkvwvi go gkvu yx drsc Kzbsv nki")
])
def test_encode(in_text, shift, out_text):
    assert encode(in_text, shift)[1] == out_text

@pytest.mark.parametrize("in_text, shift, out_text", [
    ("", 3, ""),
    ("d", 3, "a"),
    ("A", 3, "X"),
    ("abc", 3, "xyz"),
    ("a!b.c&", 3, "x!y.z&"),
    ("mkvwvi go gkvu yx drsc kzbsv nki", 10, "calmly we walk on this april day")
])
def test_decode(in_text, shift, out_text):
    assert decode(in_text, shift) == out_text

def test_alphabet():
    assert encode("", 1)[0] == list(string.ascii_lowercase)

@pytest.mark.bankaccount
def test_zero_deposit():
    acc = BankAccount(balance=500)
    acc.deposit(0)
    assert acc.balance == 500  # Balance should remain the same
@pytest.mark.bankaccount
def test_exact_balance_withdraw():
    acc = BankAccount(balance=500)
    acc.withdraw(500)
    assert acc.balance == 0  # Should work without error

@pytest.mark.checkingaccount
def test_checking_account_multiple_overdrafts():
    acc = CheckingAccount(balance=100)
    acc.withdraw(150)  # Overdraft should apply a $30 fee
    assert acc.balance == -80  # -50 (withdrawal) - 30 (fee) = -80

@pytest.mark.checkingaccount
def test_checking_multiple_overdrafts():
    acc = CheckingAccount(balance=50)
    acc.withdraw(100)  # Overdraft should apply a $30 fee
    assert acc.balance == -80  # -50 (withdrawal) - 30 (fee) = -80

    acc.withdraw(50)  # Another overdraft, another $30 fee
    assert acc.balance == -160  # -50 (withdrawal) - 30 (fee) = -160

# ------------------------
# BankAccount Tests
# ------------------------

def test_deposit():
    acc = BankAccount(balance=100)
    acc.deposit(50)
    assert acc.balance == 150

def test_withdraw():
    acc = BankAccount(balance=100)
    acc.withdraw(50)
    assert acc.balance == 50

def test_negative_deposit():
    acc = BankAccount(balance=100)
    with pytest.raises(ValueError, match="Deposit amount cannot be negative."):
        acc.deposit(-10)

def test_insufficient_funds():
    acc = BankAccount(balance=100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        acc.withdraw(200)

def test_future_date():
    with pytest.raises(Exception, match="Creation date cannot be in the future."):
        BankAccount(creation_date=datetime.date.today() + datetime.timedelta(days=1))


# ------------------------
# SavingsAccount Tests
# ------------------------

def test_savings_withdraw():
    acc = SavingsAccount(balance=500, creation_date=datetime.date.today() - datetime.timedelta(days=181))
    acc.withdraw(200)
    assert acc.balance == 300

@pytest.mark.xfail(reason="Withdrawals are only permitted after 180 days")
def test_savings_early_withdraw():
    acc = SavingsAccount(balance=500, creation_date=datetime.date.today() - datetime.timedelta(days=179))
    acc.withdraw(200)


# ------------------------
# CheckingAccount Tests
# ------------------------

def test_checking_overdraft():
    acc = CheckingAccount(balance=500)
    acc.withdraw(600)  # Should allow overdraft and charge $30
    assert acc.balance == -130

def test_checking_normal_withdraw():
    acc = CheckingAccount(balance=500)
    acc.withdraw(300)  # Normal withdrawal
    assert acc.balance == 200

