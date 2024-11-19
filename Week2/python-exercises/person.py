import unittest
# write a person class that has the instance variables of name and age
# implement __init__ with the default argument for age as -1
# implement __str__ to give name and age in the following format 'Bill, 40 years old'
# additionally make a class variable that keeps track of the amount of people created

class Person:
    pass



########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_adam(self):
        print(1)
        adam = Person('Adam',19)
        self.assertEqual(str(adam), 'Adam, 19 years old')

    def test_richard(self):
        print(2)
        richard = Person('Richard',22)
        self.assertEqual(str(richard), 'Richard, 22 years old')

    def test_amount(self):
        print(3)
        self.assertEqual(Person.amount, 2)


if __name__ == '__main__':
    unittest.main()
