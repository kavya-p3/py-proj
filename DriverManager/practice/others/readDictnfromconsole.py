x = {}
n = int(input('enter the length of ur stupid dictionary '))

for i in range(n):
    print("enter key :")
    k = (input())
    print("enter a value")
    v=(input())
    x.update({k:v})

print(x)