def list_operations():
    lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
    unique_list = list(set(lst))  # Remove duplicates
    sorted_list = sorted(unique_list)  # Sort the list
    second_largest = sorted_list[-2] if len(sorted_list) > 1 else None  # Find second largest

    print("Unique List:", unique_list)
    print("Sorted List:", sorted_list)
    print("Second Largest:", second_largest)

list_operations()
def swap_tuples():
    t1 = tuple(map(int, input("Enter first tuple values separated by spaces: ").split()))
    t2 = tuple(map(int, input("Enter second tuple values separated by spaces: ").split()))

    t1, t2 = t2, t1  # Swap without extra variables

    print("Swapped Tuple 1:", t1)
    print("Swapped Tuple 2:", t2)

swap_tuples()
def set_operations():
    set1 = set(map(int, input("Enter first set values separated by spaces: ").split()))
    set2 = set(map(int, input("Enter second set values separated by spaces: ").split()))

    union_set = set1 | set2  # Union
    intersection_set = set1 & set2  # Intersection
    difference_set = set1 - set2  # Difference

    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Difference:", difference_set)

set_operations()
def highest_mark_student():
    students = {}
    n = int(input("Enter the number of students: "))

    for _ in range(n):
        name = input("Enter student name: ")
        marks = int(input(f"Enter marks for {name}: "))
        students[name] = marks

    highest_student = max(students, key=students.get)  # Find student with max marks
    print("Top Student:", highest_student, "with Marks:", students[highest_student])

highest_mark_student()
