def next_bigger(l):
    n = list(str(l))
    for i in range(len(n)-1, 0, -1):
        if n[i] > n[i-1]:
            sor = sorted(n[i-1:])
            for j in range(len(sor)):
                if sor[j] > n[i-1]:
                    return int(''.join(n[:i-1]) + sor.pop(j) + ''.join(sor))
    return -1

print(next_bigger(12))
print(next_bigger(513))
print(next_bigger(2017))
print(next_bigger(414))
print(next_bigger(144))
print(next_bigger(531))
print(next_bigger(152))
print(next_bigger(165))
print(next_bigger(371))