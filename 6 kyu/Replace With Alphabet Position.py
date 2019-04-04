def alphabet_position(text):
    letters = list(filter(lambda x: x.isalpha(), text.lower()))
    return ' '.join(list(map(lambda x: str(x), list(map(lambda x: ord(x) - 96, letters)))))
    # chPos = ord(text) - 96
    # return chPos

print(alphabet_position("The sunset sets at twelve o' clock."))

