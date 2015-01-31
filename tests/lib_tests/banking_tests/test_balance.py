"""
    balance models tests
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.dirname(
    os.path.realpath(__file__)) + '/../../../lib/'))

from banking.balance import Balance

class TestBalanceAdd(unittest.TestCase):
    """ test the balance add method """

    @classmethod
    def setUp(self):
        """ bootstrap each test fixture """
        self.balance = Balance()

    def test_integer_value(self):
        """ test_integer_value """
        self.balance.add(1)
        self.assertEquals(self.balance.total, 1)

    def test_negative_integer_value(self):
        """ test_negative_integer_value """
        self.balance.add(-1)
        self.assertEquals(self.balance.total, -1)

    def test_string_integer_value(self):
        """ test_string_integer_value """
        self.balance.add('1')
        self.assertEquals(self.balance.total, 1)

    def test_string_value(self):
        """ test_string_value """
        self.assertRaises(ValueError, self.balance.add, 'a')


class TestBalanceSubtract(unittest.TestCase):
    """ test the balance subtract method """

    @classmethod
    def setUp(self):
        """ bootstrap each test fixture """
        self.balance = Balance()

    def test_integer_value(self):
        """ test_integer_value """
        self.balance.subtract(1)
        self.assertEquals(self.balance.total, -1)

    def test_negative_integer_value(self):
        """ test_negative_integer_value """
        self.balance.subtract(-1)
        self.assertEquals(self.balance.total, 1)

    def test_string_integer_value(self):
        """ test_string_integer_value """
        self.balance.subtract('1')
        self.assertEquals(self.balance.total, -1)

    def test_string_value(self):
        """ test_string_value """
        self.assertRaises(ValueError, self.balance.subtract, 'a')


if __name__ == '__main__':
    unittest.main()

