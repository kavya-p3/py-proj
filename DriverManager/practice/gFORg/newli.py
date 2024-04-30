lis = [1]
print(lis)
for i in range(len(lis)):

    a = lis.pop()
    lis.insert(i, a)
    

print(lis)