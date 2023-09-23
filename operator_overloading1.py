# # Magic Methods (Dunder Methods)

# class Person:
#     def __init__(self, name1, marks1):
#         self.name = name1
#         self.marks = marks1

#     def Girnar(sf):
#         sf.Expense = 90000
#         print("Happy Journey",sf.Expense)

#     def add_marks(gh, other):
#         print(gh.marks + other.marks)

#     def __add__(gh,other):
#         print(gh.marks + other.marks)

#     def __lt__(gh,other):
#         return gh.marks < other.marks
    
#     def __ge__(gh,other):
#         return gh.marks >= other.marks

# param = Person("Param", 901)
# mitanshu = Person("Param", 901)

# param.Girnar()   # Happy Journey 90000


# print(89 + 67.90)   # 156.9
# print(89 + True)    # 90

# param.add_marks(mitanshu)   # 1802
# # param.+(mitanshu)
# param + mitanshu   # 1802
# print(param < mitanshu)    # False
# print(param >= mitanshu)   # True
# # param + mitanshu


list1 = [10,20,30, 99,33,22,11]


# x = list(map(lambda x: x+800, list1))

x = list(map(lambda x : x % 2, list1 ))
x = list(filter(lambda x : x % 2, list1 ))
print(x)   # [99, 33, 11]



# x = input().strip().split()

str1 = "Aman has 3 Rs. only."

print(str1.partition(' '))
print(str1.rpartition(' '))
print(str1.partition('A'))   # ('', 'A', 'man has 3 Rs. only.')
print(str1.split('A'))   # ['', 'man has 3 Rs. only.']

print(x)


print(list(map(int , input().strip().split())))


print([int(i) for i in input().split()])


# a=[1,2,3,4,5,(4,5),"u",{"w":45,"r":21},5]

# output
# 1
# 2
# 3
# 4
# 5
# tupel is: (4,5)
# dictonary keys:w
# dictonary values:45
# dictonary keys:r
# dictonary values:21
# 5