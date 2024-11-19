import unittest

# the analyze function takes in an var arguent of numbers
# it should return a dicitonary of {'mean':0,'median':0,'mode':0,'largest':0,'smallest':0}
def analyze(*nums):
    pass

########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_analyze_1(self):
        data = analyze(1,2,2,2,3)
        self.assertDictEqual(data, {'mean':2,'median':2,'mode':2, 'largest':3,'smallest':1})
        

    def test_analyze_2(self):
        data = analyze(10,5,10,200,-65)
        self.assertDictEqual(data, {'mean':32,'median':10,'mode':10, 'largest':200,'smallest':-65})
        


if __name__ == '__main__':
    unittest.main()
