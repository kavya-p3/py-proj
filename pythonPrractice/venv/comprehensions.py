a = []
a=[x**2 for x in range(2,12,2)]
print(a)

list1=[1,2,3,4,5,8]
list2=[5,6,7,8,0,0]
'''total= [i+j for i in list1 for j in list2]
print(total)
tota2 = [i+j for i in [1,2] for j in [3,4]]
print(tota2)
Listw = []
words = ['acc','bcc','kkk','lll']
for i in words:
    Listw.append(i[0])

print(Listw)'''
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
print (list3)
list4=[i for i in list1 if i not in list2]
print(list4)

