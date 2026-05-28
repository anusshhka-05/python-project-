import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# GLOBAL DATA STORAGE

records = []
student_ids = []

# MODULE 1 – STUDENT REGISTRATION & GRADE EVALUATION

def register_student():

    name = input("Enter student name: ")
    sid = input("Enter student ID: ")
    marks = int(input("Enter marks (0-100): "))

    # Grade Evaluation
    if marks >= 90:
        grade = "O"
        remark = "Outstanding"

    elif marks >= 80:
        grade = "A+"
        remark = "Excellent"

    elif marks >= 70:
        grade = "A"
        remark = "Very Good"

    elif marks >= 60:
        grade = "B"
        remark = "Good"

    elif marks >= 50:
        grade = "C"
        remark = "Average"

    else:
        grade = "F"
        remark = "Needs Improvement"

    # Store data
    student = {
        "name": name,
        "id": sid,
        "marks": marks,
        "grade": grade,
        "courses": []
    }

    records.append(student)
    student_ids.append(sid)

    print("\n===== STUDENT REPORT =====")
    print("Name   :", name)
    print("ID     :", sid)
    print("Marks  :", marks)
    print("Grade  :", grade)
    print("Remark :", remark)
    print()

# MODULE 2 – COURSE ENROLLMENT MANAGEMENT

def enroll_courses():

    sid = input("Enter student ID: ")

    student = None

    for s in records:
        if s["id"] == sid:
            student = s
            break

    if student is None:
        print("Student not found!\n")
        return

    print("\nAdd maximum 5 courses")
    print("Type 'done' to stop\n")

    while len(student["courses"]) < 5:

        course = input("Enter course name: ")

        if course.lower() == "done":
            break

        if course == "":
            print("Invalid course!")
            continue

        student["courses"].append(course)

    print("Courses enrolled successfully!\n")

# MODULE 3 – DISPLAY STUDENT RECORDS

def display_records():

    if len(records) == 0:
        print("No student records available!\n")
        return

    print("\n========== STUDENT RECORDS ==========")

    for s in records:

        print("ID      :", s["id"])
        print("Name    :", s["name"])
        print("Marks   :", s["marks"])
        print("Grade   :", s["grade"])

        if len(s["courses"]) > 0:
            print("Courses :", ", ".join(s["courses"]))
        else:
            print("Courses : None")

        print("-----------------------------------")

    print()

# MODULE 4 – SORTING & SEARCHING

def sort_and_search():

    if len(student_ids) == 0:
        print("No student IDs available!\n")
        return

    ids = student_ids[:]

    # Bubble Sort
    n = len(ids)

    for i in range(n):

        for j in range(0, n - i - 1):

            if ids[j] > ids[j + 1]:

                temp = ids[j]
                ids[j] = ids[j + 1]
                ids[j + 1] = temp

    print("\nSorted Student IDs:")
    print(ids)

    # Linear Search
    key = input("\nEnter ID to search: ")

    found = False

    for i in range(len(ids)):

        if ids[i] == key:
            print("Student ID found at position", i)
            found = True
            break

    if not found:
        print("Student ID not found!")

    print()


# MODULE 5 – FEE CALCULATION USING FUNCTIONS

def calculate_fee(tuition=50000, hostel=0, transport=0):

    total = tuition + hostel + transport

    return total


def fee_menu():

    hostel = int(input("Enter hostel fee (0 if none): "))
    transport = int(input("Enter transport fee (0 if none): "))

    total = calculate_fee(
        hostel=hostel,
        transport=transport
    )

    print("\n===== FEE DETAILS =====")
    print("Tuition Fee :", 50000)
    print("Hostel Fee  :", hostel)
    print("Transport   :", transport)
    print("Total Fee   :", total)
    print()

# MODULE 6 – FILE HANDLING

def file_handling():

    filename = "student_records.txt"

    # Write records
    with open(filename, "w") as file:

        file.write("ID,Name,Marks,Grade\n")

        for s in records:

            line = (
                f"{s['id']},"
                f"{s['name']},"
                f"{s['marks']},"
                f"{s['grade']}\n"
            )

            file.write(line)

    print("Records written successfully!")

    # Read records
    print("\n===== FILE CONTENT =====")

    with open(filename, "r") as file:

        data = file.readlines()

        for line in data:
            print(line.strip())

    print()

# MODULE 7 – DIRECTORY SCANNING WITH EXCEPTION HANDLING

class MissingFileOrFolderError(Exception):
    pass


def scan_directory():

    path = input("Enter directory path: ")

    try:

        if not os.path.exists(path):
            raise FileNotFoundError(
                "Directory path does not exist!"
            )

        print("\nScanning Directory...\n")

        for root, dirs, files in os.walk(path):

            level = root.replace(path, "").count(os.sep)

            indent = " " * 4 * level

            print(f"{indent}{os.path.basename(root)}/")

            sub_indent = " " * 4 * (level + 1)

            for file in files:
                print(f"{sub_indent}{file}")

            if not files and not dirs:
                raise MissingFileOrFolderError(
                    f"Empty folder detected: {root}"
                )

    except FileNotFoundError as e:
        print("Error:", e)

    except MissingFileOrFolderError as e:
        print("Custom Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)

    print()



# MODULE 8 – PERFORMANCE ANALYSIS (REAL-TIME DATA)

def performance_analysis():

    if len(records) == 0:
        print("No student records available!\n")
        return

    try:

        # Create DataFrame using real-time records
        data = []

        for s in records:

            data.append({
                "Name": s["name"],
                "Marks": s["marks"]
            })

        df = pd.DataFrame(data)

        print("\n===== STUDENT PERFORMANCE DATA =====")
        print(df)

        # Statistical Summary
        print("\n===== STATISTICAL SUMMARY =====")
        print(df.describe())

        # Mean Marks
        mean_marks = np.mean(df["Marks"])

        print("\nAverage Marks :", mean_marks)

        # Top Performer
        top_student = df.loc[df["Marks"].idxmax(), "Name"]

        top_marks = df["Marks"].max()

        print("\nTop Performer :", top_student)
        print("Top Marks     :", top_marks)

        # Graph using real-time data
        plt.figure(figsize=(7, 5))

        plt.bar(df["Name"], df["Marks"])

        plt.title("Student Performance Analysis")

        plt.xlabel("Student Names")

        plt.ylabel("Marks")

        plt.show()

    except Exception as e:
        print("Unexpected Error:", e)

    print()

# MAIN DASHBOARD
def main():

    while True:

        print("======================================")
        print(" SMART CAMPUS INFORMATION SYSTEM ")
        print("======================================")
        print("1. Student Registration")
        print("2. Course Enrollment")
        print("3. Display Records")
        print("4. Sorting & Searching")
        print("5. Fee Calculation")
        print("6. File Handling")
        print("7. Directory Scanning")
        print("8. Performance Analysis")
        print("9. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            enroll_courses()

        elif choice == "3":
            display_records()

        elif choice == "4":
            sort_and_search()

        elif choice == "5":
            fee_menu()

        elif choice == "6":
            file_handling()

        elif choice == "7":
            scan_directory()

        elif choice == "8":
            performance_analysis()

        elif choice == "9":
            print("\nThank You!")
            break

        else:
            print("Invalid choice! Please try again.\n")
# PROGRAM START
if __name__ == "__main__":
    main()