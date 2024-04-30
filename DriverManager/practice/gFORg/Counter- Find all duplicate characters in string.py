from collections import Counter
def findup(st):
    st = Counter(st)
    print(st)
    st = dict(st)
    print(st)
    for k,v in st.items():
        if v>1:
            print(k,end=' ')


s = 'heeelloo'
findup(s)