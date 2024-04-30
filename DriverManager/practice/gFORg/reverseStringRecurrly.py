# def recurseString(str,i):
#     if i==3:
#         return
#     str[i],str[len(str)-1-i]=str[len(str)-1-i],str[i]
#     i+=1
#     recurseString(str,i)
#
#
#
#
# s=[1,2,3,4,5]
# recurseString(s,0)
# print(s)
# ===================================================================
def reverseRecc(s):
    if len(s) <= 1:
        return s
    return reverseRecc(s[1:]) + s[0]


k='kavya'
print(reverseRecc(k))
