def f_nbrs(cur):
    if cur == 0:
        return cur + 1, cur + 5
    elif cur == 4:
        return cur - 1, cur + 5
    elif cur == 20:
        return cur - 5, cur + 1
    elif cur == 24:
        return cur - 5, cur - 1
    elif cur == 5 or cur == 10 or cur == 15:
        return cur - 5, cur + 1, cur + 5
    elif cur == 9 or cur == 14 or cur == 19:
        return cur - 5, cur - 1, cur + 5
    elif cur < 4:
        return cur - 1, cur + 1, cur + 5
    elif cur > 20:
        return cur - 5, cur - 1, cur + 1
    return cur - 5, cur - 1, cur + 1, cur + 5


def make(add, flag, filled_field, field):
    if len(filled_field) % 5 == 0:
        if add == 0 or add == 3 or (add == 4 and flag != 4) or (add == 1 and not flag % 3):
            if len(filled_field) == 25:
                return filled_field
            remains = [x for x in range(25) if x not in filled_field]
            for i in remains:
                tmp = make(1 if field[i + i // 5] == 'O' else 0, flag + add, filled_field + [i], field)
                if tmp:
                    return tmp
            else:
                del filled_field[-5:]
                return
        else:
            return

    for i in f_nbrs(filled_field[-1]):
        if i in filled_field:
            continue
        filled_field.append(i)
        tmp = make(add + (1 if field[i + i // 5] == 'O' else 0), flag, filled_field, field)
        if tmp:
            return tmp
        filled_field.pop()

def gerrymander(s):
    filled_field = [0]
    tmp = make(1 if s[0] == 'O' else 0, 0, filled_field, s)
    print(tmp)
    if tmp:
        res = str()
        tmp_arr = range(25)
        for i in range(25):
            res += str(tmp_arr[tmp.index(i)] // 5 + 1)
            res += '' if (i + 1) % 5 or i == 24 else '\n'
        return res


test = ['OOXXX',
        'OOXXX',
        'OOXXX',
        'OOXXX',
        'OOXXX']

# test2 = ['XXOXO',
#          'XOXOX',
#          'OXOXO',
#          'XOXOX',
#          'XXOXX']
#
# test3 = [
# 		'OXOOX',
# 		'XXOXO',
# 		'XOXXX',
# 		'XXOXX',
# 		'OXXOO']

print(gerrymander('\n'.join(test)))