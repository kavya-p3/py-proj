def checkpali(s):
    s1 = s[-1::-1]
    if s==s1:
        print('hech yeah palindrome')
    else:
        print('oopsy daisy')

st = input('enter string ')
checkpali(st)
reversed(st)
print('at las',st)