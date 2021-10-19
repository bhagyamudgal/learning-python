# Variables
num1 = 10
num2 = 5
num3 = 2
num4 = 3
print("Sum of 10 and 5 is", num1 + num2)
print("Differnce of 10 and 5 is", num1 - num2)
print("Product of 10 and 5 is", num1 * num2)
print("Dividend of 10 and 5 is", num1 / num2)
print("Remainder of 10 and 5 is", num1 % num2)
print("2 to the power of 3 is", num3**num4)
print("BODMAS rule applies [ 2 + 10 * 10 + 3 ] here",
      num3 + num1 * num1 + num4)
print("BODMAS rule applies [ (2 + 10) * (10 + 3) ] here",
      (num3 + num1) * (num1 + num4))

# Check data type using type()
print(type(num1))

#Strings
my_string = "Bhagya Mudgal"

# Printing str length using len()
print(len(my_string))

# String slicing
print(my_string[7:13:2])

# Reverse string
print(my_string[::-1])

# Strings are immutable
# name="Bhagya"
# name[0]="M"
# it will not work

# String concatenation
name = "Bhagya"
last = name[1:]
name = "M" + last
print(name)

# Multiply string
letter = "B"
letter = letter * 10
print(letter)

# String methods
my_string2 = "Bhagya Mudgal"
print(my_string2.upper())
print(my_string2.lower())
print(my_string2.split())  # Default split on white space

# String interpolation
print("Bhagya {}".format("Mudgal"))
print("Bhagya {} Mudgal".format("is"))
print("Bhagya {1} Mudgal {2}".format("is", "am", "are"))
print("Bhagya {a} Mudgal {ar}".format(i="is", a="am", ar="are"))

# Float formatting
result = 100 / 777
print("Result is", result)
print("Result is {}".format(result))
print("Result is {:1.3f}".format(result))  # {value:width:precision}

# Another way
name = "Bhagya"
print(f"Hi {name}")

# List
my_list = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8]
print(my_list)
print(len(my_list))
print(my_list[-2])
print(my_list + my_list2)

# List are mutable
my_list2[2] = 9
print(my_list2)
my_list.append(100)
print(my_list)
pop_item = my_list.pop()
print("Pop item is {}".format(pop_item))

# Sort list
my_list = [34, 94, 24, 82, 12]
my_list.sort()
print(my_list)

# Dictionaries -> Key value pair (Object in JS)
my_dict = {"name": "bhagya", "age": 19}
print(my_dict)
print(my_dict["age"])

# Dictionaries are mutable
my_dict["name"] = "John"
print(my_dict)

# Dictionaries methods
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# Tuples -> are immutable
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
print(my_tuple)
print(my_list)
# my_tuple[2]=4 .... it will generate error

# Sets -> unique items only
my_set = set()
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(3)
print(my_set)
my_set.add(1)
print(my_set)

# Boolean -> true || false
boolean = 1 > 2
print(boolean)
