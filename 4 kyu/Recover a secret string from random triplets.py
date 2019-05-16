def recoverSecret(triplets):
    dct = {}
    for i in triplets:
        if i[0] not in dct:
            dct[i[0]] = set()

        if i[1] not in dct:
            dct[i[1]] = {i[0]}
        else:
            dct[i[1]].add(i[0])

        if i[2] not in dct:
            dct[i[2]] = {i[0], i[1]}
        else:
            dct[i[2]].update({i[0], i[1]})

    res = ''

    while dct:
        tmp = ''
        for k, v in dct.items():
            if not v:
                tmp = k
                del dct[k]
                break

        for k, v in dct.items():
            if tmp in v:
                dct[k].remove(tmp)
        res += tmp


    return res


tripl = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(tripl))
