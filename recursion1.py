from functools import reduce

# list1 = [1,2,3,4,5]
num = 10
x = reduce(lambda x , y: x * y, [i for i in range(1,num+1)])
print(x)

from itertools import accumulate

y = list(accumulate([i for i in range(1,num+1)], lambda x , y: x * y))
print(y)  # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


# Recursion

def fibonacci(num):
    n1,n2 = 0,1

    print(n1,n2,end=' ')

    for i in range(num-2):
        n3 = n1 + n2 
        print(n3,end=' ')
        n1 = n2
        n2 = n3

fibonacci(5)   # 0 1 1 2 3


# Recursion
print()
print()
print()


import time
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonnacci_rec(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonnacci_rec(num-1) + fibonnacci_rec(num-2)


# print(fibonnacci_rec(5))  # 5
fr_start = time.time()
for i in range(50):
    print(fibonnacci_rec(i),end=' ')   # 0 1 1 2 3
print("Recursion Execution TIme: ",time.time() - fr_start)

# -----------------------------------
print()
def fibo(num):
    list1 = [0,1]
    for i in range(num):
        list1.append(list1[-1] + list1[-2])
    return list1[-2]

fi_start = time.time()
print(fibo(50))   # 5
print("Iterators Execution TIme: ",time.time() - fi_start)


'''
l1 = [[3, 2, 4],[16, 4, 1, 64],[9, 12, 3, 6]]
l2 = list(map(lambda x : sorted(x), l1))
l3 = list(map(lambda x : map(lambda i : i[-2], list(x)), l2))
print(l3)
'''

l1 = [[3, 2, 4],[16, 4, 1, 64],[9, 12, 3, 6]]
l2 = list(map(lambda x : sorted(x), l1))


lst5 = [i for i in l2]
for i in lst5:
    print(i[-2])

l3 = list(map(lambda x : x[-2], [i for i in l2]))
print(l3)

# 12. Given a list of strings and a string str, print all anagrams of str

my_list = ["geeks", "geeg", "keegs", "practice", "aa"]
str = "eegsk"

list1 = []

for i in str:
    list1.extend(i)

print(type(list1))
print(sorted(list1))
list2 = []
for i in my_list:
    list2 = []
    for j in i:
        if j in list2 or j not in list2:
            list2.append(j)
    # print(list2)
    if sorted(list1) == sorted(list2):
        print(i)