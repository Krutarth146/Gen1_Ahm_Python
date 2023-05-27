x = 90
y = 80

print(f"{x} + {y} = {x+y}")

str1 = 'lorem\tipsum123.'

print(str1.encode())   # b'lorem ipsum123.'


str2 = "Ståle"
print(str2.encode())   # b'St\xc3\xa5le'

print(str2.encode(encoding="ASCII", errors="ignore"))   # b'Stle'   (b'St\xc3\xa5le'  in utf-8)
print(str2.encode(encoding="ASCII", errors="namereplace"))   # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(str2.encode(encoding="ASCII", errors="backslashreplace"))   # b'St\\xe5le'
print(str2.encode(encoding="ASCII", errors="xmlcharrefreplace"))   # b'St&#229;le'
print(str2.encode(encoding="ASCII", errors="replace"))   # b'St?le'


print(str1.endswith('.',5))  # True

print(str1.expandtabs(16))  # lorem           ipsum123.


str1 = 'd      a      d'
print(str1.isalnum())

# str1.isascii()
# str1.isdigit()
# str1.isnumeric()
# str1.isdecimal()

print(str1.isidentifier())
print(str1.isspace())


str3 = "Parth is Good Boy123. "
print('_'.join(str3))
print(len(str3))   # 21
print(str3.ljust(30,'_'))
print(str3.rjust(30,'_'))


print(str3.lstrip())   # Parth is Good Boy123.
print(str3.rstrip())  #           Parth is Good Boy123.
print(str3.strip())   # Parth is Good Boy123.

print(str3.removeprefix('Pa'))  # rth is Good Boy123.

print(str3.rfind('z'))   # -1
# print(str3.rindex('z'))  # error


str4 = "5000"
print(str4.zfill(5))


str6 = "Hello Tirth"


table = str6.maketrans('T', "a", "o")
print(table)  # {84: 97, 111: None}


str6 = str6.translate(table)
print(str6)   # Hello airth


'''

# String Programs

# 1. Write a Py program that takes your full Name and Print Like This :
# Input - Krutarth Daxeshbhai Patel
# o/p   - K.D.Patel

# 2. Find NUmber of spaces characters in a given str.
# input - Python Programming

# o/p - vowels - 4, white spaces - 1, consonents - 13

# 3. write a py program to make a new string
# input  - This is lion in the cage.
# o/ p - This is lion in cage.

# 4. WAP:
# input - Keep yourself Mute while not speaking
# output - Keep_yourself Mute while not#speaking

# 5. Write a program to calculate the sum of series up to n term. For example, if n = 5 the series will become 3 + 33 + 333 + 3333 + 33333 = ???

# 6. Write a Python function that checks whether a passed string is palindrome or not.

# 7. Write a Py program to calculate the factorial of a number (a non-negative integer).

# 8. Python program to find second largest number in a list.  // Null

# 9. Check whether bthis str is aplindrome or not??
str2 = "Computer"

# print(str2[::-1])  Without using this 

'''






# List ---------------------------