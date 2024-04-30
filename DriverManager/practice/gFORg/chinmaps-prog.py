import collections

# initializing dictionaries
dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }
l1 = [10,20,30,40]
l2 = [20,99,88,6]
l3 = 'kavya'
l4 = (555,88)
# initializing ChainMap
chain = collections.ChainMap(l1, l2,dic1)

# printing chainMap using maps
print ("All the ChainMap contents are : ")
print (chain.maps)


# printing keys using keys()
print ("All keys of ChainMap are : ") 
print ((chain.keys()))

# printing keys using keys() 
print ("All values of ChainMap are : ") 
print ((chain.values()))
chain=chain.new_child(l3)
chain=chain.new_child(l4)
print('chain;;;',chain.maps)
print(type(chain))
print('simplychain',chain['b'])
