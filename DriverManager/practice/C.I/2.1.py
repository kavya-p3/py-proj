def removeDups(li):
    i = 0

    while i < len(li) - 1:
        j=i+1
        while j < len(li):
            if li[i] == li[j]:
                del li[j]
                j = j - 1
            j += 1
        i += 1


li = [0,8, 8, 8,1,0,0,6,8,6]
removeDups(li)
print(li)
