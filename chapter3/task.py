# a =1
# b = 2
# a,b = b, a
#
# print(a, b)
#
# lst = [25, 10, 15, 5, 30, 55, 35, 45]
# for number in lst:
#     minimum = lst[0]
#     if lst > minimum:
#         minimum[number]
# print(minimum)
lst = [25, 10, 15, 5, 30, 55, 35, 45]

for i in range(len(lst)):
    minimum = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[minimum]:
            print
            minimum = j
            lst[i], lst[minimum] = lst[minimum], lst[i]
# print(lst)

set1 = {6, 2, 5, 4, 1}
new_value = sorted(set1)
print(new_value)
