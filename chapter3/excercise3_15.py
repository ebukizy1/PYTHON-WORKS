
first_number = 0
second_number = 1
third_number = 0

for number in range(10):
   third_number = first_number + second_number
   first_number = second_number
   second_number = third_number
   print(first_number)