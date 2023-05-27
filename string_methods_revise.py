str1 = 'Aman'
str2 = "Palak"
str3 = 'M'

print(type(str1))
print(type(str2))
print(type(str3))

print(len(str1))  # 4  -> Length starts from 1
str1 = "ROyal_is Best Institute Ever123."


# Indexing
print(str1[3])  # a
print(str1[-2])  # 3

# Slicing

# print(str1[start : end(n-1) : step])
str1 = "ROyal_is Best Institute Ever123."
print(len(str1))
print(str1[2 : 7])  # yal_i
print(str1[ : 7])  # ROyal_i   # start position default - 0
print(str1[6:])  # is Best Institute Ever123.

print(str1[8:2])  # blank
print(str1[:])  # ROyal_is Best Institute Ever123.
print(str1[:32])  # ROyal_is Best Institute Ever123.
print(str1[30:31])  # 3
print(str1[31:31])  # blank

print(str1[-8:-2])  # Ever12
print(str1[-2:-8])  # blank


print(str1[3:8:])   # step value -> 1  (n-1) # al_is
print(str1[3:18:3])   # aiBtn
print(str1[18:2:3])   # blank

print(str1[::3])  # RaiBtnitEr3

str1 = "ROyal_is Best Institute Ever123."
print(str1[-3:-9:2])  # blank
print(str1[-3:-9:-2])  # 2rv
print(str1[-3::-2])  #2rv tttn sBs_aO
print(str1[-4:5:2])  # blank

print(-18 // 4)  # -5


# String Methods
str1 = "ROyal_is Best Institute Ever123."
print(str1.capitalize())  # Royal_is best institute ever123.
print(str1.casefold())  # royal_is best institute ever123.
print(str1.lower())  # royal_is best institute ever123.
print(str1.upper())  # ROYAL_IS BEST INSTITUTE EVER123.
print(str1.title())  # Royal_Is Best Institute Ever123.
print(str1.swapcase())  # roYAL_IS bEST iNSTITUTE eVER123.

print(str1)  # ROyal_is Best Institute Ever123.

name = "Aman"
mode = "Good"

str2 = "{} is {} Boy.".format(name,mode)
print(str2)


str2 = "{1} is {0} Boy.".format(name,mode)
print(str2)


str2 = "{name} is {mode} Boy.{x} {address}".format(x = 90,name="Aman",mode="Bad", address = "Ahm")
print(str2)  # Aman is Bad Boy.90 Ahm

dict1 = {"Name" : {10,20,20,30}, 'list1' : {"city" : "Gnr"}}


str3 = "{Name} is {list1} Girl.".format_map(dict1)

print(str3)


set1 = {}
print(type(set1))  # <class 'dict'>

set2 = {10,}
print(type(set2))  # <class 'set'>


str1 = "ROyal is Best Institute Ever123."

print(str1.replace("Institute", "Technosoft"))  # ROyal_is Best Technosoft Ever123.

str1 = str1.replace(' ','#',1)

str1= str1[::-1]
str1 = str1.replace(' ','#',1)
str1= str1[::-1]
print(str1)  # ROyal#is Best Institute#Ever123.

print(str1.center(40,'*'))  # ****ROyal#is Best Institute#Ever123.****

str3 = "Aman is\nGood\nBoy123."
print(str3.split(' '))    # ['Aman', 'is', 'Good', 'Boy123.']
print(str3.partition(' '))  # ('Aman', ' ', 'is Good Boy123.')
print(str3.rpartition(' '))  # ('Aman is Good', ' ', 'Boy123.')

print(str3.find('Z'))   # -1
# print(str3.index('Z'))  # Gives Error

print(str3.rindex('2'))  # 17

print(str3.splitlines())  # ['Aman is', 'Good', 'Boy123.']

str4 = "Python"
user_need = 'y'
for i in str4:
    if i == user_need:
        print(f"{user_need} is available ")
    else:
        pass

if user_need in str4:
    print(f"{user_need} is available ")

