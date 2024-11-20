a_string = 'my string' 
b_string = "another string"
c_string = str(234) #str(<a value>) 

# we can treat a string line a collection of chars
# strings are enumerable (we can index through them)

# Strings are immutable - once a string is saved in memory (as a variable) we cannot modify it, only replace the entire string

# We can "slice" a string to return a sub string
# string[start:finish:step]
print(a_string[5])
print(a_string[1:7])
print(a_string[:5])
print(a_string[5:])
print(a_string[-4]) #slice from the end of the string, backwards
print(a_string[5:-3])
print(a_string[-6:])
print(a_string[::2]) #print every other character

print(a_string)
print(b_string)
ab_string = a_string + b_string
print(ab_string)

print(a_string.upper())
print(a_string.upper().isupper())

# a_string searching for "string"
print(a_string.find('string'))
print(a_string.find('another'))

r_string = ".somecontentthroughthemiddle$"
tmp = r_string[1:-1]
print(tmp)

# name:_Richard Hawkins_____
name = "____ Richard Hawkins    ___"
print(name.strip() + "|") # strip r and l
print(name.rstrip() + "|") # right strip
print(name.lstrip() + "|") # left strip
print(name.strip("_") + "|") # we can tell strip what character to remove

# Split breaks a string into a list of strings by some delimeter
print(b_string)
print(b_string.split(" "))
print(b_string.split())

my_list = list(b_string)
print(my_list)
# Join will "join" a set together on a delimeter
print(''.join(my_list)) # we're using the empty string to join together the element of my_list. it's the glue!
print(a_string * 4)