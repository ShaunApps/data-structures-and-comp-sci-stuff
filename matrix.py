# # 3x3 matrix
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# # 3x4 matrix
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]
# # result is 3x4
# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]
#
# # iterate through rows of X
# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]
#
# for r in result:
#    print(r)
#
#
#
#
# X = [[12,7,3],[4 ,5,6],[7,8,9]]
# Y = [[5,8,1,2],[6,7,3,0],[4,5,9,1]]
#
# result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# for i in range(len(X)):
#     for j in range(len(Y[0])):
#         for k in range(len(Y)):




X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
       result[i][j] = X[i][j] /2

for r in result:
   print(r)

#
# X = [[12,7,3,3,2],
#     [4 ,5,6,1,1],
#     [7 ,8,10,4,5],
#     [7 ,8,9,4,5],
#     [7 ,8,9,4,5]]
#
# n = 5
#
# middle = X[(n/2)][(n/2)]
# sum1 = (X[0][0]) + middle + (X[n-1][n-1])
# sum2 = (X[0][n-1]) + middle + (X[n-1][0])
# print abs(sum1 - sum2)
