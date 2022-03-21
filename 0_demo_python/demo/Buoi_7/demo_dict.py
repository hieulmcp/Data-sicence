# dict_1 = {
#     'one': 1, 
#     'two': 2, 
#     'three': 3,
#     'four': 4,
#     'five': 5,
#     'one': 6
# }

# print(dict_1)
# print(dict_1['one'])


# list_nums = [4, 5, 6, 1, 2, 3, 7, 8, 9]
# print(list_nums)
# list_nums.clear()
# print(list_nums)


# dict_1 = {
#     'one': 1, 
#     'two': 2, 
#     'three': 3,
#     'four': 4,
#     'five': 5,
#     'one': 6
# }

# print(dict_1['one'])

# d = str(dict_1)
# print(d[0])




# dict_1 = {
#     'one': 1, 
#     'two': 2, 
#     'three': 3,
#     'four': 4,
#     'five': 5,
#     'one': 6
# }
# print(dict_1)
# dict_2 = dict_1.copy()
# dict_2['three'] = 30
# print(dict_2)
# print(dict_1)


# list_nums = [4, 5, 6, 1, 2, 3, 7, 8, 9, 4]
# dict_2 = dict.fromkeys(list_nums, "abc")
# print(dict_2)


# dict_1 = {
#     'one': 1, 
#     'two': 2, 
#     'three': 3,
#     'four': 4,
#     'five': 5,
#     'one': 6
# }
# print(dict_1['one'])
# print(dict_1.get('one'))



dict_1 = {
    'one': 1, 
    'two': 2, 
    'three': 3,
    'four': 4,
    'five': 5,
    'one': 6
}
for item in dict_1:
    print(item, '--', dict_1[item])

print()

for key, value in dict_1.items():
    print(key, '--', value)

# a = list(dict_1.items())
# print(a)

