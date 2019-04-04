def anagrams(word, words):
    return list(filter(lambda x: sorted(x) == sorted(word), words))
    # return [item for item in words if sorted(item)==sorted(word)]


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('racer', ['cradder', 'carder', 'racdar', 'caders', 'racerd']))
