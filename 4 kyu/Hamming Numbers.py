# def percent(a):
#     result = []
#     b = a**4
#     l, m, n = int(math.log(b,2)+1), int(math.log(b,3)+1), int(math.log(b,5)+1)
#     for i in range(n):
#         for j in range(int(m-i)):
#             for k in range(int(l-i-j)):
#                 result.append(5**i*3**j*2**k)
#     return(sorted(result)[a-1])

def hamming(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]

print(hamming(5000))