def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
def factorial_for_loop(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

if __name__ == "__main__":
    
    num = int(input("Enter a number to compute its factorial: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")