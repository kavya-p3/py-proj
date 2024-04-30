def tree(r):
    return [r,[],[]]

def insertLeft(r,branch):
    t=r.pop(1)
    print(len(t))
    if len(t)>1:
        r.insert(1,[branch,t,[]])
    else:
        r.insert(1,[branch,[],[]])

    return r

def insertRight(r,branch):
    t= len(r[2])
    if t>1:
        r.insert(t-1,[branch,[],[]])
    else:
        r.insert(2,[branch,[],[]])

    return r

def getRoot(root):
    return root[0]

def changeRoot(root,newval):
    root[0]=newval



root=tree(5)
insertLeft(root,8)
insertLeft(root,9)
insertLeft(root,10)
print(root)
# insertRight(root,'right1')
# print(root)
# insertRight(root,'first2')
# print(root)
# insertRight(root,'firstr3')
#
# changeRoot(root,'roo')
# print(root)
