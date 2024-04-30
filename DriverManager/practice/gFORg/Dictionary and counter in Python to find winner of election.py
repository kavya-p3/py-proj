from collections import Counter
def countVote(v):
    v = Counter(v)
    print(type(v))
    v = list(v.items())
    print(v)
    print('the highest vote getter is :',v[0])

votes = ["john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"]
countVote(votes)

di = {'john': 4, 'johnny': 4, 'jamie': 3, 'jackie': 2}
d2 = list(di.keys())
print('d2',d2)