def rectangle_rotation(a, b):
    a, b = int(a//(2**0.5)), int(b//(2**0.5))
    if (a % 2 == 0 and b % 2 == 0) or (a % 2 == 1 and b % 2 == 1):
        return a * b + (a + 1) * (b + 1)
    return a * (b + 1) + (a + 1) * b

print( rectangle_rotation(6,4)) #,23)
print( rectangle_rotation(30,2)) # ,65)
print( rectangle_rotation(8,6)) #,49)
print( rectangle_rotation(16,20)) #,333)print
