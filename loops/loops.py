my_list = ["Hello", "Bhagya", "Mudgal"]
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_dic = {"fname": "Bhagya", "lname": "Mudgal", "age": 19}

# For loop
for item in my_list:
    print(item)

for num in my_list2:
    print(num * 2)

for letter in "Bhagya Mudgal":
    print(letter)

for key in my_dic:
    print(key)

for key, value in my_dic.items():
    print(key, value)

for num in range(0, 11, 2):
    print(num)

# While loop
x = 10
while x > 5:
    print(x)
    x = x - 1

# break, continue, pass
for item in my_list2:
    pass  # do nothing can be used as placeholder

for item in my_list2:
    if (item % 2 == 0):
        continue  # skip this step
    print(item)

for item in my_list2:
    if (item == 3):
        break  # break on this condition
    print(item)
