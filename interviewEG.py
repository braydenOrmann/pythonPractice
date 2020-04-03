# Write and execute a function that accepts two numbers, checks that they are
# valid numbers, adds the numbers together and return the result as a string

def func(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        newNum = num1 + num2
        return str(newNum)
    else:
        print("Numbers are not intergers")

print("The result is:", func(56, 2))
