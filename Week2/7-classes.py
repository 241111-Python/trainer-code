# classes defines state and behavior for an object
# it acts as the blueprint for the type object 

class Person:

    # constructor method defines how to create an object of this class type
    # "dunder methods" -> double underscore methods/ magic methods
    def __init__(self, name):
        self.name = name # not private
        self.__identifier = name # private

    def print_name(self):
        print(self.__identifier)

    def __str__(self):
        return f'{self.name}: {self.job}'
    
    def __eq__(self, other):
        return self.__identifier == other.__identifier


# anying in this condition, only run if the module is being directly run, not if it's imported
if __name__ == '__main__':
    new_person = Person("Dallas")

    new_person.print_name()
    # print(new_person.__identifier) # won't work, becuase __identiefer is not public!
    new_person.job = "Associate"
    print(new_person.job)
    new_person.experience = 10

    print(new_person)

    new_person.experience += 10
    print(new_person.experience)

    for key, value in new_person.__dict__.items():
        print(key, value)

    print(new_person.__dict__)
    print( vars(new_person))