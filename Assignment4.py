Matrix_A = [[1, 2],
            [3, 4]]
Matrix_B = [[5, 6],
            [7, 8]]
sum_matrix = [[0, 0],
              [0, 0]]

for i in range(len(Matrix_A)):
    for j in range(len(Matrix_A[0])):
        sum_matrix[i][j] = Matrix_A[i][j] + Matrix_B[i][j]
print("Sum of Matrix A and Matrix B:")

for row in sum_matrix:  
    print(row)
