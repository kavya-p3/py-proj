n = int(input('enter the length of lst '))
lst=[]
for i in range(n):
    lst.append(int(input('enter value  ')))

count = 0
num = int(input('enter number to count the occurances '))

for i in lst:
    if( i== num):
        count+=1
if count>0:
    print('the count is ',count)
else:
    print('oops daisy the count is 0')