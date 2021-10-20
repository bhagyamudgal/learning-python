# Add function
def add(x=0, y=0):
    return x + y


result = add(10, 20)
print(result)
result = add()
print(result)


# *args -> return tuples
def myfunc(a, b):
    return sum((a, b)) * 0.05


result = myfunc(40, 60)
print(result)


def myfunc2(*args):
    return sum(args)


result = myfunc2(10, 20, 30, 40, 50, 60, 70, 80)
print(result)


# **kwargs -> return dictionaries
def myfunc(**kwargs):
    for key in kwargs:
        print(key)


myfunc(Name="Bhagya", age=19)


# Lambda Expressions Map and Filter
def square(num):
    return num**2


mynums = [1, 2, 3, 4, 5]
for item in map(square, mynums):
    print(item)

print(list(map(square, mynums)))


def check_even(num):
    return num % 2 == 0


print(list(filter(check_even, mynums)))

square = lambda num: num**2
print(square(3))

print(list(map(lambda num: num * num, mynums)))

# LEGB Rule
# L -> Local (def,lambda)
# E -> Enclosing functions (def,lambda)
# G -> Global
# B -> Built-in