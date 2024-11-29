# lst_1 = [1, 2 ,3 ,4, 5, 6]

# for el in lst_1:
#     if el == 3:
#         continue

#     print(el)

# lst_2 = []
# lst_2.append(1)
# lst_2.append(8)
# lst_2.extend([2, 4, 5, 7])

# first_el, second_el, *_ = lst_2

# print(first_el)
# print(second_el)

# tpl_1 = (1, 2, 3, 4, 5)

# print(tpl_1[1])

# tpl_2 = (1, 2, 3, [1, 2, 4,], "asd", "erf")
# print(len(tpl_2))
# print(tpl_2[3])
# tpl_2[3][2] = "test"
# tpl_2[3].append("new")
# print(tpl_2)

# tpl_3 = 123, "er"

# print(type(tpl_3))

# set_1 = {1, 2, 44, 55, 16, 7}

# for el in set_1:
#     print(el)

# list_5 = [1, 2, 1, 2, "a", "a"]

# set_2 = set(list_5)
# print(set_2)

# dict_1 = {
#     1: "ase", 
#     2: "33", 
#     "from": "I"
# }

# dict_1.update({"I am": "Betmen"})

# # for k, v in dict_1.items():
# #     print(f"k = {k}, v = {v}")

# print(dict_1[1])

# print(dict_1.get("true", "За тим ключом ніхуя нема"))

list_6 = [1, 2, 3, 4, 5]
lst_7 = [1, 4, 5, 5, 8]

# sum = 0

# for el in list_6:
#     sum += el

# print(sum)

def sum(lst):
    """
    Say sum function
    """
    sum = 0
    for el in lst:
        sum += el
    return sum
    

print(sum(list_6))
print(sum(lst_7))