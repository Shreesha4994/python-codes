class student:

	def __init__(self):
		self.student_name = None
		self.student_rollno = None
		self.student_marks = [0]*3
		self.total_marks = 0
		self.average = 0
	
	def calc_total(self):
		for mark in self.student_marks:
			self.total_marks+=mark
		return self.total_marks
	
	def calc_average(self):
		return self.total_marks/3

	def display(self):
		print("Name: ", self.student_name)
		print("Roll No: ", self.student_rollno)
		print("Total Marks: ", self.calc_total())
		print("Average Marks: ", self.calc_average())
	
	def set_name_rollno_marks(self, name, rollno, mark1, mark2, mark3):
		self.student_name = name
		self.student_rollno = rollno
		self.student_marks[0]=mark1
		self.student_marks[1]=mark2
		self.student_marks[2]=mark3

s1 = student()
s1.set_name_rollno_marks("Rahul",21,42,54,76)
s1.display()

s2 = student()
s2.set_name_rollno_marks("Raj",22,54,56,78)
s2.display()
