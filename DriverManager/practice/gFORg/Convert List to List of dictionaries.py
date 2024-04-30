temp = []
fin = []
l3 = []
d3 = {}
k = ['name','id']
v = ['kavya',444,'saumya',999,'juhi',77,'kalu',742]
vl = len(v)
#d = [{'name':'kavya','id':444},{'name':'saumya','id':999}]
l1 = ['kavya',444]
l2 = zip(k,l1)
d1 = dict(l2)

for i in range(0, vl, 2):
    temp.append(v[i])
    temp.append(v[i+1])
    fin = zip(k,temp)
    l3 = list(fin)
    d3.update(dict(l3))
    print(d3)
    temp = []
print(type(d3))
'''-------------------------------------
# Python3 code to demonstrate working of
# Convert List to List of dictionaries
# Using zip() + list comprehension

# initializing lists
test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]

# printing original list
print("The original list : " + str(test_list))

# initializing key list
key_list = ["name", "number"]

# using list comprehension to perform as shorthand
n = len(test_list)
res = [{key_list[0]: test_list[idx], key_list[1]: test_list[idx + 1]}for idx in range(0, n, 2)]
s = str(res)

# printing result
print("The constructed dictionary list : " + s)
print(type(s))'''


