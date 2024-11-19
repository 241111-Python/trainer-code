import unittest

# Write a method that takes in a starting character and the number of characters to return,
# and returns a string of letters from the alphabet.
# If a string would extend pass "z", it should "wrap around" back to "a" and continue from the beginning again.
# If the starting letter is lower case, the string should be lowercase.
# If the starting letter is upper case, the string should be uppercase.

def wrap_around(s, n):
    pass

########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_string_wrap_1(self):
        result = wrap_around('a', 5)
        self.assertEqual(result, 'abcde')
        
    def test_string_wrap_2(self):
        result = wrap_around('x', 6)
        self.assertEqual(result, 'xyzabc')
    
    def test_string_wrap_3(self):
        result = wrap_around('G', 10)
        self.assertEqual(result, 'GHIJKLMNOP')
    
    def test_string_wrap_4(self):
        result = wrap_around('A', 60)
        self.assertEqual(result, 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGH')
    

if __name__ == '__main__':
    unittest.main()
