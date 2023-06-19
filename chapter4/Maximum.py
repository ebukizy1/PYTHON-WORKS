def maximum(value1, value2, value3):
    """enter the value of three integers"""
    max = value1
    if value2 > max:
        max = value2
    if value3 > max:
        max = value3

    return max


print(maximum(23, 48, 50))
print(maximum(23.5, 40.5, 12.7))
print(maximum('yellow', 'red', 'green'))

print(max([12, 60, 45]))
print(max('yellow', 'green', 'red'))
