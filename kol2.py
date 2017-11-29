#!#!usr/bin/env python2.7
import json
import sys
#first word from console will be used as filename!


class Class(object):
	def __init__(self, subjects, students):
		self.register = {}
		for i in students:
			for j in subjects:
			 self.register[i]={j:{"grades":[],"presence":[]}}
			

	def add_grade(self, id, subject, grade):
		self.register[id][subject]["grades"].append(grade)

	def check_presence(self, id, subject, presence):
		self.register[id][subject]["presence"].append(presence)

	def student_average_from_subject(self, id, subject):
		return sum(self.register[id][subject]["grades"])/float(len(self.register[id][subject]["grades"]))

	def student_average_from_all_classes(self, id):
		ret = 0
		for key in self.register[id].keys():
			ret += self.student_average_from_subject(id,key)
		return ret/len(self.register[id].keys())

	def average_from_subject(self,subject):
		ret = 0
		for key in self.register.keys():
			ret += self.student_average_from_subject(key,subject)
		return ret/len(self.register)

	def total_attendance_of_a_student(self,id):
		ret = 0
		for key in self.register[id].keys():
			ret += sum(self.register[id][key]["presence"])/float(len(self.register[id][key]["presence"]))
		return ret/len(self.register[id].keys())

	def save(self, filename):
		with open(filename, 'w') as save_file:
			json.dump(self.__dict__, save_file)












### <- 50 lines from the beggining of the Class code 8-)

if __name__ == "__main__":


	filename= str(sys.argv[1])

	subjects = ["Python"]
	students = ["Andrzej Duda", "Kubus Puchatek", "Seba"]
	D = Class(subjects,students)
	D.add_grade("Andrzej Duda","Python",2)
	D.add_grade("Kubus Puchatek","Python",3)
	D.add_grade("Seba","Python",4)
	D.add_grade("Andrzej Duda","Python",2)
	D.add_grade("Kubus Puchatek","Python",3)
	D.add_grade("Seba","Python",4)
	D.check_presence("Andrzej Duda","Python",0)
	D.check_presence("Kubus Puchatek","Python",1)
	D.check_presence("Seba","Python",1)
	D.check_presence("Andrzej Duda","Python",0)
	D.check_presence("Kubus Puchatek","Python",1)
	D.check_presence("Seba","Python",0)


	for student in students:
		print student + " average from all classes " + str(D.student_average_from_all_classes(student))
		print student + " total attendance " + str(D.total_attendance_of_a_student(student))
		for subject in subjects:
			print student + " average from " + subject + " " + str(D.student_average_from_subject(student,subject))

	for subject in subjects:
		print "Average from " + subject + ": " + str(D.average_from_subject(subject))

	print "Class will be saved in a file " + filename
	D.save(filename)
