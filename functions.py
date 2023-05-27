# STL -> standard Template Lib. 1. Algorithms   2. Containers  3. Iterators

# Functions

# 1. Inbuilt
# 2. User Defined

# Functions

# 1. Func. Defination
# 2. Func. Calling

# Func. Types 
# 1. without args without return Type
# 2. with args without return Type
# 3. without args with return Type
# 4. with args with return Type

# 1. without args without return Type


# void sum()
# {
#     // statements
# }

def royal():   # func. Defination
    print("This is Royal Func.")
    print(20+30)


royal()   # 50

# 2. with args without return Type

def devanshu(x,y,z):
    print(x,y,z)

devanshu(10, "Dj", 90.89)  # 10 Dj 90.89


# 3. without args with return Type

def ronit():
    return 43+12,89-12

x = ronit()
print(x)   # 55

print(ronit())  # 55




# 4. with args with return Type

def param(_, _1):
    return _ + _1


print(param(20,90))  # 110


def series(num):
    for i in range(num):  # 0 to 4
        yield i
    

for i in series(5):
    print(i)

def kamble(x,y,z=None):
    print(x,y,z)
# print(y)  # error
kamble("mm",'rr','yy')


def jay(x,y,*kru,q=0):
    print(kru)
    for i in kru:
        print(i)


jay(10,90.89,"str1",[10,20])   # (10, 90.89, 'str1')


# kwargs ---> Dictionary

# key, value

dict1 = {"Name" : "Krutarth", "Roll" : 678, 'list1' : [10,20,30,40,90]}

print(dict1)  # {'Name': 'Krutarth', 'Roll': 678, 'list1': [10, 20, 30, 40, 90]}

def yash(*args,**kamble):
    print(kamble) 

    for i in kamble.keys():
        print(i)
    for i in kamble.values():
        print(i)
    for i in kamble.items():
        print(i)

yash(10,20,30,name="Jay", roll = 70, school = "hbk")   # {'name': 'Jay', 'roll': 70, 'school': 'hbk'}


# Lambda 
# (Anounomus Function)

def square(num):
    return num ** 2

print(square(4))   # 16

square_lam = lambda x : x**2

print(square_lam(50))   # 2500


# Quadratic Function  

# (a*(x**2) + b*x + c)

def quadratic_fun(a,b,c):
    return lambda x : (a*(x**2) + b*x + c)

dhiraj_sir = quadratic_fun(10,20,30)
  
print(dhiraj_sir(5))   # 380


# func. refer, lambda 15 Programs
