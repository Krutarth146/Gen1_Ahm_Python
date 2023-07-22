# Inheritance

class Alto():
    def __init__(self):
        self.wheels = 4
        print("This is Alto Class Constructor.")

    def Brake(self):
        print("Brake Method Under Alto Class", self.wheels)

    def Seat(self):
        print("Alto Have Four Seats")


# class Ferari :: public Alto

class Ferrari(Alto):
    def __init__(self):
        super().__init__()
        print("This is Ferari class Constructor")

    def Safety(self):
        super().Seat()
        print("This is Safety Method Under Ferrari Class")


mit = Ferrari()

mit.Brake()
mit.Safety()

list1 = [[1,0,1], [1,1,1], [2,1,0], [2,0,0]]

n = 3
sum = 0
# res= []
# for i in range(len(list1)):
#     sum = 0
#     for j in list1[i]:
#         sum += j
#     if sum != n:
#         res.append(list1[i])
        

# print(res)     


# list(filter())


x,y,z = 1,1,2


for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            print([i,j,k],end=' ')