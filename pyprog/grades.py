#results


invalid = 1

while invalid == 1:
	invalid = 0
	students = raw_input("How many students are there: ")
	students = int(students)
	if students <= 0:
		print "0 invalid choice. Must be at least 1 student."
		invalid = 1

A = 0
B = 0
C = 0
D = 0
E = 0


for i in range(students):
	subinvalid = 1
	while subinvalid == 1:
		subinvalid = 0
		grade = raw_input("Please enter the student's grade: ")
		grade = int(grade)
		if grade < 0 or grade > 100:
			print "Invalid, grade must be between 0 and 100."
			subinvalid = 1
		if grade >= 70 and grade <= 100:
			A= A + 1
		elif grade >=60 and grade <= 69:
			B= B + 1		
		elif grade >=50 and grade <= 59:
			C= C + 1
		elif grade >=40 and grade <= 49:
			D= D + 1
		elif grade <=39:
			E= E + 1
		
print "Option 1: Display student grades."
print "Option 2: Quit."
invalid = 1

while invalid == 1:
	invalid = 0
	choice = raw_input("Type 1 for option 1 or type 2 for option 2.")
	if choice == "1":
		print "A", A
		print "B", B
		print "C", C
		print "D", D
		print "E", E	
	if choice == "2":
		print