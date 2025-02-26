# Check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# Print Fibonacci series up to N terms
def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci series:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Check if a three-digit number is an Armstrong number
def is_armstrong(num):
    if 100 <= num <= 999:
        sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))
        if num == sum_of_cubes:
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
    else:
        print("Please enter a valid three-digit number.")

# User input
num1 = int(input("Enter a number to check if it's positive, negative, or zero: "))
check_number(num1)

n_terms = int(input("Enter the number of terms for the Fibonacci series: "))
fibonacci(n_terms)

num2 = int(input("Enter a three-digit number to check if it's an Armstrong number: "))
is_armstrong(num2)
