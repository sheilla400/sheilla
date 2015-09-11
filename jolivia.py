
student_list=[]
library_list=[]

class Student(object):
	def __init__(self, sname, sidno, my_bag=[] ):
		self.sname = sname
		self.sidno = sidno
		self.my_bag=my_bag

class Book(object):
	def __init__(self, bname, bidno, bcost):
		self.bname = bname
		self.bidno = bidno
		self.bcost = bcost

class Librarian(object):
	def __init__(self, lname, lidno, books_lent=[],library=[] ):
		self.lname= lname
		self.books_lent=books_lent
		self.library= library
		self.lidno=lidno

class System(object):
	if __name__ == "__main__":
		while True:

			print "Welcome to makerere University Library system"
			print "1.Register a Student"
			print "2.Register a book"
			print "3.Borrow a book"
			print "4.Return a book"
			print "5.View registered students"
			print "6.View registered books"
			print "7.Exit"
			choice = int(raw_input('Select an option [1-7] and "Enter": '))
			choice = int(choice)

			if choice == 1:
				print "Registering a student.."
				sname = raw_input("Enter student name: ")
				sidno = raw_input("Enter student ID number: ")
				student=Student(sname, sidno)
				student_list.append(student)
				print "Student registered successfully!"
				print len(student_list)

			elif choice == 2:
				print "Registering a book.."
				lname = raw_input("Enter librarian name: ")
				lidno = raw_input("Enter ID number: ")
				bname = raw_input("Enter Book name: ")
				bidno = raw_input("Enter Book number: ")
				bcost = raw_input("Enter Book cost: ")
				librarianx=Librarian(lname, lidno, books_lent=[],library=[] )
				library=[]
				book=Book(bname, bidno, bcost)
				library.append(book)
				print"Book successfully registered!"

			elif choice == 3:
				print "Borrowing a book: "
				sname = raw_input("Enter student name: ")
				sidno = raw_input("Enter student ID number: ")
				lname= raw_input("Enter Librarian name: ")
				lidno= raw_input("Enter Librarian ID number: ")
				bname= raw_input("Which book would you like to borrow? ")
				bidno= raw_input("Enter ID number of book: ")
				studentx = Student(sname, sidno, my_bag=[])
				librarian=Librarian(lname, lidno, books_lent=[],library=[])	
				library=[]
				books_lent=[]
				my_bag=[]	
				library.remove(book)
				books_lent.append(book)
				my_bag.append(book)
				print (my_bag[0])

			elif choice ==7:
				break

			else:
				print "invalid Selection!"

System()

