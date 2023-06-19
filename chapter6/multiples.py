def isMulitiple(number, number2):
    if number % number2 == 0:
        return "true"
    else:
        return "false"


number = isMulitiple(20, 10)
print(number)
