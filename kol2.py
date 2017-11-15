# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

#!#!usr/bin/env python2.7

class Student:
    
    
    def __init__(self, name, surname, id):
		self.name = name
		self.surname = surname
		self.id = id
		self.subjects_ids = []
		self.average = 0


class Diary:
	

	def __init__(self, school_name):
		self.school_name = school_name
		self.number_of_students = 0
		self.number_of_subjects = 0
		self.subjects = []
		self.students = [] 
	
	def get_average_from_subject(self,subject_id):
		tmp = self.subjects[subject_id].grades
		ret = 0		

		for row in range (len(tmp)):
    		for col in range(len(tmp[0])):
				ret += tmp[row][col]
		return ret/(len(self.subjects[subject_id].students_ids)*number_of
	
	def get_average_for_student(self):
		pass

class Subject:

	
	def __init__(self, subject_name, id):
		self.subject_name = subject_name
		self.subject_id = id
		self.students_ids= []
		self.grades = []
		self.number_of_grades = 0
		self.number_of_classes = 0
		self.present = []

	def enroll_students(self, students_ids):
		self.students_ids = students_ids

	def get_average_of_students(self):
		pass

	def input_grades(self, grades):
		self.number_of_grades += 1
		self.grades.append(grades)
	def check_attendance(self, attendance)
		self.number_of_classes += 1
		self.present.append(grades)
		
