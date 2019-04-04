# тут приведено решение, со сложностью O(n^3/2), на 5 к оно в 20 раз меньше времени занимает!!!!!!
import time

def list_squared(m, n):
    start_time = time.time()
    solution = []
    for i in range(m, n):
        arr = 0
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                arr += j**2
                if i/j != j:
                    arr += (i/j)**2
        if (arr**0.5)%1 == 0:

            solution.append([i, arr])
    print('%s' % (time.time() - start_time))
    return solution


print(list_squared(1, 5000)) #, [[1, 1], [42, 2500], [246, 84100]])
# print(list_squared(42, 250)) #, [[42, 2500], [246, 84100]])
# print(list_squared(250, 500)) #, [[287, 84100]])print()



## ТУТ я попробовал через простые множители пойти, но хрень
# def factor(n):
#     ans = [1]
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             ans.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         ans.append(n)
#     return ans
#
# def list_squared(m, n):
#     solution = []
#     for i in range(m, n):
#         f = factor(i)
#         arr = 0
#         if len(f)%2 == 0:
#             while len(f) >= 2 and f[-1] == f[-2]:
#                 arr += f.pop()
#                 arr += f.pop()
#             if len(f) > 0:
#                 continue
#             solution.append([i, arr])
#         else:
#             continue
#     return solution