"""
    balance class
"""

class Balance(object):
    """ the balance class includes the balance operations """

    def __init__(self):
        """ instantiate the class """
        self.total = 0

    def add(self, value):
        """ add value to the total
        Args:
            value (int): numeric value
        """
        value = int(value)
        self.total += value

    def subtract(self, value):
        """ subtract value from the total
        Args:
            value (int): numeric value
        """
        value = int(value)
        self.total -= value
