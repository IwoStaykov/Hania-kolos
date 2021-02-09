

n = int(input())
m = int(input())

matrix = []

for i in range(n):
    row = input().split()
    row = [int(row[i]) for i in range(len(row))]
    matrix.append(row)

toatl = []


diagonal_horizontal = [matrix[0][index] for index in range(m)]
diagonal_vertical = [matrix[index][0] for index in range(n)]
list_of_sums = []

for x in range(n):
    s = 0
    for y in range(m):
        

        
