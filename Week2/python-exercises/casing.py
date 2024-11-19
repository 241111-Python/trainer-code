import unittest
# write a function that convernts a word into different casings
# assume no spacing
# snake_case example fire_truck OR Fire_Truck  (capitalization does not matter)
# camelCase example fireTruck
# PascalCase example FireTruck
# kebab-case example fire-truck

# casing('registeredUser','camelCase','kebab-case') -> registered-user
def casing(word, initial, target):
    pass


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_camel_to_Pascal(self):
        result = casing(word='redSphere',initial='camelCase',target='PascalCase')
        self.assertEquals(result,'RedSphere')

    def test_camel_to_kebab(self):
        result = casing('redSphere','camelCase','kebab-case')
        self.assertEquals(result,'red-sphere')

    def test_camel_to_snake(self):
        result = casing('redSphere','camelCase','snake_case')
        self.assertEquals(result,'red_Sphere')


    def test_Pascal_to_snake(self):
        result = casing('GreenApple','PascalCase','snake_case')
        self.assertEquals(result,'Green_Apple')

    def test_Pascal_to_kebab(self):
        result = casing('GreenApple','PascalCase','kebab-case')
        self.assertEquals(result,'green-apple')

    def test_Pascal_to_camel(self):
        result = casing('GreenApple','PascalCase','camelCase')
        self.assertEquals(result,'greenApple')
    

    def test_kebab_to_camel(self):
        result = casing('green-apple','kebab-case','camelCase')
        self.assertEquals(result,'greenApple')

    def test_kebab_to_Pascal(self):
        result = casing('green-apple','kebab-case','PascalCase')
        self.assertEquals(result,'GreenApple')   

    def test_kebab_to_snake(self):
        result = casing('green-apple','kebab-case','snake_case')
        self.assertEquals(result,'green_Apple') 
    

    def test_snake_to_camel(self):
        result = casing('green_apple','snake_case','camelCase')
        self.assertEquals(result,'greenApple') 
    
    def test_snake_to_Pascal(self):
        result = casing('green_apple','snake_case','PascalCase')
        self.assertEquals(result,'GreenApple') 
    
    def test_snake_to_kebab(self):
        result = casing('green_apple','snake_case','kebab-case')
        self.assertEquals(result,'green-apple') 

if __name__ == '__main__':
    unittest.main()