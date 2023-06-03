# Files    1. Text File  2. Binary File

# FIles Opening Modes

# 'w' ---> Write Mode (Overwrite)

# 'r' ---> Read Mode

# 'a' ---> Append Mode (Append the data from last line of code)

# 't' ---> Text file 

# 'b' ---> Binary FIle

# 'x' ---> If file Exists then it will give an error

# '+' ---> Read + write 

fp = open("jay1.txt","w")

fp.write("\nHello I am Mitanshu Patel")
fp.write("\nHello I am Ashok Patel")

list1 = ["\nHello I am Mitanshu Patel", "\nHello I am Ashok Patel", "\nHello I am Ashok Patel", "\nHello I am Ashok Patel"]

fp.writelines(list1)
fp.close()

fp = open('jay.txt','r')

# x = fp.read()

# print(x)
print(fp.tell())   # 0
print(fp.readline())

print(fp.tell())   # 2
print(fp.readline())  # Hello I am Mitanshu Patel
print(fp.tell())   # 29
print(fp.readline())  # Hello I am Ashok Patel
print(fp.readline())  # Hello I am Ashok Patel
print(fp.readline())  # Hello I am Ashok Patel
print(fp.readline())  # Hello I am Ashok Patel
print(fp.readline())  # Hello I am Ashok Patel
print(fp.readline())  # Hello I am Ashok Patel
print(fp.readline())  # Hello I am Ashok Patel
print(fp.readline())  # Hello I am Ashok Patel
print(fp.readline())  # Hello I am Ashok Patel
print(fp.tell())   # 150

# fp.seek(2)
# print(fp.readline())    # Hello I am Mitanshu Patel

# fp.seek(29)
# print(fp.readline())    # Hello I am Ashok Patel

fp.seek(34,0)
print(fp.readline())
print(fp.readline())

fp.seek(0)

print(fp.readlines())  # ['\n', 'Hello I am Mitanshu Patel\n', 'Hello I am Ashok Patel\n', 'Hello I am Mitanshu Patel\n', 'Hello I am Ashok Patel\n', 'Hello I am Ashok Patel\n', 'Hello I am Ashok Patel']


fp.seek(0)

x = fp.read()

# for i in x:
#     print(i)

words = x.split()
print(words)

counter = 0
for k in words:
    if k.endswith('k'):
        counter+=1

print(counter)

fp.close()


f1  =open("m1.png",'rb')
x = f1.read()
f1.close()

# print(x)

f2 = open("m3.png",'wb')
f2.write(x)
f2.close()
import json



# Palindroeme, Prime
# Read + Write, Pickle (dumps, load, loads), Random, 0, 1, 2


import random

print(random.randint(1,100))