# def fino(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return (fino(n-1)+fino(n-2))
#
# print(fino(10))


def fibo(n):

    sum=0
    for i in range(n+1):
        if i == 0:
            sum0=0
        elif i == 1:
            sum1=1
        else:
            sum=sum0+sum1
            sum0=sum1
            sum1=sum


    print(sum)

fibo(10)