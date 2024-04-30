def add(lst):
    n=len(lst)
    sum=0
    for i in lst:
        sum+=i
    avg=sum/n
    return sum,avg

lst=[10,20,50,70]
s,a=add(lst)
print('sum ={}, avg= {}'.format(s,a))