# Q1
# Return
# 1.The first item in the list. ✅
# 2.The third item in the list. ✅
# 3.The last item in the list. ✅
# 4.The first three items in the list. ✅
# 5.The last three items in the list. ✅
#   print(foods[len(foods)-3:len(foods)])
# 6.The last item in the sublist.

foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
    ]

# print(foods[-3:-1])
# This prints passionfruit and kiwifruit because -1 is not inclusive of the final item when using slice(I think?) 

#print(len(foods[-4]))
# prints 4

# print(foods[-1])
# prints kiwifruit 



# 1,2,3
# print(ls[a,b]) : print items from a to b-1

# Q2
# Format and print the following list:
mailing_list = [
    "Chilli", "chilli@thechihuahua.com"
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"]
]

# Q3
name1 = input("Enter a name:")
name2 = input("Enter a name:")
name3 = input("Enter a name:")

list_of_names = [name1, name2, name3]
print(list_of_names)

list_of_names.append(name3)


############## Q4 ##############
#Using the following starter code:
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []



f = [a, b, c]
# print(f)

# f = a + b + c
# print(f)

a.extend(b)
a.extend(c)
print(a)

f = [*a, *b, *c]
print(f)

# Produce the following lists:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
