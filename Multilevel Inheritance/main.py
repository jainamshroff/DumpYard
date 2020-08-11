# Multilevel Inheritance

class Dad():
    basketball = 1

class Son(Dad):
    dance = 1

    def isdance(self):
        return f"Yes I Dance {self.dance} number of times"

class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"Yes I Dance Very Awesomely {self.dance} number of times"


darry = Dad()
larry = Son()
harry = Grandson()


print(harry.basketball)