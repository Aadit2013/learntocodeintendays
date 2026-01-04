print ("hello world")
x=21
print(x)
y=21
print (f"The value of x is {x} and y is {y}")


def compare (x,y):
    if x==y:
        return "x is equal to y"
    elif x > y:
        return "x is greater than y"
    else:
        return "y is greater than x"

answer = compare(x, y)
print(answer)
# Example 2: Subtraction