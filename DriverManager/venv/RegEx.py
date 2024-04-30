import re

str='vijay 20 1-5-2001, rohit 21 22-10-1990,sita 22 15-09-2000'
result=re.findall(r'\b[\d]+-[\d]+-[\d]+',str)
print('----------------------')
print(result)
lis=[7,9,0]
print(lis[-1::-1])


