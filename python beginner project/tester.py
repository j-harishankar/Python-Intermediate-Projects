from collections import defaultdict;
l = ['hari','bobson','ramesh','suresh','irah']
dict= defaultdict(list)
for s in l:
    so = tuple(sorted(s))
    dict[so] = dict.append(s)
    print(so)