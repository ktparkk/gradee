import csv
from func import *

if argUnique("-n"): # create new semester
    # add new semester
    print("\nNew unique semester name (e.g. Spring2020)")
    semesterName = input()
    while newSemester(semesterName) == False:
        print("\nSemester name already exists; please retry: ")
        semesterName = input()
    semester_csv = open(newSemester(semesterName), 'w')
    semester_writer = csv.writer(semester_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # add courses to semester
    courseNum = 1
    print("Name of " + ordinalNum(courseNum) + " course: ")
    courseName = input()
    courseRow = [courseName]

    assessNum = 1
    assessValueRow = ["Value"]
    while True: # add assessment types to course
        print("Name of " + ordinalNum(assessNum) + " assessment in " + courseName + ": ")
        courseRow.append(input())
        print("Value of " + ordinalNum(assessNum) + " assessment in " + courseName + ": ")
        assessValueRow.append(input())
        print("Add another assessment to " + courseName + "? (y/n): ")
        answer = input()
        if answer != "y": break
        assessNum += 1
        
    semester_writer.writerow(courseRow)
    semester_writer.writerow(assessValueRow)







    semester_writer.writerow(["Course","Assessment","Name","Grade","Date","Notes"]) # add fields for submission input(column headers)
    