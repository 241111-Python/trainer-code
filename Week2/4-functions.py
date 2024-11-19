def my_function(item):
    return

# functions need to be defined by the def keyword
#   need a name
#   need parameters (if any), or just the ()
#   : to open the body of the function
#   return keyword to close the function with a return, or pass keyword to continue on

def output(item, some_arg=3, separator="-") -> None: #the -> <type> is more for documentation than anything else
    try:
    #what are we attempting to run, that might have issues?
        iter(item)
        print(*item, sep=separator)

        #if we WANT to create an error/exception, we can use the 'raise' keyword

    except TypeError as e:
    #what do we do IF this listed type of error occurs?
        print(item)
    finally:
    #no matter what, do this...
        # return item
        pass

# python is interpreted! define your functions before you call them!
output("hi there")
output(item=[1,2,3,4,5], separator=",")
output()
# Error Handling with Try-Catch-Finally


# SCOPE - python uses 4 levels of scope
# 1 - Local - the stuff in the same function
# 2 - Enclosing - the values from the immediately surrounding/wrapping layer of application/function
# 3 - Global - values universally available within our program
# 4 - Built-In - values available for any python application