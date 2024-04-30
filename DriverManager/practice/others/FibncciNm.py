'''n = int(input ('please enter total numbers u wud like to see '))
m1 = 0
m2 = 1
print(m1)
print(m2)
for i in range(n-2):
    m3 = m1+m2
    print(m3)
    m1 = m2
    m2 = m3
-------------------------------------for ith fibonocci num-----------------------------------------'''
'''lst = [0, 1]

n = int(input('print the ith fib number u like to see '))
i = 2

while i < n:
    lst.append(lst[i - 1] + lst[i - 2])
    i += 1
print('your ith number is ', lst[i-1])'''
#----------------to check if given number is fibonocci or not

lst = [0, 1]

n = int(input('enter a number '))
i = 2
flag = False
while i < n+1:
    lst.append(lst[i - 1] + lst[i - 2])
    if n in lst:
        print('heck yeahh')
        flag = True
        break

    i += 1
if flag == False:
    print("oppsy daisy")