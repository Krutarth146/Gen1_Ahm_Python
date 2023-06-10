# record = {
#     '1001' : {'name' : "Parleg", 'price' : 5, 'qn' : 400},
#     '1002' : {'name' : "5star", 'price' : 20, 'qn' : 200},
#     '1003' : {'name' : "Oats", 'price' : 40, 'qn' : 190},
#     '1004' : {'name' : "kellogs", 'price' : 50, 'qn' : 500}
# }


import json
f1 = open('Record.txt','r')
x = f1.read()
record = json.loads(x)
f1.close()

# print(record['1003'])  # {'name': 'Oats', 'price': 40, 'qn': 190}
# print(record['1003']['price'])  # 40
# print(record.get('1005'))  # ignores
# # print(record['1005'])  # Error

user_need = input("Enter product: ")
quantity = int(input("Enter Quantity: "))

if user_need not in record:
    print("Product Not Found")
    exit()

total_bill = 0
if quantity <= record[user_need]['qn']:
    total_bill = quantity * record[user_need]['price']
    record[user_need]['qn'] -= quantity
    print(f"Your Bill Amount is {total_bill}")

else:
    print(f"We have only {record[user_need]['qn']} products.")
    choice = input("If u need then Press Y: ")

    if choice.lower() == "y":
        total_bill = record[user_need]['qn'] * record[user_need]['price']
        record[user_need]['qn'] = 0
        print(f"Your Bill Amount is {total_bill}")
        print("Inventory Updated!")

    else:
        print("Thank you!")
        exit()


rj = json.dumps(record)
print(type(rj))
print(rj)
fp = open("Record.txt","w")
fp.write(rj)
fp.close()