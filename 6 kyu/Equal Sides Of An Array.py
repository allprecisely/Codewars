# ката о нахождении индекса из списка, справа и слева от которого суммы равны

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1





print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([0,0,0,0,0]))
print(find_even_index([-1,-2,-3,-4,-3,-2,-1]))
print(find_even_index(range(-100,-1)))