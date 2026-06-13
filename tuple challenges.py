"""student_record=[]

numb= 3

for i in range(numb):
    print(f"Enter student {i+1} details:")
    name = input("Enter name: ")
    age = input("Enter age: ")
    score = input("Enter score: ")
    students = (name,age,score)
    student_record.append(students)


print("\nhere are the student details:")
for items in student_record:
    print(items)"""


items_price  = []
numb = 3

for i in range(numb):
    print(f"Enter details for item {i+1} ")
    name1 = input("Enter item name: ")
    price1 = input("Enter item price: ")
    imported1 = input ("Is item inported [Y/N]: ")

    item1 = (name1,price1,imported1)
    items_price.append(item1)


print(" Here is what you have bought")
print("-"*40)


for items in items_price:
    name,price,imported = items
    print(f"Name : {name}")
    print(f"Price : {price}")
    print(f"imported: {imported}")
    print("-"*100)

