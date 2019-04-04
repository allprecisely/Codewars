def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    return list(map(lambda x: x**2, sorted(array1))) == sorted(array2)

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
a3 = []
a4 = []
a5 = None
a6 = []
# a2 = [1,2,3,4,5,6,7,8]

print(comp(a1, a2))
print(comp(a3, a4))
print(comp(a5, a6))