st = ['aaaa', 'ghj', 'lm', 'cc']
sub = 'aaaa'

for j in range(1, 4):
    k = 0
    for i in st[j]:
      if i==sub[k]:
          #if i not in sub:
            #sub+=i
            k = k + 1
      else:
        try:
          if i != sub[0][k] :
              print('remove',i,sub)
              sub=sub[0:len(sub)-1]
          break
        except:
            pass
print(sub)
