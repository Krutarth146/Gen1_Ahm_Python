# Poly ---> Many
# Morph ---> Forms

# right ---> left-right, right-wrong
# len() ---> 

print(len([10,20,30,]))  # 3
print(len("Param"))   # 5
print(len((10,20,30,[20,30])))   # 4

def fun1():
    print("This is fun1")

def fun1(n1,n2):
    print("This is fun1 with args",n1+n2)

fun1(40,90)


class Royal:
    def __init__(self):
        self.students = 500

    def fun1(ml):
        ml.temp = 9000
        print("This is fun1 Under Royal")


class Infosys(Royal):
    def fun1(df):   # Method Overriding  (Requires Inheritance)
        # super().fun1()
        Royal.fun1(df)
        df.xerox = 700
        print("This is fun1 Under Infosys")

    def fun2(dr):
        print("This is fun2")

    def fun2(sa, n1,n2):    # Method Overloading ()
        print("This is fun2 with args")

Jay = Infosys()   # Jay is object

Jay.fun1()

list1 = [Royal(), Infosys()]
print(list1)   # [<__main__.Royal object at 0x000001E35ABD7430>, <__main__.Infosys object at 0x000001E35ABD7FD0>]


for i in list1:
    i.fun1()

Jay.fun2(20,30)
Jay.fun2()