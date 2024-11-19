import unittest

def add(num1,num2):
    return num1 + num2


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_add_1(self):
        sum = add(2,2)
        assert sum == 4

    def test_add_2(self):
        sum = add(45,17)
        assert sum == 62


if __name__ == '__main__':
    unittest.main()
