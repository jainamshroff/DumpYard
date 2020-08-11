# Public Protected Private types of variables

# You have a page with all your info
# Public - you want to share this paper with everyone, in public - stick outside home
# protected - you want to share this paper with only your family member - stick inside home
# private - you do not want to share this paper with anyone - keep it with you only - stick inside your closet

# if you want to keep a variable as protected you start it with protected
# if you want to make it private

# protected means base class can use it, and the class which is derived from it can use it
# to make a variable private we start its name with __ , to access it we have to use
# _classname__privatevariablename it is called name mangling

# public - any class anywhere can use it
# protected - only base class and child class and use it
# only the base class can use it that too with name mangling method

# print(emp._Employee__protectedvariable)

class Employee():

    numberofleaves = 10
    _protectedvariable = 100
    __privatevariable = 1000

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role


jainam = Employee("Jainam", 10050, "Instructor")

print(jainam.numberofleaves)
print(jainam._protectedvariable)
print(jainam._Employee__privatevariable)


