def snail(array):
    if array == [[]]:
        return []
    length = len(array)
    rev_arr = [[0]*length for i in range(length)]
    r_rev_arr = [[0] * length for i in range(length)]
    r_array = [[0] * length for i in range(length)]
    for i in range(length):
        for j in range(length):
            rev_arr[i][j] = array[j][i]
            r_rev_arr[i][-j-1] = array[j][i]
            r_array[j][-i-1] = array[j][i]
    print(rev_arr)
    new_arr = []
    for i in range(length//2):
        new_arr += array[i][i:-i-1] + rev_arr[-i-1][i:-i-1] + r_array[-i-1][i:-i-1] + r_rev_arr[i][i:-i-1]
    return new_arr if not length%2 else new_arr + [array[length//2][length//2]]

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array))


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(array))

array = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]
print(snail(array))

array = [[1,2,3,4,5],
         [12,13,14,5,6],
         [11,16,15,6,7],
         [10,9,8,7,8],
         [10,9,8,7,9]]
print(snail(array))