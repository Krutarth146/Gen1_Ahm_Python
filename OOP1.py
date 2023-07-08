#  OOP  ----> class, Object


# class Param
# {
#     int id;
#     float sal;
#     char name[10];


#     void set_data()
#     {
#         scanf();
#     }

#     void display()
#     {
#         printf();
#     }

# };


# Constructor ---> TO Intialize Member Variable

# main()
# {
#     int    num;
#     Param p1;
# }
    # Bank()
    # {

    # }


# self --- > this

class Bank:
    ROI = 4   # class Variable

    def __init__(self):
        self.name = input("Enter Name: ")   # Instance Variable
        self.id = int(input("Id: "))
        self.balance = 0

    def print_details(self):
        print(self.name, self.id, self.balance)

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount


    @classmethod
    def change_ROI(cls):
        cls.ROI = 10


    # ROI ---> Calc. Interest

# Bank b1;

mitanshu = Bank()
pratik = Bank()

mitanshu.deposit(5000)
mitanshu.withdraw(400)
mitanshu.print_details()

pratik.deposit(6000)
pratik.withdraw(100)
pratik.print_details()

