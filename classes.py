def avg(list):
    return sum(list)/len(list)

class Submission:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Assessment:
    def __init__(self, name, value, submissions):
        self.name = name # type of assessment, e.g. "Exams", "Homework"
        self.value = value # percentage of final grade, e.g. "0.20" (20%)
        self.submissions = submissions # list of submissions in assessment
        if len(submissions) > 0:
            self.grade = avg([i.grade for i in submissions]) # average grade of all submissions in assessment

class Course:
    def __init__(self, name, assessments):
        self.name = name # name of course, e.g. "MATH 2212"
        self.assessments = assessments # list of assessments in course
        self.grade = 0
        scale = 0
        for a in assessments:
            if hasattr(a,'grade'):
                self.grade += a.grade * a.value
                scale += a.value
        self.grade = self.grade / a.value

class Semester:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

class Record:
    def __init__(self, semesters):
        self.semesters = semesters