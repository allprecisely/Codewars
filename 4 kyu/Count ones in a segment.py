import math

def del_up(point):
    point_pow = int(math.log(point, 2))
    rem = point - 2**point_pow
    fin = rem
    for i in range(1, point_pow + 1):
        fin += ((rem // 2**i) * 2**(i - 1) + (rem % 2**i - 2**(i-1) if rem % 2**i > 2**(i-1) else 0))
    return fin


def del_down(point):
    point_pow = int(math.log(point, 2)) + 1
    rem = 2**point_pow - (point + 1)
    fin = rem
    for i in range(1, point_pow):
        fin += ((rem // 2**i) * 2**(i - 1) + (2**(i - 1) if rem % 2**i >= 2**(i-1) else rem % 2**(i-1)))
    return fin


def countOnes(left, right):
    left_p = int(math.log(left, 2))
    right_p = int(math.log(right, 2))
    sum = -(del_up(left) + del_down(right))
    for i in range(left_p, right_p + 1):
        sum += 2**(i-1) * (2 + i)
    return sum

# print(countOnes(5,7))
print(countOnes(32,33))