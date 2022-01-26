import unittest
from modules.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.pair1 = Calculator(1, 1)

    def mytest(self):
        self.assertEqual(True, True)