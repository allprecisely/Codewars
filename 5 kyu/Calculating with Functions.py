def itter(a, func):
    func = func.split()
    if func[0] == '+':
        return a + int(func[1])
    if func[0] == '-':
        return a - int(func[1])
    if func[0] == '*':
        return a * int(func[1])
    if func[0] == '//':
        return a // int(func[1])

def zero(func = None):
    if func == None:
        return 0
    return itter(0, func)
def one(func = None):
    if func == None:
        return 1
    return itter(1, func)
def two(func = None):
    if func == None:
        return 2
    return itter(2, func)
def three(func = None):
    if func == None:
        return 3
    return itter(3, func)
def four(func = None):
    if func == None:
        return 4
    return itter(4, func)
def five(func = None):
    if func == None:
        return 5
    return itter(5, func)
def six(func = None):
    if func == None:
        return 6
    return itter(6, func)
def seven(func = None):
    if func == None:
        return 7
    return itter(7, func)
def eight(func = None):
    if func == None:
        return 8
    return itter(8, func)
def nine(func = None):
    if func == None:
        return 9
    return itter(9, func)

def plus(func):
    return f'+ {func}'
def minus(func):
    return f'- {func}'
def times(func):
    return f'* {func}'
def divided_by(func):
    return f'// {func}'

print(seven(times(five()))) #, 35)
print(four(plus(nine()))) #, 13)
print(eight(minus(three()))) #, 5)
print(six(divided_by(two()))) #, 3)