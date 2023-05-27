# print(25 to 100)

# _ = 25  # Intialization (start)

# while( _ <= 100 )
# {
#     printf("%d",_);
#     _+=1;  // _ = _ + 1
# }

_ = 100

while _ >= 25:
    if _%5==0 and (_%7==0 and _% 10 == 0):
        print(_,end=' ')
    _ -= 1
# 70

# -----------------------------
print()
for i in range(4):   # 0 1 2 3   -> i=0
    for j in range(i+1):  # 1
        if i == j:  # 0 == 0
            print(j)   # 0
            continue
        print(i)
    print(i)


for k in range(5):   # 0 to 4      k = 1
    for _dhiraj_sir in range(5):  # 0 to 4   _dhiraj_sir = 0
        print((k,_dhiraj_sir),end=' ')

# (1,1) , (1,2), (1,3)  # (0, 0) (0, 1) (0, 2) (0, 3) (0, 4) (1, 0) (1, 1) (1, 2) (1, 3) (1, 4) (2, 0) (2, 1) (2, 2) (2, 3) (2, 4) (3, 0) (3, 1) (3, 2) (3, 3) (3, 4) (4, 0) (4, 1) (4, 2) (4, 3) (4, 4)


# Armstrong Number B/w 1 to 10000


# Palinbdrome, Armstrong, Prime,Perfect, Twin



num = 3
step = 5
# 3 + 33 + 333 + 3333 + 33333 = ans