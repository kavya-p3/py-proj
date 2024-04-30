import numpy


def matrixRotation(mat):
    ro = numpy.array([[0,0,0],[0,0,0],[0,0,0]])
    i = 0
    j = 2
    k =0
    while i < len(mat):
        while k <len(mat):

            ro[i][k] =mat[k][j]
            k+=1
        i+=1
        j-=1
        k=0





    return(ro)


re = numpy.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
'''print(re[0][2])
re.insert([1][0],[8])
re.insert([1][1],9)'''
print(re)
k =matrixRotation(re)

print(k)

