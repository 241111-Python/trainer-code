def my_function(item):
    return

# functions need to be defined by the def keyword
#   need a name
#   need parameters (if any), or just the ()
#   : to open the body of the function
#   return keyword to close the function with a return, or pass keyword to continue on

def output(item, some_arg=3, separator="-"):
    try:
    #what are we attempting to run, that might have issues?
        iter(item)
        print(*item, sep=separator)

    except TypeError as e:
    #what do we do IF this listed type of error occurs?
        print(item)
    finally:
    #no matter what, do this...
        pass

# python is interpreted! define your functions before you call them!
output("hi there")
output(3)
output()
# Error Handling with Try-Catch-Finally