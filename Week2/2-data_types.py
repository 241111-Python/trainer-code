print("hello world")

# comments in python are noted by the "#"

# Variables
# Number formats/ numerica data types
# int, float

x = 2 + 5

y = 10.5 # y is a float
z: float = 10
# Be CAREFUL of data loss in conversion!

# aritmatic operators
# - + / * % - modulo/modulus: the remainder of division
# ++ / -- - +1/-1 notation
# += / -= - x += 1 : as close as we get
# ** - exponent (to the power of)
# // - integer division - divides to the whole number
print( 5 / 2 ) #2.5
print( 5 // 2 ) #2

# Logical and comparison operators
# and or not
# > < == != >= <=  

# boolean type use True and False
print( True or False ) # True
print( True and False ) # False
print( True or not False ) # !true
print( True and not False ) # 

# strings
# functionally, we can declare a string with " or ' quote
# we may NEED double quotes to escape single quote in the string
my_string = "this is a string"
my_second_string = 'this is also a string'

# indexing through a string with [#]
my_character = my_string[0] # == 't'
multi_line_string = ''' this
is 
a
multi
line
string'''

# the 'in' operator lets us check for membership
print( 'is' in multi_line_string ) # True
