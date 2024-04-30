Dict = ["go","bat","me","eat","goal","boy", "run","ee"]
arr = ['e','o','b', 'a','m','g', 'l']
st=''
for i in arr:
    st=st+i
print(st)
k=0
for j in Dict:
 while k <len(j):
    if j[k] in st:
        #print(j)
        k+=1
    else:
        break
 if k==len(j):
     print(j,'---',end=' ')