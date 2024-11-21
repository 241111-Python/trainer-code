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

with open (path, "w") as file:
    file.write("Hello File" + '\n')


# The following code was generously donated by Team Steak

import csv

text_file = "textfile.txt"
data_source = "./stock-data./AAPL_data.csv"
output_file = "stockdata.txt"

# Reading the whole file into 1 string
print("File contents in one string: ")
with open (text_file, "r") as file:
  my_string = file.read()
file.close()
print(my_string)

print("------------------------------------------\n")

# Reading a file into a list of lines
print("Reading line by line into a list: ")
linesArray = []
with open (text_file, "r") as file:
  for line in file:
    linesArray.append(line.strip())
print(linesArray)

print("------------------------------------------\n")

with open (text_file, "r") as file:
    lines = [line.strip() for line in file.readlines()]
print(f'Using readlines: {lines}')    

print("------------------------------------------\n")

# Different way
print("Another way: ")
temp = open(text_file,'r').read().split('\n')
print(temp)

print("------------------------------------------\n")

# Reading csv file
with open (data_source, "r") as file:
    lines = [line.strip().split(",") for line in file.readlines()]
print(f'Using readlines: {lines}') 

# Either read into a collection (line by line) OR split the string by new lines

# Writing a file
with open (output_file, "w") as file:
    writer = csv.writer(file)
    writer.writerow(lines[1])
file.close()