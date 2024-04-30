lst = ['s','t','r','i','n','g','s','s','t','r','i','g']
print(lst)
s = input('enter the element to be removed ')
if s not in lst:
    print(' ele not exists ')
else:
   n = int(input('enter the occurance you want to remove '))
   count = 0
   i = 0
   while i < len(lst):
       if lst[i]==s:
           count+=1
           if count==n:
               del lst[i]
               print(lst)

       i+=1

