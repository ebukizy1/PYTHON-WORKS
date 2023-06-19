
# def swaping(a, b):
#     value= a,b = b, a
#     return value
#
# # print(swaping(2,5))
# #
# lst = [25, 10, 15, 5, 30, 55, 35, 45]
# # # for number in lst:
# # #     minimum = lst[0]
# # #     if lst > minimum:
# # #         minimum[number]
# # # print(minimum)
# def arrangement(lst):
#     for i in range(len(lst)):
#         minimum = i
#         for j in range(i+1, len(lst)):
#              if lst[j] < lst[minimum]:
#                 minimum = j
#                 total = lst[i], lst[minimum] = lst[minimum], lst[i]
#                 return lst
#
# #
# # print(arrangement(lst))# print(swaping(2,5))
# #
# lst = [25, 10, 15, 5, 30, 55, 35, 45]
# # # for number in lst:
# # #     minimum = lst[0]
# # #     if lst > minimum:
# # #         minimum[number]
# # # print(minimum)
# def arrangement(lst):
#     for i in range(len(lst)):
#         minimum = i
#         for j in range(i+1, len(lst)):
#              if lst[j] < lst[minimum]:
#                 minimum = j
#                 total = lst[i], lst[minimum] = lst[minimum], lst[i]
#                 return lst

#
# print(arrangement(lst))
even = (i for i in range(21) if i % 2 == 0)
print(even)