# lambda
doubler = lambda x: x * 2
print(doubler(2))
print(doubler(5))

# lambda
evenOdd = (lambda x:
           'odd' if x % 2 else 'even')

print(evenOdd(2))
print(evenOdd(3))

# lambda multiple argu
add = lambda x, y, z: x + y + z
print(add(2, 5, 10))

# ways to call lambda
# Positional arguments
add = lambda x, y, z: x + y + z
print(add(2, 3, 4))
# Prints 9

# Keyword arguments
add = lambda x, y, z: x + y + z
print(add(2, z=3, y=4))
# Prints 9

# Default arguments
add = lambda x, y=3, z=4: x + y + z
print(add(2))
# Prints 9

# *args
add = lambda *args: sum(args)
print(add(2, 3, 4))
# Prints 9

# **args
add = lambda **kwargs: sum(kwargs.values())
print(add(x=2, y=3, z=4))


# Prints 9

# lambda with filter -filter() function is similar to the map().
# It takes a function and applies it to each item in the list to create a new
# list with only those items that cause the function to return True.
def checkAge(age):
    if age > 18:
        return True
    else:
        return False


age = [5, 11, 16, 19, 24, 42]
adults = filter(checkAge, age)
# adults = filter(lambda x: x > 18, age)
# print(list(adults))
print(list(adults))

# lambda with reduce - reduce() is another Python function. It applies a
# rolling calculation to all items in a list. You can use it to calculate the
# total sum or to multiply all the numbers together.
from functools import reduce

def summer(a, b):
    return a + b

L = [10, 20, 30, 40]
result = reduce(summer, L)
print(result)
