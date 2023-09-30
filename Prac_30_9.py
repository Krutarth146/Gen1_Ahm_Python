def Manoj(Raman):
    print('Manoj Function')
    return Raman()

# @Manoj
def Ashok():
        print('This is Function ----------------------')

# Manoj(Ashok)


def Aman(jkl):
    jkl.append(900)


list1= [10,90,80,45,67] 

Aman(list1)  # [10,90,80,45,67]
list1+=[10,20]

print(list1)    # [10, 90, 80, 45, 67, 900, 10, 20]

def Aman(n1):
    n1 += 900
    print(n1)   # 980
 
x1 = 80

Aman(x1)  # [10,90,80,45,67]
x1 += 55

print(x1)    # 135


# ----------------------------


x = 10

def manoj():
    x = 70   # Local Variable
    x+=20
    print(x)  # 90

manoj()
x+=11   # Global Variable
print(x)   # 21

x = 10

def manoj():
    global x   # Global Variable
    x+=20
    print(x)  # 30

manoj()
x+=11   # Global Variable
print(x)   # 41


dict1=  {'Name' : "Krutarth", 'ROll' : 900}


from bidict import bidict

dict2 = bidict(dict1)
print(dict2)   # bidict({'Name': 'Krutarth', 'ROll': 900})


dict3 = dict2.inverse
print(dict3)   # bidict({'Krutarth': 'Name', 900: 'ROll'})

print(dict3['Krutarth'])


dict3.update({'HBK' : 'School'})

print(dict3)

# -------------------------------------------------------


import array as arr

manoj = arr.array('i',[10,20,30,40,50])
manoj = arr.array('u',['S','A','M','M','K'])

print(manoj)   # array('i', [10, 20, 30, 40, 50])
print(type(manoj))   # <class 'array.array'>
