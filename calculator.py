#making a calculator using functions, under the functions block

# This is a simple calculator program that performs basic arithmetic operations
def calculator(num1, num2, operation):
    def addition(a, b): 
        return a + b
    
    def subtraction(a, b):
        return a - b
    
    def multiplication(a, b):
        return a * b
    
    def division(a, b):
        if b == 0:
            return "Division by zero is not allowed"
        return round(a / b, 3)
    
    # Dictionary to map operations to functions
    # This allows us to call the appropriate function based on user input
    operations = {
        'add': addition,
        'sub': subtraction,
        'mult': multiplication,
        'div': division
    }

    # Check if the operation is valid and call the corresponding function
    # If the operation is not valid, return an error message
    if operation in operations:
        return operations[operation](num1, num2)
    else:
        return "Invalid operation. Please choose from the following operations: add, sub, mult, div."
    
# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, sub, mult, div)): ")

# Call the calculator function and print the results
result = calculator(num1, num2, operation)

# Print the results
print("Result:", result)