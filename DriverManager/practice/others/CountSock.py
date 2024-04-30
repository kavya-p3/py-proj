ar = [1, 0, 0, 0, 1, 3, 1, 3, 1, 0, 1]

i = 1
j = 0
count = 0
c = 0
while j < len(ar):
    count = 1
    if ar[j] != 'x':
        while i < len(ar):
            if ar[j] == ar[i]:
                count += 1
                ar[i] = 'x'
            i=i+1
        c+=(count//2)
    j=j+1
    i=j+1

print(c)
