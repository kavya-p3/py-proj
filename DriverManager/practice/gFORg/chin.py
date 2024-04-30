from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
ch = list(ChainMap(adjustments, baseline))
di = {'music': 'bach', 'art': 'rembrandt'}
dl = list(di)
print('dl',dl)