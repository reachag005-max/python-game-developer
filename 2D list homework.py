matrix=[]
matrixi=[]
matrixy=[]
b = int(input("enter number of rows: "))


for i in range (b):
    Temp=[]
    for j in range (b):
        x = int(input("enter value - "))
        Temp.append(x)
    matrix.append(Temp)

"""for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j], end=" ")
    print("\n")
"""

c = int(input("enter number of rows: "))


for z in range (c):
    Temp=[]
    for y in range (c):
        x = int(input("enter value - "))
        Temp.append(x)
    matrixi.append(Temp)

"""for i in range(0,len(matrixi)):
    for j in range(0,len(matrixi[0])):
        print(matrixi[i][j], end=" ")
    print("\n")"""


print("here is your matrix")

for i in range (len(matrix)):
    Temp=[]
    for j in range (len(matrix[0])):
        Temp.append(matrix[i][j] + matrixi[z][y])
        matrixy.append(Temp)

print("sum matrix")
for i in range (len(matrixy)):
    for j in range (len(matrixy[0])):
        print(matrixy[i][j], end =" ")
    print("\n")


"""for i in range(len(matrixy)):
    for j in range(len(matrixy[0])):
        print( matrix[i][j] + matrixi[z][y], end=" ")
    print("\n")"""