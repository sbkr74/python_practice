# muliplication of two matrices
A = [[1,2,3],      
    [4,5,6],
    [7,8,9]]           

B = [[3,2,1],
    [6,5,4],
    [9,8,7]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        for k in range(len(A[0])):
            result[i][j]+=A[i][k]*B[k][j]
for r in result:
    print(r)