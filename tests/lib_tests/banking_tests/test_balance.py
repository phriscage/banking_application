"""
    user models tests
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.dirname(
    os.path.realpath(__file__)) + '/../../../../../../lib/'))

class TestUserModel(unittest.TestCase):
    """ test the user model """


if __name__ == '__main__':
    unittest.main()

