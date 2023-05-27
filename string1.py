
x = 90
y = 89.78
print(x+y)  # 179.78

v = True
print(type(v))  # bool
g = 45
print(type(g))  # Int
print(v+g)  # 46    # Implicit Typecasting


x = '78.98'
print(int(float(x)))  # 78  # Explicit Typecasting

h = (90,)
print(list(h))  # [90]

# Indexing
str1 = "Royal Technosoft is Best Institute Ever123."
print(str1[2])  # y
print(str1[-1])  # .

# Slicing

# print(str1[start : end(n-1) :step(n-1)])
 
print(str1[4:8])  # l Te

print(str1[2::1])  # yal Technosoft is Best Institute Ever123.
print(str1[2::3])  # y cofiBtnitEr3
print(str1[10::2])  # nsf sBs nttt vr2.
print(str1[10:3:2])  # blank

print(str1[10:3:-1])  # nhceT l
print(str1[10:15:3])   # no
print(str1[10:15:-3])   # blank

str1 = "Royal Technosoft is Best Institute Ever123."
print(str1[-5:-1:2])   # r2
print(str1[:-1:2])   # RylTcnsf sBs nttt vr2
print(str1[:7:])   # Royal T
print(str1[-5:-2:-2])   # 
print(str1[-5::-2])   # rv tttn sBs fsncTlyR
print(str1[-5::2])   # r2.
print(str1[-5:4:3])   # blank




# Krutarth Daxeshkumar Patel

# K.D.Patel
  
str1 = 'Mukesh Ashokbhai Patel'

words = str1.split(' ')
# print(words)
# print(f"{words[0][0]}.{words[1][0]}.{words[2]}")
print(words[0][0],'.',words[1][0],'.',words[2],sep='')
print(words[-2][-4])  # b


str2 = "Keep yourself Mute while Not speaking"
# ans = "Keep_yourself Mute while Not#speaking"

str2 = str2.replace(' ','_',1)
print(str2)  # Keep_yourself Mute while Not speaking



# String Programs

# 1. Write a Py program that takes your full Name and Print Like This :
# Input - Krutarth Daxeshbhai Patel
# o/p   - K.D.Patel

# 2. Find NUmber of spaces characters in a given str.
# input - Python Programming

# o/p - vowels - 4, white spaces - 1, consonents - 13

# 3. write a py program to make a new string
# input  - This is the lion in the cage.
# o/ p - This is lion in cage.

# 4. WAP:
# input - Keep yourself Mute while not speaking
# output - Keep_yourself Mute while not#speaking

# 5. Write a program to calculate the sum of series up to n term. For example, if n = 5 the series will become 3 + 33 + 333 + 3333 + 33333 = ???

# 6. Write a Python function that checks whether a passed string is palindrome or not.

# 7. Write a Py program to calculate the factorial of a number (a non-negative integer).

# 8. Python program to find second largest number in a list.  // Null
