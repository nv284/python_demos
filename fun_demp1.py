# create function
def course_func(name, course_name):
    print("Hello", name, "Welcome to PYnative")
    print("Your course name is", course_name)


# call function
course_func('John', 'Python')


def calculate(a, b):
    add = a + b
    return add


res = calculate(5, 8)
print("Addition - ", res)


# docstring. It is a descriptive text (like a comment) written by
# a programmer to let others know what block of code does.
def any_fun(parameter1):
    """
       Description of function

       Arguments:
       parameter1(int):Description of parameter1

       Returns:
       int value
    """


print(any_fun.__doc__)


# function return multiple value
def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    multiply = num1 * num2
    division = num1 / num2
    # return four values
    return add, sub, multiply, division


# read four return values in four variables
a, b, c, d = arithmetic(10, 2)

print("Addition: ", a)
print("Subtraction: ", b)
print("Multiplication: ", c)
print("Division: ", d)


# When the interpreter finds a pass statement in the program, it returns no operation.
def addition(num1, num2):
    # Implementation of addition function in comming release
    # Pass statement
    pass


addition(10, 2)
