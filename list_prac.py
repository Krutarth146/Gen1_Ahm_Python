list1 = []
print(type(list1))  # <class 'list'>

list2 = [10, 290.90, "str1", [(10,20,30),(403,12,1,2),(3,3,3)], {10,20,301,10}, {"Name" : "Krutarth", "Address" : {'City' : "Ahm", 'state' : "Guj"}}, 10, True]
print(list2)


print(len(list2))   # 8

print(list2[-4])
print(list2[4])

# List -> Ordered (Indexed), Allow Duplicates, Mutable (Changeble)

print(list2[2:])
print(list2[2::-1])  # ['str1', 290.9, 10]


list1 = [30,40,50,60,70,80]
print(type(list2[2:3]))   # List

# List Methods

# Add -> append, insert, extend

# Delete -> pop, pop(index), remove, del

# Add -> 1. Append()


list1.append(5000)
print(list1)  # [30, 40, 50, 60, 70, 80, 5000]


# list1.extend(5000)   # Gives Error

list1.extend("Jay")
print(list1)  # [30, 40, 50, 60, 70, 80, 5000, 'J', 'a', 'y']


list5 = [30,390, 80, 60, [10,20]]

# list1.append(list5)  # Len = 11
# print(list1)   # [30, 40, 50, 60, 70, 80, 5000, 'J', 'a', 'y', [30, 390, 80, 60, [10, 20]]]

# list1.extend(list5)  # len = 15
# print(list1)  # [30, 40, 50, 60, 70, 80, 5000, 'J', 'a', 'y', 30, 390, 80, 60, [10, 20]]


list1.insert(-1,4000)
print(list1)   # [30, 40, 50, 60, 70, 80, 5000, 'J', 'a', 4000, 'y']

list1[-1] = 8000
print(list1)  # [30, 40, 50, 60, 70, 80, 5000, 'J', 'a', 4000, 8000]

list1 += list5
print(id(list1))
print(list1)
print(id(list1))


ele = list1.pop(3)
print(ele)  # 60

list1.remove(5000)

print(list1)  # [30, 40, 50, 70, 80, 'J', 'a', 4000, 8000, 30, 390, 80, 60, [10, 20]]

# del list1
del list1[:]

print(list1)  # []


list2 = list1.copy()   # shallow Copy

 
list3 = list1   # Deep Copy


list3.append(5001)
print(list1)

list3= [20,10,10,10,45, 90,10]
print(list3.count(10))  # 4

list3.sort()
print(list3)  # [10, 10, 10, 10, 20]

list3.sort(reverse=True)
print(list3)  # [90, 45, 20, 10, 10, 10, 10]


print(type(range(5)))     # <class 'range'>


for i in list3:
    print(i,end= ' ')  # 90 45 20 10 10 10 10

for _ in range(len(list3)):
    print(list3[_])    # # 90 45 20 10 10 10 10


list1 = [[10,20,30], [40,50,60], [90,22,11]]

for i in list1: 
    print(i,end=' ')  # [10,20,30]  [40,50,60]   [90,22,11]

print()
for i in list1:  # [10,20,30]
    for d in i:
        print(d,end=' ')
    print()


print(list1[2][1])   # 22

# 10 20 30
# 40 50 60
# 90 22 11

# Transpose
for i in range(len(list1)):   # 0 1 2    i = 0
    for r in range(len(list1[i])):     # r = 1
        print(list1[r][i],end= ' ')    # list1[0][1]
    print()

# 10 40 90
# 20 50 22
# 30 60 11



# List Comprehensension

dim = int(input("ENter Dimensions: "))
main = []

# list4 = [[], [], []]

for i in range(dim):
    temp = [int(i) for i in input().split()]
    main.append(temp)

print(main)   # [[10, 20, 30], [40, 50, 66], [32, 55, 899]]


# Task : 

# 1. Snake -> 10 20 30 60 50 40 90 22 11 (4*4)
# 2. Sum of Diagonal -> 10 + 50 + 11 = ?   -> 30 + 50 + 90 = ?
# 3. Spiral -> 10 20 30 60 11 22 90 40 50


'''
Task-:
1. Create a list of Fruits(15 exotic fruits)
take user input and check if the fruits are avail in the list
if available print "fruit_name is Available"


2. create a list of numbers(15 numbers (1-100))
sort that list in ascending order
search for the number in the list
take input from user and find all the occurence
print the occurence


Tasks-: 
    1. Wap to find no. of month from the given no. of days
    2. wap to scan seconds and print hour, minute and remaining seconds
    3. wap to swap 3 numbers that is scanned by the user (a->b, b->c, c->a)
    4. wap to check whether the number is odd or even
    5. wap to find out the maximum, minimum, average of the numbers that is scanned by the user
    6. wap to make any user inputted string in uppercase or lowercase
    7. wap to print the sum of user entered numbers (scan by the user)
    8. wap to find power of a number
    9. wap to print numbers between n1 and n2 (n1, n2 are scanned by the user)
    
    Finale-: Make a Python program that generates a list of powers of base that is given by user upto the power given by user.    
    eg: base = 2, power=10
    output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

    10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

    11. A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

    12. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.

'''