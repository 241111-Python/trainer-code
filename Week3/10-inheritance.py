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

class Employee(Person): # Here, we create an Employee class that inherits from Person

    # Employee still needs a constructor that takes in self, as well as all arguments for the 
    # person constructor. 
    def __init__(self, name, employee_id, department):
        # We need to call the parent class's constructor from our child class's constructor
        # We do that with super()
        super().__init__(name)
        self.employee_id = employee_id
        self.department = department
        self.salary = 0

    def set_salary(self, new_salary):
        self.salary = new_salary
    
    def __str__(self):
        return f'{self.name}: {self.department}, Salary: {self.salary}'


# Anything in this condition, only run if the module is being directly run, not if it's imported
if __name__ == '__main__':

    # Working with the Person parent class, just like before
    person_obj = Person("Romeo")
    person_obj.job = "Trainee"
    person_obj.print_name()
    print(person_obj)

    employee_obj = Employee("Andrew", "A-12345", "Engineering")
    print(employee_obj)
    
    employee_obj.print_name()

