# collections are a group of related objects


# type          mutable, duplicate, enumarable/indexable/ordered
# list          yes         yes         yes
# tuple        no          yes         yes
# dictionary    yes         no - keys   yes (since 3.7)
# set           yes         no          no

# mutable - we can change the value of the object in memmory without replacing the whole thing.
new_list = [ 4, 8, 2, 6]
new_list[0] = 0

# immutable - we must replace the whole object in memory to modify it
my_string = 'some string'
# my_string[6] = "k"


# Lists
data_l = [0,2,4,6,8]
data_l[0] = 1
data_l.append(10)
data_l += [3,5,7]
print(data_l)

nested_list = [1, [2, 4, 6], 3]
print(nested_list)
nested_list[2] = [9,8,7]
print(nested_list)
print(nested_list[1][2])

# Sorting
print()
print(nested_list)
print(sorted(nested_list[2])) # sorted returns a sorted list, but doesn't change the original order
nested_list[2].sort() # .sort() sorts in place
print(nested_list)


# Tuples
# immutable, so we can use it as a dictionary key
data_t = ('abc', 3, 19)
data_tup = tuple(data_l)

for (i, item) in enumerate(data_t):
    print(f' {i} : {item}')
    
# Set
# unique values allows us to leverage hashtables for reference,
# which is a much faster way to return the values to our application
usernames = set()
usernames = { 'rich', 'russell', 'rachel' }
usernames.add( 'Trey' )
# usernames.remove( 'dallas' ) # removing a value that is not part of the set will throw an error
usernames.discard( 'dallas' ) # discarding a value that is not part of the set will discard or not, without throwing an error

print( 'Romeo' in usernames ) # check for membership
print(usernames)
print(usernames.pop()) # pop returns a value from the set, and removes that entry from the set
print(usernames)


# dictionary
my_dictionary = {} # a dictionary, not a set

# dictionaries need to pair keys and values
my_dictionary = {
    'rich' : 33,
    'russell' : 28,
    'andrew' : 25
}

print(my_dictionary)
print(my_dictionary['andrew'])

print(my_dictionary.keys())
print(my_dictionary.values())

for key in my_dictionary:
    print(f'{key}')
for value in my_dictionary.values():
    print(f'{value}')
for key, value in my_dictionary.items():
    print(f'{key} : {value}')

print(my_dictionary.get('saad', None)) # find the value at the key, or return a default

my_dictionary.update({'rich':34}) # update a value by referencing the key
print(my_dictionary['rich'])

my_dictionary.update({'john' : 27}) # use update to add a new key/value pair
print(my_dictionary['john'])


# comprehension gives us a shorthand to applying a behavior to a collection and gathering the results into a new collection

base = [2,3,4,5]
squared = [i** 2 for i in base]

# for i in base:
#     squared.append(i * i)

print(squared)

collection = [ x * y for x in base for y in base if x != 0]
# for x in base:
#     for y in base: 
#         if x != 0:
#             collection.append(x*y)
print(collection)

print(base) # base is treated as a collection
print(*base) # base is treated as individual values
