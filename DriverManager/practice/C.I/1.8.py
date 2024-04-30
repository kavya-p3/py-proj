import numpy

def settinZero(mat):
    for i, j in mat:
        if mat[i][j] ==0:
            for k in mat[i][k]:
                mat[i][k]=0


re = numpy.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
settinZero(re)