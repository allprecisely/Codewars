def solution(a):
    length = len(a)
    iter = min(a)
    buffer = []
    for i in range(1, len(a)):
        s = a[i] - (a[i]//iter)*iter
        if s > 0:
            buffer.append(s)
            buffer.append(iter - s)
    if len(buffer) == 0:
        return length * iter
    return length * min(buffer)




    while len(a) > 1:
        iter = min(a)
        a = [x % iter for x in a if x % iter > 0]
        a.append(iter)
    return iter * length


print(solution([1, 21, 55]))
print(solution([6, 9, 21]))
print(solution([9]))
print(solution([21, 41]))