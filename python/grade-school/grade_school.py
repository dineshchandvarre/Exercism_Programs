# # class School(object,grade):
# #     def __init__(self):

# def addStudent(name,grade):
# 	grade1=[]
# 	grade2=[]
# 	grade3=[]
# 	grade4=[]
# 	grade5=[]
# 	if(grade==1):
# 		grade1.append(name)
# 	if(grade==2):
# 		grade2.append(name)

# 	print(grade2)

# addStudent("alexa",2)
# addStudent("robin",2)
# addStudent("alexa",1)
# addStudent("rohan",2)
from collections import defaultdict

class OrderedDefaultDict(defaultdict):
    def __missing__(self, key):
        self[key] = ()
        return self[key]

class School(OrderedDefaultDict):
    def __init__(self, name):
        self.name = name

    def add(self, student, grade):
        self[grade] += (student,)

    def grade(self, grade):
        return self[grade]

    def sort(self):
        return self.items()

