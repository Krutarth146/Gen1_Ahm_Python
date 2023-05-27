# Map, Reduce, Filter

list1 = [10,20,30,40,50,90]
square = [1,4,9,16,25,81]


res = []
for i in list1:
    res.append(i**2)
print(res)

sq = lambda x : x**2
print(sq(25))   # 625

sq1 = list(map(lambda x : x**2, list1))  # <map object at 0x000002A752F22590>
print(sq1)  # [100, 400, 900, 1600, 2500, 8100]

sq2 = tuple(map(lambda d : d*10, list1))
print(sq2)   # (100, 200, 300, 400, 500, 900)


# Filter

list1 = [10,20,30,41,51,91]

# filter()

x1 = list(filter(lambda f : f % 5 == 0 or f % 7 == 0, list1))
print(x1)   # [10, 20, 30]

import statistics
y1 = list(filter(lambda v : (sum(list1)//len(list1)) < v, list1))
y1 = list(filter(lambda v : statistics.mean(list1) < v, list1))
print(sum(list1)//len(list1))
print(y1)


# Reduce
list1 = [1,2,3,45,32,1]
from functools import reduce
z = reduce(lambda z,m : z * m, list1)
print(z)  # 84

from itertools import accumulate

s1 = list(accumulate(list1, lambda z,m : z + m))
print(s1)  # [1, 3, 6, 51, 83, 84]

# 5 Programs Map, reduce, filter

# oye balle balle oye
# OyE BallE BallE OyE

# hw --> function --> authentication(email, pass)  # Register  
