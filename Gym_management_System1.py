import mysql.connector


mydb = mysql.connector.connect(user = "root", password = 'mysql', host = 'localhost', database = 'krutarth')

if mydb.is_connected():
    print("Database Conncted....")
else:
    print("Not Connected....")

cur = mydb.cursor()

cur.execute("create table if not exists cust_details (id int primary key auto_increment, Name varchar(30), Gender char, contact int, username varchar(30), password varchar(30))")


cur.execute("create table if not exists phy_details1 (pid int primary key auto_increment, Name varchar(30), height float not null, weight float not null, bmi float, diet varchar(30), id int, foreign key(id) references cust_details(id))")


print("Gym Management System".center(40))

# cur.execute("Alter table cust_details modify username varchar(30) unique")


class UniqueUsername(Exception):
    pass


try:
    while True:
        print("1 ---- Signup")
        print("2 ---- Login")
        print("3 ---- Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            name = input("Enter Name: ")
            gender = input('Enter Gender: ')
            contact = int(input("Enter Contact: "))
            try:
                username = input('Enter Username: ')

                q8 = "select * from cust_details where username = %s"
                t6 = (username, )
                cur.execute(q8,t6)

                list1 = cur.fetchall()

                if len(list1) > 0:
                    raise UniqueUsername 
                
                else:
                    password = input('Enter Password: ')   # REGEX

                    q = "INSERT INTO CUST_DETAILS (NAME, GENDER, CONTACT, USERNAME, PASSWORD) VALUES (%s, %s, %s, %s, %s)"

                    val1 = (name, gender, contact, username, password)
                    cur.execute(q, val1)

                    mydb.commit()

                    height = float(input("Enter Height: "))
                    weight = float(input("Enter Weight: "))

                    q8 = "select id, name from cust_details where username = %s"
                    t6 = (username, )
                    cur.execute(q8,t6)

                    data= cur.fetchone()

                    q78 = "INSERT INTO PHY_DETAILS1 (NAME, HEIGHT, WEIGHT, ID) VALUES (%s, %s, %s, %s)"
                    val78 = (data[1], height, weight, data[0])
                    cur.execute(q78, val78)   
                    mydb.commit()
            
            except UniqueUsername:
                print('User iD Taken')
        elif choice == 2:
            pass

        elif choice == 3:
            break


except:
    print("An Error Occured")

finally:
    cur.close()
    mydb.close()