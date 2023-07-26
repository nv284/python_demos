"""
why use nested / inner fun
1) encapsulation  2)
def outer_function():
    x= 'ABC'
    def inner_function():
        y = 'xyz'
        print("This is the inner function.")
    print("This is the outer function.")
    inner_function()
    print(y)

"""


# demo1
def function1():  # outer function
    print("Hello from outer function")

    def function2():  # inner function
        print("Hello from inner function")

    function2()


# demo 2
def num1(x):
    def num2(y):
        return x * y

    return num2


# demo 3
def f1():  # outer function
    x = 2  # A variable defined within the outer function

    def f2(a):  # inner function
        # Let's define a new variable within the inner function
        # rather than changing the value of x of the outer function
        x = 6
        print(a + x)

    print(x)  # to display the value of x of the outer function
    f2(3)


function1()

res = num1(10)

print(res(5))


# closure in nested function - allow us to create functions that retain access to
# variables from their enclosing scope, even after the outer function has finished executing.
def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


closure_example = outer_function(10)
result = closure_example(5)
print(result)  # Output: 15

# Inner Functions Can Modify Mutable Outer Function Variables
def outer_function():
    x = [1, 2, 3]

    def inner_function():
        x.append(4)
        print("Inner x:", x)

    inner_function()
    print("Outer x:", x)


outer_function()
# nested function - Global Variables Can Be Accessed But Not Modified
x = 10


def outer_function():
    def inner_function():
        global x
        x = 20
        print("Inner x:", x)

    inner_function()
    print("Outer x:", x)


outer_function()  # Output: Inner x: 20, Outer x: 20
print("Global x:", x)



# assign fun to variables
def hello():
    print('Hello, World!')


hi = hello
hi()


# fun assign to dict
def findSquare(x):
    return x ** 2


def findCube(x):
    return x ** 3


# Create a dictionary of functions
exponent = {'square': findSquare, 'cube': findCube}

print(exponent['square'](3))
# Prints 9
print(exponent['cube'](3))
# Prints 27
