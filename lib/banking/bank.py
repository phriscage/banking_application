"""
    bank class
"""
#pylint: disable=C0330
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../../lib')
from banking.customer import Customer
from banking.customers import Customers

class Bank(object):
    """ the bank class contains all the bank operations """

    def __init__(self, name):
        """ instantiate the class """
        self.name = str(name)
        self.customers = Customers()
        self.signup_customer(name)

    def signup_customer(self, name):
        """ signup a new customer to the bank """
        name = str(name)
        if not self.customers.get(name, None):
            self.customers[name] = Customer(name)

    def close_customer_account(self, name, account_type):
        """ close an account for a customer by name and account_type """
        customer = self.customers.get(str(name), None)
        if customer:
            customer.close_account(str(account_type))

    def cancel_customer_accounts(self, name):
        """ cancel customer account(s) and put balances in the bank savings """
        customer = self.customers.get(str(name), None)
        if customer:
            self.customers[self.name].create_account('savings')
            self.customers[self.name].deposit_into_account('savings',
                customer.get_account_totals())
            self.customers.pop(name, None)
