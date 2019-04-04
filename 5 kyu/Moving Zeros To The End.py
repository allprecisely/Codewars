def move_zeros(array):
    arr = [x for x in array if x != 0 or str(x) == 'False']
    return arr + [0 for i in range(len(array) - len(arr))]


print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]))
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
print(move_zeros([0,1,None,2,False,1,0]))
print(move_zeros(["a","b"]))
print(move_zeros(["a"]))
print(move_zeros([0,0]))
print(move_zeros([0]))
print(move_zeros([False]))
print(move_zeros([]))