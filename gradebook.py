"""
GradeBook Analyzer
Author: Vansh Viraj Bisht
Date:1/12/25
Description: CLI program to import student marks, analyze them, assign grades,
filter pass/fail students, and print formatted tables.
"""

import csv



def manual_entry():
    marks = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        score = int(input("Enter marks: "))
        marks[name] = score
    return marks


def csv_import():
    marks = {}
    file = input("Enter CSV file path: ")
    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                marks[row[0]] = int(row[1])
    except:
        print("Error loading CSV file")
    return marks




def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    values = sorted(marks.values())
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (values[mid-1] + values[mid]) / 2
    else:
        return values[mid]

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())




def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades



def pass_fail_filter(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    return passed, failed


def print_table(marks, grades):
    print("\nName\tMarks\tGrade")
    print("-" * 30)
    for name in marks:
        print(f"{name}\t{marks[name]}\t{grades[name]}")


def main_menu():
    print("\n==== GradeBook Analyzer ====")
    print("1. Manual Entry")
    print("2. Import from CSV")
    print("3. Exit")
    choice = input("Choose option: ")
    return choice




def main():
    print("Welcome to GradeBook Analyzer (By Vansh Viraj Bisht)\n")

    while True:
        choice = main_menu()

        if choice == "1":
            marks = manual_entry()

        elif choice == "2":
            marks = csv_import()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")
            continue

        
        print("\n--- Analysis Summary ---")
        print(f"Average Marks: {calculate_average(marks):.2f}")
        print(f"Median Marks : {calculate_median(marks)}")
        print(f"Max Marks    : {find_max_score(marks)}")
        print(f"Min Marks    : {find_min_score(marks)}")

        grades = assign_grades(marks)
        print_table(marks, grades)

        passed, failed = pass_fail_filter(marks)
        print(f"\nPassed Students ({len(passed)}): {passed}")
        print(f"Failed Students ({len(failed)}): {failed}")

        again = input("\nRun again? (y/n): ")
        if again.lower() != 'y':
            break


if __name__ == "__main__":

    main()
