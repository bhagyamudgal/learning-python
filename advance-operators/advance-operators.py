my_list = [1, 2, 3]

# Generate a range
for num in range(10):
    print(num)

print("\n")

# enumerate
word = "abcde"

for index, value in enumerate(word):
    print(index, value)

my_list2 = ["a", "b", "c", "d"]

# zip lists
zip_list = list(zip(my_list, my_list2))
print(zip_list)

for item in zip(my_list, my_list2):
    print(item)

# check if some value present in a data structure
print(1 in my_list)
print(10 in my_list)

# min element
print(min(my_list))

# max element
print(max(my_list))

# user input -> always accept every input as a string
user_input = input("Enter a name: ")
print(f"Hello {user_input}")