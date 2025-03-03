def list_operations():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    unique_sorted = sorted(set(nums))  # Remove duplicates and sort
    print("Unique List:", unique_sorted)
    print("Second Largest:", unique_sorted[-2] if len(unique_sorted) > 1 else "N/A")

list_operations()
def swap_tuples():
    t1 = tuple(map(int, input("Enter first tuple values: ").split()))
    t2 = tuple(map(int, input("Enter second tuple values: ").split()))
    t1, t2 = t2, t1  # Swapping in one step
    print("Swapped Tuples:", t1, t2)

swap_tuples()
def set_operations():
    s1, s2 = set(map(int, input("Enter first set values: ").split())), set(map(int, input("Enter second set values: ").split()))
    print("Union:", s1 | s2, "\nIntersection:", s1 & s2, "\nDifference:", s1 - s2)

set_operations()
def highest_mark_student():
    students = {input("Enter student name: "): int(input("Enter marks: ")) for _ in range(int(input("Enter number of students: ")))}
    top_student = max(students, key=students.get)
    print("Top Student:", top_student, "with Marks:", students[top_student])

highest_mark_student()
