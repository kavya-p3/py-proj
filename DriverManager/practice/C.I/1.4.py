from collections import Counter
st = input('enter a string ')
di = Counter(st.lower())
print(di, sum(di.values()))
c=0
for i in di:
  if i!=' ':
    if di[i]%2!=0:
        c+=1

if c>1:
    print('cant be a palindrome')
else:
    print('heck ya')
