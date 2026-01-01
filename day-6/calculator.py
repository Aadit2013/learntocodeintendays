# Simple Calculator Program
# This program teaches us how to use functions to perform basic math operations

# Function for addition
def add(num1, num2):
    """
    This function adds two numbers together
    
    Arguments:
        num1: The first number
        num2: The second number
    
    Returns:
        The sum of num1 and num2
    """
    result = num1 + num2
    return result


# Function for subtraction
def subtract(num1, num2):
    """
    This function subtracts the second number from the first number
    
    Arguments:
        num1: The first number (we subtract FROM this)
        num2: The second number (we subtract this)
    
    Returns:
        The difference (num1 - num2)
    """
    result = num1 - num2
    return result


# Function for multiplication
def multiply(num1, num2):
    """
    This function multiplies two numbers together
    
    Arguments:
        num1: The first number
        num2: The second number
    
    Returns:
        The product of num1 and num2
    """
    result = num1 * num2
    return result


# Function for division
def divide(num1, num2):
    """
    This function divides the first number by the second number
    
    Arguments:
        num1: The first number (we divide this)
        num2: The second number (we divide BY this)
    
    Returns:
        The quotient (num1 / num2)
    
    Special case:
        We need to be careful not to divide by zero!
    """
    # Check if num2 is zero (we cannot divide by zero!)
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    
    result = num1 / num2
    return result


# Main program - This is where we use our functions
print("=" * 40)
print("       WELCOME TO MY CALCULATOR!")
print("=" * 40)
print()

# Example 1: Addition
print("Example 1: ADDITION")
print("Question: What is 10 + 5?")
answer1 = add(10, 5)
print(f"Answer: {answer1}")
print()

# Example 2: Subtraction
print("Example 2: SUBTRACTION")
print("Question: What is 20 - 7?")
answer2 = subtract(20, 7)
print(f"Answer: {answer2}")
print()

# Example 3: Multiplication
print("Example 3: MULTIPLICATION")
print("Question: What is 6 × 9?")
answer3 = multiply(6, 9)
print(f"Answer: {answer3}")
print()

# Example 4: Division
print("Example 4: DIVISION")
print("Question: What is 50 ÷ 5?")
answer4 = divide(50, 5)
print(f"Answer: {answer4}")
print()

# Example 5: Division by Zero (Special Case)
print("Example 5: DIVISION (Special Case - Division by Zero)")
print("Question: What is 10 ÷ 0?")
answer5 = divide(10, 0)
print(f"Answer: {answer5}")
print()

# Interactive Calculator - Let the user try!
print("=" * 40)
print("    TRY THE CALCULATOR YOURSELF!")
print("=" * 40)
print()

# Ask user for first number
num1 = float(input("Enter the first number: "))

# Ask user for second number
num2 = float(input("Enter the second number: "))

# Ask user what operation they want to do
print("\nWhat operation do you want to do?")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (×)")
print("4. Division (÷)")

operation = input("\nEnter your choice (1/2/3/4): ")

# Perform the operation the user chose
if operation == "1":
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == "2":
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == "3":
    print(f"{num1} × {num2} = {multiply(num1, num2)}")
elif operation == "4":
    print(f"{num1} ÷ {num2} = {divide(num1, num2)}")
else:
    print("Invalid choice! Please enter 1, 2, 3, or 4")

print()
print("=" * 40)
print("     Thank you for using the calculator!")
print("=" * 40)
