import os
import sys

def argUnique(arg): # check that script has only one additional argument, string arg
    if len(sys.argv) == 2 and sys.argv[1] == arg: return True
    return False

def extension(f): # return file extension from filename f
    return f[f.rfind('.')+1:len(f)]
def hasTitle(f,title): # check if str title is in the beginning of str f 
        if len(f) > len(title):
            if f[0:len(title)] == title: return True
        else: return False
def tag(f,title): # return substring of str f after initial substring title in str f
        if hasTitle(f,title):
            return f[len(title):f.rfind('.')]
def listSemesters():
    semesters = [] # list of Semester csv files
    for f in os.listdir():
        if hasTitle(f,"Semester") and extension(f) == "csv":
            semesters.append(f)
    return semesters
def newSemester(name): # return file name for new semester name
    semesters = listSemesters()
    for f in semesters:
        if tag(f,"Semester_") == name:
            return False
    return "Semester_"+name+".csv"

# https://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers/41301
def ordinalNum(n): # return string of ordinal number equivalent of int n (e.g. ordinalNum(3) = "3rd")
    SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = SUFFIXES.get(n % 10, 'th')
    return str(n) + suffix
