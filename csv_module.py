# x = 10

# def jay(m1, m2):
#     global x
#     y = 20
#     print(x+y)


#     x = x+y
#     print(x)
#     # print(m1,m2)



# # m2 = 90
# # m1 = 45

# print(x)
# jay(m2 = 90 , m1 = 45)   # 45 90

# Comma Seprated Values (CSV)

import csv

rows = []


filename = 'BlackFriday.csv'
with open(filename, 'r') as csvfile:
    csvreader1 = csv.reader(csvfile)
    heading = next(csvreader1)
    # heading = next(csvreader1)
    print(heading)   # Heading List

    for i in csvreader1:
        rows.append(i)

    # print(rows)

    print('Total No. of lines are %d'%(csvreader1.line_num))

print('First 5 rows are: ')

for k in heading:
    print(k,end=' ')
print()
for line in rows[0:5]:
    for word in line:
        print("%7s"%word,end=' ')
    print()


fiels = ['Name', 'Roll', 'Address']

rows = [
    ["Aaryan", 90, 'Ahm'],
    ["Aaryan", 90, 'Ahm'],
    ["Aaryan", 90, 'Ahm'],
    ["Aaryan", 90, 'Ahm'],
    ["Aaryan", 90, 'Ahm'],
    ["Aaryan", 90, 'Ahm'],
]

with open("try.csv",'w') as csvfilee:
    csvwriter = csv.writer(csvfilee)
    csvwriter.writerow(fiels)
    csvwriter.writerows(rows)


dict1 = [
    {'Name' : 'Aman','Address' : 'Gnr' ,'Roll' : 93, },
    {'Name' : 'Aman', 'Roll' : 93, 'Address' : 'Gnr'},
    {'Name' : 'Aman', 'Roll' : 93, 'Address' : 'Gnr'},
    {'Name' : 'Aman', 'Roll' : 93, 'Address' : 'Gnr'},
    {'Name' : 'Aman', 'Roll' : 93, 'Address' : 'Gnr'},
    {'Name' : 'Aman', 'Address' : 'Gnr'},
]

heading = ['Name', 'Roll', 'Address']
with open("jay.csv",'w') as csvfile1:
    csvdictwriter = csv.DictWriter(csvfile1, fieldnames = heading)
    csvdictwriter.writeheader()
    csvdictwriter.writerows(dict1)


    
