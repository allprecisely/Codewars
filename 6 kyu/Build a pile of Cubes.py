def find_nb(m):
    n=1
    while m > 0:
        m -= n**3
        n +=1
    return n-1 if m == 0 else -1


print(find_nb(4183059834009))
print(find_nb(24723578342962))
print(find_nb(135440716410000))
print(find_nb(40539911473216))
print(find_nb(26825883955641))
print(find_nb(9))
