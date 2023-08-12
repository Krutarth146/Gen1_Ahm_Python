# Decorators is first class Object

# Function ---> can pass function as an arugument
# Function ---> can make function in another function

def Jay(f1):
    print("Jay Raval")
    f1()


def Aman():
    print("Boat Co-Founder")


# CA = Aman

# Jay(CA)
Jay(Aman)


# ------------------------------------

def fun2(f3):

    def fun6():
        print("This is fun6 Method Under fun2")
        f3()

    return fun6()

# fun2(UDay)
print("-----------------")

@fun2
def UDay():
    print("This is Uday Foundation")


print("-----------------")
@fun2
def SHrey_sir():
    print("Shrey Sir")

@classmethod
def JayP(lm):
    print("Jayp is Class method Now.")