# Method Overriding

class A():
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "Instance variable in class A"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        super.__init__()
        self.var1 = "Inside B constructor"
        self.classvar1 = "Instance variable in class B"

a = A()
b = B()

# when we call a variable it finds instance variable in itself, then in parent class
# then it search for class variable in itself then class variale in parent class

