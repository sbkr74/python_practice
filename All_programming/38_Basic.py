# Transpose of matrix
A = [[1,2,3],      
    [4,5,6],
    [7,8,9]]
# ==================================================================
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[j][i]

for r in result:
    print(r)

# ====================================================================
print()
transpose_matrix = [[row[i] for row in A] for i in range(len(A[0]))]
for t in transpose_matrix:
    print(t)