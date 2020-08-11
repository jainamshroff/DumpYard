# Multiple Inheritance

class Employee():

    numberofleaves = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}"

    @classmethod
    def changenumberofleaves(cls, newleaves):
        cls.numberofleaves = newleaves

    @classmethod
    def constructorfromdash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def justsomerandomfunction():
        print("Hello World, This Is A Static Function In Employee Class")


# Independent Class - independent from employee class
class Player():
    maxnumberofgames = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Name: {self.name}, Game: {self.game}"

# the class argument which is written first is used as constructor
# The order is important in the inheritance argument inside a class
class CoolProgrammer(Employee, Player):
    pass



jainam = Employee("Jainam", 500, "Instructor")
rohan = Employee("Rohan", 1000, "Manager")

shubham = Player("Shubham", ["Cricket", "Football", "Tennis"])
karan = CoolProgrammer("Karan", 10000, "CoolProgrammer")
print(karan.printdetails())

