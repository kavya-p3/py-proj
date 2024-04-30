# global su
# def sum(n):
#     if n==1:
#         return 1
#     su = n+sum(n-1)
#     return su
#
#
# su=sum(4)
# print(su)
#-------------------------------------------------------------------------------

# def sum(n):
#     if n//10==0:
#         return n
#     else:
#         re=n%10
#         qu=int(n/10)
#         su=re+sum(qu)
#         return(su)
#
# s=sum(120000000)
# print(s)

#-------------------
def checkstr(str,list_of_words,output):
    for word in list_of_words:
        if str.startswith(word):
            output.append(word)

            return checkstr(str[len(word):],list_of_words,output)

    return output

li=['I','go','am','a','l','hero','h','ro']
st ='Iamherok'
k=checkstr(st,li,[])
print(k)
