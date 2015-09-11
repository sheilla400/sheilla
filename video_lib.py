
movies_list=[]
class Customer(object):
	def __init__(self, customer_name, borrow_days, customer_pile=[]):
		self.customer_name=customer_name
		self.borrow_days=borrow_days
		self.customer_pile=customer_pile


class Movie(object):
	def __init__(self, name, category, price):
		self.name=name
		self.category=category
		self.price=price



class Video_System(object):
	if __name__ == "__main__":
		while True:
			print "  "
			print "MENU"
			print "1.Add movie to library."
			print "2.Borrow a movie."
			print "3.Return a movie."
			print "4.Exit"
			choice=raw_input("Select an option [1-4]: ")
			choice=int(choice)

			if choice == 1:
				print "Registering a movie.."
				name=raw_input("Enter movie name: ")
				print "Movie category options are: "
				print "1.New release 2.Regular 3.Children  "
				category=int(raw_input("Enter movie category code[1-3]: "))
				while True:
					if int(category) == 1:
						price = 1000
						break
					elif int(category) == 2:
						price = 500
						break
					elif int(category) == 3:
						price = 300
						break
					else:
						print "Invalid selection! Select again:"
						category=int(raw_input("Enter movie category code[1-3]: "))

				m=Movie(name, category, price)
				movies_list.append(m)

				print "Movie successfully added!"

			elif choice == 2:
				#print (m.name for m in movies_list)
				#movies_list=['LionKing', 'Matilda', 'Expendables']
				customer_name=raw_input("Customer name: ")
				movie_to_borrow=raw_input("Enter movie to be borrowed: ")
				borrow_days=raw_input("Number of days to borrow movie: ")
				customer = Customer(customer_name, borrow_days, customer_pile=[])
				customer_pile=[]
				customer_pile.append(movie_to_borrow)

				if movie_to_borrow in movies_list:
					print "you have borrowed "+movie_to_borrow+"for "+borrow_days+"days at ush."+price

				else:
					print "Sorry!We do not have the movie."

			elif choice == 4:
				break

			else:
				print "Invalid selection, please select again: "
Video_System()