from collections import Counter

def commonEle(ar1,ar2,ar3):
    ar1 = Counter(ar1)
    ar2 = Counter(ar2)
    ar3 = Counter(ar3)
    res = dict(ar1.items()& ar2.items()& ar3.items())
    common = []
    for (key, val) in res.items():
        for i in range(0, val):
            common.append(key)
    print(common)


ar1 = [1, 20, 10, 20, 40, 80]
ar2 = [20, 7, 20, 80, 100,80]
ar3 = [20, 40, 15, 20, 30, 70, 80, 120]
commonEle(ar1,ar2,ar3)