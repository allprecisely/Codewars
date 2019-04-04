def Factor(n):
   Ans = set()
   d = 2
   n = abs(n)
   while d * d <= n:
       if n % d == 0:
           Ans.add(d)
           n //= d
       else:
           d += 1
   if n > 1:
       Ans.add(n)
   return list(Ans)

def sum_for_list(lst):
    dct = dict()
    for i in lst:
        for prime in Factor(i):
            if prime in dct:
                dct[prime] += i
            else:
                dct[prime] = i
    sorted_by_value = sorted(dct.items(), key=lambda kv: kv[0])
    return [list(x) for x in sorted_by_value]


print(sum_for_list([15, 30, -45]))
