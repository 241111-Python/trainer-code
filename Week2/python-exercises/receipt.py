import unittest
# write a method that takes in a sales tax as the first argument
# then takes in varargs of tuples with the name of the item and its base cost
# it should return a list of dictionaries ordered by cost descending
# purchases(10,('shoes',15),('apple',1),('stapler',11))
# -> [{'item':'shoes','base':15,'taxed':16.50},
# {'item':'stapler','base':11,'taxed':12.10},
# {'item':'apple','base':1,'taxed':1.10}]
def purchases(tax,*items):
    pass


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_add_1(self):
        result = purchases(5,('soda',12),('pop rocks',2),('steak',35))
        expected = [
        {'item':'steak','base':35,'taxed':36.75},
        {'item':'soda','base':12,'taxed':12.6}, 
        {'item':'pop rocks','base':2,'taxed':2.1}
        ]
        self.assertListEqual(result,expected)

    def test_add_2(self):
        result = purchases(15,('ginger ale',12),('ice cream',9),('pork chops',21))
        expected = [
        {'item':'pork chops','base':21,'taxed':24.15},
        {'item':'ginger ale','base':12,'taxed':13.8}, 
        {'item':'ice cream','base':9,'taxed':10.35}
        ]
        self.assertListEqual(result,expected)


if __name__ == '__main__':
    unittest.main()