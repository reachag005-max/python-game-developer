"""list = [1,2,3,4,5,6]"""

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

"""print(matrix)
print(matrix [1])
print(matrix [1] [3])
print(len(matrix))
print(len(matrix[0]))

for i in matrix:
    print(i[1])"""



for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j], end=" ")
    print("\n")

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j], end=" ")

"""matrix=[]
b = int(input("enter number of rows - "))

for i in range (b):
    Temp=[]
    for j in range (b):
        x = int(input("enter value - "))
        Temp.append(x)
    matrix.append(Temp)

for i in range (b):
    print(matrix[i][j], end = " ")
print("\n")"""


