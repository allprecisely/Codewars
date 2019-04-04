def find_uniq(arr):
    return [i for i in arr if i !=arr[0]][0] if arr[0] == arr[1] else [i for i in arr if i !=arr[2]][0]

print(find_uniq([1,1,1,1,1,1,11,1,1,1]))
print(find_uniq([1,5,1,1,1,1,1,1,1,1]))
print(find_uniq([0,1,1,1,1,1,1,1,1,1]))