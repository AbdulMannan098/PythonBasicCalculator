num1:float=float(input("Enter First Number: "))
num2:float=float(input("Enter Second Number: "))
operation:str=str(input("Enter the operation (+, -, *, /):"))
result:float
if operation == '+':
    result=num1 + num2
elif operation == '-':
    result=num1 - num2
elif operation == '*':
    result=num1 * num2
elif operation == '/':
    result=num1 / num2
else:
    print("Invalid operation")

# Displaying the result
print(f"The result of {num1} {operation} {num2} is {int(result)}.")