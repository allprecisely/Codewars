def find_outlier(integers):
    new_lst = [i%2 for i in integers]
    return integers[new_lst.index(1)] if sum(new_lst) == 1 else integers[new_lst.index(0)]


print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))