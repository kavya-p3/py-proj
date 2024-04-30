def checkPrime(num,flag):
 if (num>2):
    for i in range (2,num):
          if(num%i==0):
             flag=False
             break
          else:
              flag=True
    return flag

n=int(input("please enter your number :"))
flag=True
print("yeaaah prime 2")
for i in range(3,n):
 flag=checkPrime(i,flag)
 if(flag):
    print("yeaaah prime",i)
