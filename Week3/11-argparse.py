# To work with argparse we just import it
import argparse

# Creating some methods to call 
def method_one():
    print("You selected Method 1!")

def method_two():
    print("Method 2 selected!!")

def method_three():
    print("You've hit method 3!!!")

# This method will load/read text in from an outside file.
# The filepath to that file will be supplied by an arg
def load_user_file(filepath_arg):
    try:
        with open(filepath_arg, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filepath_arg}' does not exist!")



# Here is my main. 
if __name__ == "__main__":
    # A confirmation that we have hit main.
    print("Main code executed!")

    # Creating our parser, the name can be whatever you want. We want to be self-documenting though.
    my_parser = argparse.ArgumentParser(description="A demo for argparser!")

    # Here I added a --method argument. If the user types --method followed by "one" "two" or "three"
    # We will run one of the methods above. 
    my_parser.add_argument("--method", type=str, choices=["one", "two", "three"], help="Selecting a method to run.")

    my_parser.add_argument("--load-file", type=str, help="Load data/text from a specified file.")

    # Once we've added all of the arguments we want to handle, we have the parser parse the arguments. 
    user_args = my_parser.parse_args()

    # Since we don't know what arguments are actually going to be passed in by the user when this runs, 
    # we store any potential args in a variable. In our case, user_args above. 

    if user_args.load_file:
        print(f'Loading from {user_args.load_file}')
        load_user_file(user_args.load_file)


    if user_args.method:

        if user_args.method == "one":
            method_one()
        elif user_args.method == "two":
            method_two()
        elif user_args.method == "three":
            method_three()