'''str = "Indiaisagr eatcountrybutcountryre" #great problems in 80 small country too like other country"
sub = "country"
i = 0
flag=False
print("length of string",len(str))
while i < len(str):
    n = str.find(sub, i, len(str))
    if(n>0):
        #print("substring found at :",n+1)
        i=n+1
        flag=True

    else:
        i = i + 1
        if(n==-1 and flag==False):
            #print("oopsy daisy not found")
            break

#n=str.count("country",70,len(str))
#rint("the number of occurances",n)

num=5000
print('{:*^8d}'.format(num))'''