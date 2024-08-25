# Simple Calculator

def Calculator(n1, n2, operation):
    if  operation == 'add':
        return n1 + n2
    elif operation == 'subtract':
        return n1 - n2
    elif operation == 'multiply':
        return n1*n2
    elif operation == 'division':
        if n2 == 0:
            return "Error: Division by zero is not promoted."
        return n1/n2
    else:
        return "Error: Invalid operation."
print("calculator") # Prompt the user for input
n1= float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
print("Choose the operation:\n add\n subtract\n multiply\n division")
operation = (input("Enter operation : ")).strip().lower()

res = Calculator(n1, n2, operation) # Perform the calculation
print(f"The result of {operation}ing {n1} and {n2} is: {res}") # to Display the result


