def factorial_recursive(n):
    if n < 0:
        return "Cannot find factorial of a negative number"
    return 1 if n in (0, 1) else n * factorial_recursive(n - 1)

def factorial_iterative(n):
    if n < 0:
        return "Cannot find factorial of a negative number"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def count_characters(s):
    return {char: s.count(char) for char in set(s)}

def is_palindrome(s):
    return s == s[::-1]

num = int(input("Enter a number: "))
print("Factorial (Recursive):", factorial_recursive(num))
print("Factorial (Iterative):", factorial_iterative(num))

string = input("Enter a string: ")
print("Character Count:", count_characters(string))

palindrome_str = input("Enter a string to check palindrome: ")
print("Is Palindrome:", is_palindrome(palindrome_str))
