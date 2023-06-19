
fastest = 0
second_fastest = 0
for number in range(10):
    userInput = eval(input("enter the speed of each runner"))
    if userInput > fastest:
        fastest = userInput
    if userInput < fastest and userInput >second_fastest:
        second_fastest = userInput
print(f"the fastest runner is {fastest}m/sc and the second to highest is {second_fastest}m/sc ")

