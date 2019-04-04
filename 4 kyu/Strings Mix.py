import re
from collections import Counter
import operator

def mix(s1, s2):
    d = []
    s1 = re.sub('[^a-z]', '', s1)
    s2 = re.sub('[^a-z]', '', s2)
    d1 = Counter(s1)
    d2 = Counter(s2)
    # sorted_d1 = dict(sorted(d1.items(), key=operator.itemgetter(1)))
    # sorted_d2 = dict(sorted(d2.items(), key=operator.itemgetter(1)))
    # for k, v in sorted_d1.items():
    #     if k not in sorted_d2:
    for (k, v) in d1.items():
        if v not in d2 or v > d2[k]:
            d.append('1:' + k*v)
        elif v > d2[k]:
            d.append('1:' + k*v)
        else:
            d.append('=:' + k * v)


        d1[k*v] = 1
    for (k, v) in d2.items():
        d2[k*v] = 1




    return d1, d2
    # return sorted_d1, sorted_d2

print(mix('fewwfeeerf', 'frefq'))