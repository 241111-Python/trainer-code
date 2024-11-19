# loops

# for and while
loop_flag = True

while loop_flag:
    loop_flag = False
    print("still going...")

# break - exit out of a loop
# continue - move to the next iteration of the loop

while input('enter x to exit: ') != 'x':
    print('going again')

# for loops in python will iterate over a range
# range(<min>, <max>, <step>)
for i in range(0, 5, 1):
    print(i)

# range is a sequence data type/function
# it's lazy - it does not precompute the values, it calculates the values on demand
print("new loop!")
# usually, we don't use range, and we find a way to iterate over a collection
#comprehension syntax - no iterator/index
sequence = [ 5, 3, 1 ]
for i in sequence:
    print(i)

print("new loop!")
for i, item in enumerate(sequence):
    if i > 0:
        print(i, ": ", item)
        

 




# conditionals
# if, else if, else

user_selection = int(input('Enter a number: ')) # type casting our input to an int
if user_selection == 0:
    print('it was zero')
elif user_selection > 0:
    print('it was positive')
elif user_selection < 0:
    print('it was negative')
else:
    user_selection = "you didn't enter a number"

print(user_selection)