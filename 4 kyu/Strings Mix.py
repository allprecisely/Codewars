#

import re
from collections import Counter
import unittest

def mix(s1, s2):
    d = []
    s1 = re.sub('[^a-z]', '', s1)
    s2 = re.sub('[^a-z]', '', s2)
    d1 = Counter(s1)
    d2 = Counter(s2)
    for (k, v) in d1.items():
        if v == 1:
            continue
        if k not in d2:
            d.append('1:' + v*k)
        elif d2[k] < v:
            d.append('1:' + v*k)
            del d2[k]
        elif d2[k] == v:
            d.append('=:' + v*k)
            del d2[k]
        else:
            d.append('2:' + k*d2[k])
            del d2[k]

    for k, v in d2.items():
        if v > 1:
            d.append('2:' + v*k)
    d.sort()
    return '/'.join(sorted(d, key=lambda s: len(s), reverse=True))


class Test(unittest.TestCase):
    def test_upper(Test):
        Test.assertEqual(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
        Test.assertEqual(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
        Test.assertEqual(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
        Test.assertEqual(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
        Test.assertEqual(mix("codewars", "codewars"), "")
        Test.assertEqual(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")


unittest.main()