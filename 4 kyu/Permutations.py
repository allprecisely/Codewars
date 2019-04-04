def permutations(string):
    if len(string) == 1: return set(string)
    first = string[0]
    rest = permutations(string[1:])
    result = set()
    for i in range(len(string)):
        for r in rest:
            result.add(r[:i] + first + r[i:])
    return result


print(permutations('12'))