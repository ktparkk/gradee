import csv
from func import *

if argUnique("-n"): # create new semester
    # add new semester
    print("\nNew unique semester name (e.g. Spring2020): ", end =" ")
    semesterName = input()
    while newSemester(semesterName) == False:
        print("\nSemester name already exists; please retry: ", end =" ")
        semesterName = input()
    semester_csv = open(newSemester(semesterName), 'w')
    semester_writer = csv.writer(semester_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    courseNum = 1
    while True: # add courses to semester
        print("\nName of " + ordinalNum(courseNum) + " course: ", end =" ")
        courseName = input()
        courseRow = [courseName]

        assessNum = 1
        assessValueRow = ["Value"]
        while True: # add assessment types to course
            print("\nName of " + ordinalNum(assessNum) + " assessment in " + courseName + ": ", end =" ")
            courseRow.append(input())
            print("Value of " + ordinalNum(assessNum) + " assessment in " + courseName + ": ", end =" ")
            assessValueRow.append(input())
            print("\nAdd another assessment to " + courseName + "? (y/n): ", end =" ")
            answer = input()
            if answer != "y": break
            assessNum += 1
        semester_writer.writerow(courseRow)
        semester_writer.writerow(assessValueRow)

        print("\nAdd another course to " + semesterName + "? (y/n): ", end =" ")
        answer = input()
        if answer != "y": break
        courseNum += 1

    semester_writer.writerow(["Course","Assessment","Name","Grade","Date","Notes"]) # add fields for submission input(column headers)

if argUnique("-a"): # add submission
    print(listSemesters())