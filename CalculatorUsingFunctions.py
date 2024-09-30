import math

# Define all your functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def mod(a, b):
    return a % b

def power(a, b):
    return a ** b

def sqrt(a):
    return a ** (1 / 2)

def cbrt(a):
    return a ** (1 / 3)

def fact(a):
    if a == 0:
        return 1
    return a * fact(a - 1)

def sin(a):
    return math.sin(math.radians(a))  # Convert to radians

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def cot(a):
    return 1 / math.tan(math.radians(a))

def sec(a):
    return 1 / math.cos(math.radians(a))

def cosec(a):
    return 1 / math.sin(math.radians(a))

def log(a, b):
    return math.log(a, b)

def ln(a):
    return math.log(a)

def log10(a):
    return math.log10(a)

def calculator():
    num1 = float(input("Enter First Number: "))
    operation = input("Enter the operation (+, -, *, /, ^, mod, sqrt, cbrt, sin, cos, tan, cot, sec, cosec, log, log10, ln, fact): ")

    if operation == 'sqrt':
        result = sqrt(num1)
    elif operation == 'cbrt':
        result = cbrt(num1)
    elif operation == 'sin':
        result = sin(num1)
    elif operation == 'cos':
        result = cos(num1)
    elif operation == 'tan':
        result = tan(num1)
    elif operation == 'cot':
        result = cot(num1)
    elif operation == 'sec':
        result = sec(num1)
    elif operation == 'cosec':
        result = cosec(num1)
    elif operation == 'ln':
        result = ln(num1)
    elif operation == 'log10':
        result = log10(num1)
    elif operation == 'fact':
        result = fact(int(num1))  # Factorial works only for integers
    else:
        # For binary operations, get the second number
        num2 = float(input("Enter Second Number: "))
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = sub(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == 'mod':
            result = mod(num1, num2)
        elif operation == '^':
            result = power(num1, num2)
        elif operation == 'log':
            result = log(num1, num2)
        else:
            print("Invalid operation")
            result = None

    # Displaying the result if a valid operation was chosen
    if result is not None:
        print(f"The result of the calculation is: {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()
