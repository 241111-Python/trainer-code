import unittest

# write a method that takes in a number and returns it as a formatted string 
# for USD. Numbers should be rounded to nearest hundreth

def currency(value):
    return f"${value:.2f}"        

########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_currency_1(self):
        money = currency(100.238123123)
        self.assertEqual(money,'$100.24')


    def test_currency_2(self):
        money = currency(5.2)
        self.assertEqual(money,'$5.20')


if __name__ == '__main__':
    unittest.main()