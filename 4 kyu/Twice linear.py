import time

def dbl_linear(n):
    start_time = time.time()
    arr = [1]
    for i in range(1000000):
        arr.append(arr[i]*2 + 1)
        arr.append(arr[i]*3 + 1)
    arr = sorted(list(set(arr)))
    print(arr.index(1511311))
    print (arr[n],  '%s' % (time.time() - start_time))


print(dbl_linear(500))

