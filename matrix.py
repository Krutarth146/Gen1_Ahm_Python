list1 = [10,20,30,40,50]

print(list1)

for i in list1:
    print(i)  # 10 20 30 40 50

list2 = [[10,20,30], 
         [40,50,60], 
         [70,80,90]]

print(list2)

print(list2[1][1])  # 50
print(list2[2][0])  # 70

list1 = [[10,20,30], (10,20,30,(90,{'address' : {'city' : "Ahmedabad", 'state' : "Gujarat"}}))]


print(list1[1])  # (10, 20, 30, (90, {'address': {'city': 'Ahmedabad', 'state': 'Gujarat'}}))
print(list1[1][-1])  # (90, {'address': {'city': 'Ahmedabad', 'state': 'Gujarat'}})
print(list1[1][3])  # (90, {'address': {'city': 'Ahmedabad', 'state': 'Gujarat'}})
print(list1[1][3][1]["address"])  # {'city': 'Ahmedabad', 'state': 'Gujarat'}
print(list1[1][3][1]["address"]['state'])  # Gujarat

list2 = [[10,20,30], 
         [40,50,60], 
         [70,80,90]]


for i in list2:
    for j in i:
        print(j,end=' ')   # 10 20 30 40 50 60 70 80 90


l1 = [[10, 20, 30], 
      [40, 50, 60], 
      [70, 80, 90]]
totalSum = 0

for i in range(len(l1)):
    for j in range(len(l1[i])):
        if i == j:
            totalSum += l1[i][j]

print(totalSum)

sum = 0
length = len(l1)
for i in range(len(l1)):
    sum += l1[i][length - 1 - i]

print(sum)  # 150
