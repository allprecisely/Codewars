def validBraces(s):
    s = list(s)
    while True:
        fin = len(s)
        for i in range(len(s)-1):
            if (s[i] == '[' and s[i+1] == ']') or (s[i] == '(' and s[i+1] == ')') or (s[i] == '{' and s[i+1] == '}'):
                del s[i], s[i]
                if len(s) == 0:
                    return True
                break
        if fin == len(s):
            return False


# def validBraces(s):
#   while '{}' in s or '()' in s or '[]' in s:
#       s=s.replace('{}','')
#       s=s.replace('[]','')
#       s=s.replace('()','')
#   return s==''

print(validBraces('[(])'))
print(validBraces('[](){}()[]{}({)}'))