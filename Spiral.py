degree = int(input('Enter a matrix degree\n'))
num_matrix = []

for i in range(degree):
    num_row = input('Enter a row:\n').split()
    num_row = [int(num_row[i]) for i in range(len(num_row))]
    num_matrix.append(num_row)
print(num_matrix[0][1])

def spiral(elem_in_line):
    