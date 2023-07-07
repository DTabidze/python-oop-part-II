from random import random

class User:

    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        if(type(age) not in (int,float) or age<18):
            raise ValueError("age must be an integer or float of at least 18")
        self._age=age

    def __repr__(self):
        return f"{type(self).__name__} Info => first name: {self.fname}, last name: {self.lname}, age: {self.age}"


class Student(User):

    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)

    def register(self,course):
        course.students.append(self)

class Instructor(User):
    
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)


class Course:

    def __init__(self,title,instructor=None):
        self.title=title
        self.instructor=instructor
        self.students=[]

    def set_instructor(self,instructor):
        if(instructor!=None and not type(instructor)==Instructor):
            raise ValueError("Instructor must be an instructor object")
        self._instructor=instructor

    def get_instructor(self):
        return self._instructor

    def __repr__(self):
        return f"{type(self).__name__} title: {self.title} instructor: {self.instructor} students: {self.students}"
    
    instructor=property(get_instructor,set_instructor)

    

#courses
course_titles=["math","english","social studies","science","computer","art"]
courses=[]
for i in range(len(course_titles)):
    courses.append(Course(course_titles[i]))

#instructors
first_names=["Sarah","Kate","William","Robert"]
last_names=["Campbell","Anderson","Miller","Wilson"]
ages=[33,35,37,38]
instructors=[]
for i in range(len(first_names)):
    instructors.append(Instructor(first_names[i],last_names[i],ages[i]))

#students
first_names=["Mary","Bob","Sam","Matt"]
last_names=["Johnson","Smith","Garcia","Rodriguez"]
ages=[22,24,25,27]
students=[]
for i in range(len(first_names)):
    students.append(Student(first_names[i],last_names[i],ages[i]))

#assign instructors to courses
for i in range(len(courses)):
    randIdx=int(len(instructors)*random())
    courses[i].set_instructor(instructors[randIdx])

#students register for courses
for i in range(4):
    randIdxCourses=int(len(courses)*random())
    randIdxStudents=int(len(students)*random())
    students[randIdxStudents].register(courses[randIdxCourses])

for course in courses:
    print(course)
    print()