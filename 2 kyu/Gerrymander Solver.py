def make(counter, flag, cur, filled_field, field):
    if len(cur) == 5:
        add = 0
        for i in cur:
            add += 1 if field[i + i // 5] == 'O' else 0
        if add == 3 or not add or (add == 4 and flag != 4) or (add == 1 and not flag % 3):
            filled_field += cur
            if len(filled_field) == 25:
                print(filled_field)
                return 1
            for i in range(25):
                if i not in filled_field:
                    if make(counter + 1, flag + add, [i], filled_field, field):
                        return 1
            else:
                del filled_field[-5:]
                return
        else:
            return None

    for i in (cur[-1] - 5, cur[-1] - 1, cur[-1] + 1, cur[-1] + 5):
        if i in cur or i in filled_field or i < 0 or i >= 25 or (not (cur[-1] % 5) and i == cur[-1] - 1)\
                or (not ((cur[-1] + 1) % 5) and i == cur[-1] + 1):
            continue
        cur.append(i)
        if make(counter, flag, cur, filled_field, field):
            return 1
        cur.pop()

def gerrymander(s):
    filled_field = list()
    if make(0, 0, [0], filled_field, s):
        res = str()
        tmp_arr = range(25)
        for i in range(25):
            res += str(tmp_arr[filled_field.index(i)] // 5 + 1)
            res += '' if (i + 1) % 5 or i == 24 else '\n'
        return res


test = ['OOXXX',
        'OOXXX',
        'OOXXX',
        'OOXXX',
        'OOXXX']

test2 = ['XXOXO',
         'XOXOX',
         'OXOXO',
         'XOXOX',
         'XXOXX']

test3 = [
		'OXOOX',
		'XXOXO',
		'XOXXX',
		'XXOXX',
		'OXXOO']

print(gerrymander('\n'.join(test2)))