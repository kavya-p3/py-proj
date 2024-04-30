'''lst = [5999, -8, 9, 6, 100, 99, 20, 98, 101, 0, 1000]
n = int(input('enter nth largest number u would like  to know '))
lst.sort(reverse=True)
print(lst)
print('the nth larget number is ',lst[n-1])'''

def largstnumber(lst1,n):

      max = lst1[0]
      for i in lst1:
        if i > max:
            max = i

      if n > 1:

        lst1.remove(max)
        n-=1
        max = largstnumber(lst1,n)


      return max




lst = [5999, -8, 9, 6, 100, 99, 20000, 98, 101, 0, 1000]
print(lst)
n = int(input('enter the nth value '))
print(largstnumber(lst,n))

