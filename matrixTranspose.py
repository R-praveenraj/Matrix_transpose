# [ [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9] ]

# Output
# [ [1, 4, 7],
#   [2, 5, 8],
#   [3, 6, 9] ]

def matrix_transpose(row,column,matrix):
    original=[]
    transpose=[]
    for i in range(row):
        for j in range(i+1,column):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix
matrix=[]
row=int(input())
column=int(input())
for i in range(row):
    matrix.append(list(map(int,input().split())))

print(matrix_transpose(row,column,matrix))