num1 = 90
num2 = 80
num3 = 78

maximum = lambda num1, num2, num3 : (print(num1) if num1 > num3 else print(num3)) if num1 > num2 else (print(num2) if num2 > num3 else print(num3))


maximum(num1,num2,num3)


dict1 = [10,20,30,40,50, {"address" : [{"state" : "GUj", "Area" : 'C.G>ROAD'}]}]

print(dict1[-1]['address'][0]["Area"])  # C.G>ROAD

l1 = [10,20,889,45,326,67,221]

need = 67

print(l1.count(need))  # 1

# Linear Search
# Binary Search

# Linear Search

l1 = [10,20,889,45,326,67,221]

need = 67

for i in l1:
    if i == need:
        print("Element is found")
        break
else:
    print("Not Found")


# Binary Search
l1.sort()
start = 0
end=  len(l1) - 1


while start <= end:
    mid = (start + end)//2
    if l1[mid] == need:
        print("Element is found")
        break
    elif l1[mid] < need:
        start = mid+1
    elif l1[mid] > need:
        end = mid-1
    else:
        print("Not Found")


# Recursive 