import unittest
# write a function that convernts a word into different casings
# assume no spacing
# snake_case example fire_truck OR Fire_Truck  (capitalization does not matter)
# camelCase example fireTruck
# PascalCase example FireTruck
# kebab-case example fire-truck

# casing('registeredUser','camelCase','kebab-case') -> registered-user
def to_kebab_case(words):
    words = [word.lower() for word in words]
    return "-".join(words)

def to_snake_case(words):
    return "_".join(words)

def to_camel_case(words):
    result = ""
    for idx, word in enumerate(words):
        if idx == 0:
            result += word.lower()
        else:
            result += word.capitalize()
    print("in to camel", result)
    return result

def to_pascal_case(words):
    result = to_camel_case(words)
    result = result[0].upper() + result[1:]
    return result

# casing('registeredUser','camelCase','kebab-case') -> registered-user
def casing(word, initial, target):
    words = []

    if initial == "kebab-case":
        words = word.split("-")
    elif initial == "snake_case":
        words = word.split("_")
    elif initial == "PascalCase" or initial == "camelCase":
        current_word = ""
        for idx, char in enumerate(word):
            # Encountered a capital character. New work
            if ord(char) < 97:
                if current_word:
                    words.append(current_word)
                current_word = str(char)
            else:
                current_word += char
        words.append(current_word)
        
    print(word, words, initial, target)

    result = ""
    if target == "kebab-case":
        result = to_kebab_case(words)
    elif target == "snake_case":
        result = to_snake_case(words)
    elif target == "PascalCase":
        result = to_pascal_case(words)
    elif target == "camelCase":
        result = to_camel_case(words)
    else:
        raise InvalidInput

    print(f"{result=}")

    return result


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_camel_to_Pascal(self):
        result = casing(word='redSphere',initial='camelCase',target='PascalCase')
        self.assertEqual(result,'RedSphere')

    def test_camel_to_kebab(self):
        result = casing('redSphere','camelCase','kebab-case')
        self.assertEqual(result,'red-sphere')

    def test_camel_to_snake(self):
        result = casing('redSphere','camelCase','snake_case')
        self.assertEqual(result,'red_Sphere')

    def test_Pascal_to_snake(self):
        result = casing('GreenApple','PascalCase','snake_case')
        self.assertEqual(result,'Green_Apple')

    def test_Pascal_to_kebab(self):
        result = casing('GreenApple','PascalCase','kebab-case')
        self.assertEqual(result,'green-apple')

    def test_Pascal_to_camel(self):
        result = casing('GreenApple','PascalCase','camelCase')
        self.assertEqual(result,'greenApple')

    def test_kebab_to_camel(self):
        result = casing('green-apple','kebab-case','camelCase')
        self.assertEqual(result,'greenApple')

    def test_kebab_to_Pascal(self):
        result = casing('green-apple','kebab-case','PascalCase')
        self.assertEqual(result,'GreenApple')   

    def test_kebab_to_snake(self):
        result = casing('green-apple','kebab-case','snake_case')
        self.assertEqual(result,'green_Apple') 
    
    def test_snake_to_camel(self):
        result = casing('green_apple','snake_case','camelCase')
        self.assertEqual(result,'greenApple') 
    
    def test_snake_to_Pascal(self):
        result = casing('green_apple','snake_case','PascalCase')
        self.assertEqual(result,'GreenApple') 
    
    def test_snake_to_kebab(self):
        result = casing('green_apple','snake_case','kebab-case')
        self.assertEqual(result,'green-apple') 

if __name__ == '__main__':
    unittest.main()