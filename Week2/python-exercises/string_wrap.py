import unittest

# Write a method that takes in a starting character and the number of characters to return,
# and returns a string of letters from the alphabet.
# If a string would extend pass "z", it should "wrap around" back to "a" and continue from the beginning again.
# If the starting letter is lower case, the string should be lowercase.
# If the starting letter is upper case, the string should be uppercase.
# Hmm I know how to do this in C++ let me go look it up if anyone is around to listen - Alexi
# ok it's the same-ish
# ok 2 failures OH I KNOW IT'S NOT LOOPING BACK TO THE LETTERS
def wrap_around(s, n):
    wrap=""
    # First iteration failed 2 cases due to going past the unicode of the alphabet
    # # just need to change ord number back to ord(s) if past the unicode of the alphabet
    # for i in range(ord(s), ord(s) + n):
    #     wrap += chr(i)

    # return wrap
    for i in range(n)
        
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
