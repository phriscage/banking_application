"""
    customer class
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../../lib')
from banking.name import Name
from banking.account import Account
from banking.accounts import Accounts

class Customer(object):
    """ the customer class includes """

    def __init__(self, name):
        """ instantiate the customer """
        self.name = Name(name)
        self.accounts = Accounts()

    def create_account(self, account_type):
        """ add a new account by account_type """
        account_type = str(account_type)
        if not self.accounts.get(account_type, None):
            self.accounts[account_type] = Account(account_type)

    def close_account(self, account_type):
        """ close a account by account_type """
        self.accounts.pop(str(account_type), None)

    def deposit_into_account(self, account_type, money):
        """ deposit money into account by account_type """
        account = self.accounts.get(str(account_type), None)
        if account:
            account.deposit(money)

    def withdrawl_from_account(self, account_type, money):
        """ withdrawl money from account by account_type """
        account = self.accounts.get(str(account_type), None)
        if account:
            account.withdrawl(money)

    def get_account_totals(self):
        """ get the totals for all accounts """
        return sum((account.get_balance for account in self.accounts.values()))
