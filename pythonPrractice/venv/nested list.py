matrix = [[1,"kavya",9000],[4,"kavya3",2000],[0,"rani",12000]]
print(len(matrix))
'''for r in matrix:
    for c in r:
       print('R=',r)
       print('C=',c)
col1=[]
col2=[]
col3=[]
c=0
for i in matrix :
    col1.append(i[0])
    col2.append(i[1])
    col3.append(i[2])
print(col1,col2,col3)'''

print(sorted(matrix,key=lambda x:x[2]))

