def parse_int(string):
    dictionary = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                  'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
                  'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
                  'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100,
                  'thousand': 1000, 'million': 1000000}
    result = 0
    numbers = list()
    for i in string.split():
        if i == 'and': continue
        if '-' in i:
            tens = i.split('-')
            numbers.append(dictionary[tens[0]]+dictionary[tens[1]])
            continue
        numbers.append(dictionary[i])
    buffer = numbers[0]
    if len(numbers) == 1: return numbers[0]

    for i in range(1, len(numbers)):
        if buffer >= 1000:
            result += buffer
            buffer = numbers[i]
            continue
        if numbers[i-1] < numbers[i]:
            buffer *= numbers[i]
        elif numbers[i-1] > numbers[i]:
            buffer += numbers[i]
    result += buffer
    return result

print(parse_int('one'))
print(parse_int('twenty'))
print(parse_int('two hundred forty-six'))
print(parse_int('five hundred thousand three hundred'))
print(parse_int('three hundred'))


