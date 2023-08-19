# Magic Methods (Dunder Methods)

class Person:
    def __init__(self, name1, marks1):
        self.name = name1
        self.marks = marks1

    def Girnar(sf):
        sf.Expense = 90000
        print("Happy Journey",sf.Expense)

    def add_marks(gh, other):
        print(gh.marks + other.marks)

    def __add__(gh,other):
        print(gh.marks + other.marks)

    def __lt__(gh,other):
        return gh.marks < other.marks
    
    def __ge__(gh,other):
        return gh.marks >= other.marks

param = Person("Param", 901)
mitanshu = Person("Param", 901)

param.Girnar()   # Happy Journey 90000


print(89 + 67.90)   # 156.9
print(89 + True)    # 90

param.add_marks(mitanshu)   # 1802
# param.+(mitanshu)
param + mitanshu   # 1802
print(param < mitanshu)    # False
print(param >= mitanshu)   # True
# param + mitanshu

