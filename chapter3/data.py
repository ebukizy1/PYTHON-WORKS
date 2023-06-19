# my_number = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17,18,19,20 ]
# old_number = []
# for num in my_number:
#     if num % 2 !=0:
#         old_number.append(num)
# print(old_number)
# my_number[4: 10] = [0]*5
# print(my_number)
# my_seven = my_number[:7]
# print(my_seven)
# my_number= []
# # print(my_number)
# list1 = list(range(1,21))
# print(list1)
# odd_numbers = list1[::2]
# print(odd_numbers)
# list1[4:10] = [0] * len(list1[5:10])
# print(list1)
# letters = ("a", "b", "c")
# print(letters)
# number = 1, 2, 3
# print(type(number))
# alpha_num = letters + number
# list = [1, "1", "a", 2]
# print(list[1:4])

# number = tuple(range(1,500))
# even_numbers = number[1:500:2]
# print(even_numbers)
# odd_number = number[::2]
# # print(odd_number)
# # total = even_numbers + odd_number
# # letters = ("a", "b", "c")
# # number = 1, 2, 3, 4,5,6
# #
# x, y, z, *others = number
# print(x, y, z, others )
#
# my_dict = {'key1': 'value', 'key2':'mylove'}
# my_prices = {'apple': 400, 'orange':250, 'egg':700}
# print(my_prices['egg'])
d = {'k1':123, 'k2':['a','b','c', 'd'],'k3':{'inside':100}}
print(d['k3']['inside'])
list = d['k2']
print(list)
letter = list[2]
print(letter.upper())
print(d['k2'][2].upper())
d['k2'] = 'rotimi'
d['k3'] = '600'
print(d.keys())
print(d.values())
print(d.items())

list1 = {65, 1, 1,1,1, 2, 2, 3, 4, 4, 5, 54,3,23,78}
set2 = {1, 2, 3, 4,5,6,54,33,32}
# my_sorted = sorted(list1)
# print(my_sorted)
# disjout it means what is not common in both set
# print(set2 ^ list1)
#
# if 8 in list1:
#     print('yes')
# else:print('no')
set2.add(10)
print(set2)








