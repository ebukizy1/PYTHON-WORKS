old_numbers = []


def check_list(num_list):
    for number in num_list:
        if number % 2 != 0:
            old_numbers.append(number)
    return old_numbers


result = check_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)
