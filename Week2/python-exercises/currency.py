import unittest

# write a method that takes in a number and returns it as a formatted string 
# for USD. Numbers should be rounded to nearest hundreth

def currency(value):
    pass

########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_currency_1(self):
        money = currency(100.238123123)
        self.assertEquals(money,'$100.24')


    def test_currency_2(self):
        money = currency(5.2)
        self.assertEquals(money,'$5.20')


if __name__ == '__main__':
    unittest.main()