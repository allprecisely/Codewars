def dirReduc(arr):
    counter = 0
    while True:
        for i in range(len(arr)-1):
            if arr[i] != arr[i+1] and len(arr[i]) == len(arr[i+1]):
                del arr[i], arr[i]
                break
        if counter == len(arr):
            return arr
        else:
            counter = len(arr)


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
