"""
    account class
"""
import locale
locale.setlocale(locale.LC_ALL, "")
from banking.balance import Balance

class Account(object):
    """ the account class contains the account operations """

    def __init__(self, name):
        """ instantiate the class """
        self.name = str(name)
        self.balance = Balance()

    def withdrawl(self, money):
        """ withdrawl the money from the balance if balance.total >= money
        Args:
            money (int): monetary value in cents
        """
        #if not self.balance.total >= money:
            #raise ValueError("I'm sorry but your balance is < '%s'", money)
        #self.balance.subtract(money)
        if self.balance.total >= money:
            self.balance.subtract(money)

    def deposit(self, money):
        """ deposit the money into the balance
        Args:
            money (int): monetary value in cents
        """
        self.balance.add(money)

    def get_balance(self):
        """ get the balance total
        Returns:
            self.balance.total (int): the balance total
        """
        return self.balance.total

    def get_currency(self):
        """ get the currency balance total
        Returns:
            locale.currency (str): the currency balance total
        """
        return locale.currency(float(self.get_balance) / 100.0)
