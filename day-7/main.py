from hello import compare
if __name__ == "__main__":
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))

    answer = compare(x, y)
    print(answer)
