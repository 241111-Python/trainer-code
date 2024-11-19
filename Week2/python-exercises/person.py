import unittest
# write a person class that has the instance variables of name and age
# implement __init__ with the default argument for age as -1
# implement __str__ to give name and age in the following format 'Bill, 40 years old'
# additionally make a class variable that keeps track of the amount of people created

# Romeo is here too :)
# Martino is here LOL
# kene was here 
# Are we now implementing? gotcha
# i like cats
# I think we could. This is so fun I feel like  i
# Vitalii is here
class Person:
    #static variable
    amount = 1
    # init here!
    def __init__(self, name, age=-1):
        self.name = name
        self.age = age
        Person.amount += 1
        
    __str__str()


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_adam(self):
        print(1)
        adam = Person("Adam", 19)
        self.assertEqual(str(adam), "Adam, 19 years old")

    def test_richard(self):
        print(2)
        richard = Person("Richard", 22)
        self.assertEqual(str(richard), "Richard, 22 years old")

    def test_amount(self):
        print(3)
        self.assertEqual(Person.amount, 2)


if __name__ == "__main__":
    unittest.main()

    