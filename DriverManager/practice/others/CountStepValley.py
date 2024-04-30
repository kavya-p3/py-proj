step = 'UDDDUDUU'
countd = 0
i=0
j=1
v = 0
while i in range(len(step)):
   if step[i]=='D':
      countd -= 1

   if step[i] == 'U':
       countd += 1
       if countd==0:
           v +=1
   i=i+1


print(v)



