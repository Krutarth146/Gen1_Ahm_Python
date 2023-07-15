class Royal():
    _faculties = 10   # protected class Variable
    __bank_balance = 10000000000000  # Private

    def __init__(self,fees, name):
        self.fees = fees  # public instance Variable 
        self.name = name

    def print_details(self):  # INstance
        print(self._faculties)   # 10
        self._faculties = 60
        print(self._faculties)   # 60
        print(Royal._faculties)  # 10
        print("Student's Name is",self.name,"Student's fees are",self.fees)

    @classmethod
    def add_money(cls, money):  # class Method
        return cls.__bank_balance + money
    


jay = Royal(500, "Jay V.")
jay.print_details()
print(jay.fees)  # 500
# print(jay.faculties)  # Error
try: 
    print(jay.faculties)  # 10
except:
    print("Sorry, Not Accessible")

print(jay._faculties)  # 10
# print(jay.bank_balance)     # Error
# print(jay.__bank_balance)   # Error
print(jay._Royal__bank_balance)   # 10000000000000
print(jay.add_money(5000))   # 10000000005000
print(Royal.add_money(90000))