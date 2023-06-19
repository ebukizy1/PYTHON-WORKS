# def isDivisible(number):
#     for num in range(1,number):
#         number2 = int(input("enter numbers of input"))
#         if number2 % 5 == 0:
#             return "true"
#         else:
#             return "false"
#
# cunt
# number2 = int(input("enter numbers of input"))
# result = isDivisible(number2)
# print(result)

def isDivisible(number2):
    count = 1
    while count < number2:
        number2 = int(input("enter numbers of input"))
        if number2 % 5 ==0:
                print("true")
    else:
                print("false")


print(isDivisible(10))

