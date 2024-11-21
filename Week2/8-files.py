# we can Import resources from other files by using an import statement!

import sys 
sys.path.append("C:\\Revature\\2118-241111-Python\\trainer-code") # sys.path is a list of strings that specifies the search paths for modules
# print(sys.path)

# from _7_classes import Person # from a file/module we can import a functionality
import _7_classes as cla # we could also just import the entire file worth of content, and we're also creating an alias for it

Richard = cla.Person("Rich")
print(Richard)

# file interaction:
path = "./test.txt"

with open (path, "a") as file:
    file.write("Hello File" + '\n')