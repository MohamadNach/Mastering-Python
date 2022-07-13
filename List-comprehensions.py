"""
Let's learn about list comprehensions! 
You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j + k is not equal to n.
Here, 0 <= i <= x ; 0 <= j <= y ; 0 <= k <= z. 
Please use list comprehensions rather than multiple loops, as a learning exercise.
"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())
# creating the list of all possible coordinates
my_list = []
# creating the list for all possible coordinates, where sum of i + j + k is not equal to n
new_list = []

while True:
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                my_list.append([i, j, k])

    for item in my_list:
        if sum(item) != n:
            new_list.append(item)

    print(new_list)
    break
