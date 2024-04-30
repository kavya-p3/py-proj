def prime(n):
    x = 1
    for i in range(2, n):

        if n % i == 0:
            x = 0
            break
        else:
            x = 1

    return x


input1 = int(input('enter how many primes do u wish to see'))
temp = 2
k = 1
while k <= input1:
    z = prime(temp)
    if z == 1:
        k = k + 1
        print(temp)
    temp = temp + 1
