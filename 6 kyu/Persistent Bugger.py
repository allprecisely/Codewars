from functools import reduce

def persistence(n):
    itr = 0
    while len(str(n)) != 1:
        n = reduce(lambda x, y: x*y, map(int, str(n)))
        itr += 1
    return itr


print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))
