# print("Hello")

# try:
#     # print(32//0)
#     # print(int('a'))
#     print('Manoj')   # Error

# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ArithmeticError:
#     print('Arithmetic Error')
# except Exception as e:
#     print('General Exception Occured',e)   # printa is Not Defined name 'printa' is not defined
# else:
#     print('Else Block Executed')
# finally:
#     print('This Block is Always Executed')

# print('Outside try block')



# print('Manoj2')
# print('Manoj1')


# for i in range(10):
#     if i==15:
#         break
#     print(i)
# else:
#     print('Else Block is Executed')

# # printa(89/0)

# # print("Hello")

# # IOError
# # AttributeError
# # Import Error
# # Value Error
# # Type Error  # 5 + "Dhruv"
# # Name Error
# # Syntax Error
# # Zero Division
# # Index Error

# # Exception: when program is syntatically correct but code results in Error.


# num = 90
# name = "Dhruv"

# try:
#     ans = num + name
# except TypeError:
#     print("Error: can not add int + str")


# print("Hello")


# # ----------------------

# list1 = [10,900,89]

# try:
#     # print("%d" %(list1[1]/0))
#     # print("%d" %(list1[8]))
#     print("%d" %(list1[-1]//0))
# # except ValueError:
# #     print("Value Error")
# except IndexError:
#     print("Index Error")
# except ZeroDivisionError:
#     print("Not Divisible By 0")
# except:
#     print("Error Generated")
# else:
#     print("Dhruv Panwala")

# finally:
#     print("Always Executed")

# # print("Hello")


# # try:
#     # raise NameError("Name Errrorrrrrrrrrrrrrrr")
# # except NameError:
#     # print("An Exception")
#     # raise


# # ------------------------------------------------


# # Built-in Exceptions

# # def factorial(num):
# #     mul = 1
# #     for i in range(1,num+1):
# #         mul = mul * i
# #         yield mul   # Generator

# # for j in factorial(5):
# #     print(j)



# def gener1():
#     try:
#         for i in range(5):
#             print("yeilding", i)
#             yield i
#     except GeneratorExit:
#         print("Exiting Early")

# g1 = gener1()

# print(type(g1))  # <class 'generator'>
# print (g1.__next__())
# print (g1.__next__())
# print (g1.__next__())
# g1.close()


# # In file 
# import os

# def create_file(filename):
#     try:
#         with open(filename,'w') as f:
#             f.write("Hello World")
#     except IOError:
#         print("Could not create a file")


# def read_file(filename):
#     try:
#         with open(filename,'r') as f1:
#             x = f1.read()
#             print(x)
#     except IOError:
#         print("Could Not Read a File")

# def deletefile(old_file_name, new_file_name):
#     try:
#         # os.remove(filename)
#         os.rename(old_file_name, new_file_name)
#         print("File successfully Deleted.")
#     except IOError:
#         print("Could not Delete a File")

# if __name__ == '__main__':
#     filename = "dhruv.txt"
#     create_file(filename)
#     read_file(filename)
#     deletefile(filename)


# def indexing(list1):

#     try:
#         print(list1[21])
#     except LookupError:
#         print("Index out of Range")
#     else:
#         print("success")

# indexing([10,20,30])


# # Inbulit, User Defined, nzec Error

# # # import math

# # # print(math.exp(10.90))  # 54176.36379669875
# # # print(math.exp(1000))  # 54176.36379669875


# # dict1 = {'a' : 'Akbar'}

# # try:
# #     print(dict1['a'])

# # # except Exception as err:
# # except Exception as err:
# #     print(err)
# # else:
# #     print("successfully run")

# # # def func():
# # #     print(name)

# # # func()



# # # User Defined Exception


# class Error(Exception):
#     """Base class for other Exceptions"""
#     pass


# class DhruvZeroDivision(Error):
#     pass

# try:
#     num = int(input("Enter Number : "))
#     if num == 0:
#         # num / 0
#         raise DhruvZeroDivision


# # except ZeroDivisionError:
# #     print("Inbuilt Zero Division Error")


# except DhruvZeroDivision:
#     print("Input Value is Zero")

# # except Exception as e:
#     print("Inbilt Error: ",e)

# # e1 = Error()
# # print(e1.__doc__)




# # def print_details(num):
# #     for i in range(num):
# #         yield i


# # for i in print_details(5):
# #     print(i)






# l3 = [3,3,4,5,56,21,2,22,4,45,5,6]

# dict1 = {}


# unique = []

# for i in l3:
#     if i not in unique:
#         unique.append(i)

# for element in unique:   # element = 3
#     temp = []
#     for ind in range(len(l3)):  # j ---> 0 to 11
#         if element == l3[ind]:  # 3 == 3
#             temp.append(l3.index(element,ind))   # [0,1]

#     dict1[element] = temp

# print(dict1)   # {3: [0, 1], 4: [2, 8], 5: [3, 10], 56: [4], 21: [5], 2: [6], 22: [7], 45: [9], 6: [11]}

# dict2 = {element : [ind for ind in range(len(l3)) if element == l3[ind]] for element in set(l3)}
# print(dict2)
# # x = 0
# # c = 0.0
# # temp = {}
# # temp = set()
# # temp = []

# # {3 : [0,1], 4 : [2,8]}


# # list1 = [10,20,30,10,10]

# # print(list1.index(10,1))
# # print(list1.index(10))


# list1 = [(390,10), (32,45) ,(21,34), (33,8), (23,2)]


# for i in range(len(list1)):   # i = (390,10)
#     for j in range(i+1,len(list1)):
#         if list1[i][1] > list1[j][1]:   # 10 > 45
#             list1[i], list1[j] = list1[j], list1[i]

# print(list1)   # [(23, 2), (33, 8), (390, 10), (21, 34), (32, 45)]


# 90  + 89



# print(e1 + e2)


# class Error():
#     def __add__(self,e2):
#         return self.temp + e2.temp
    

# e1 = Error()
# e2 = Error()

# e3 = e1.sum(e2)
#      e1 + e2

# 2 + 3


dict1 = {10:90, 'Name' : 'Aman', 'add' : 'Ahm'}


# for i,j in dict1.items():

#     if type(j) == int:
#         print('int')
#     print('Dict1 Key: ',i)
#     print('Dict1 Value: ',j)


s1 = set()

print(s1)

if type(dict1) == dict:
    print(True)