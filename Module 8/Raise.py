import re

class User:
	def __init__(self):
		try:
			self.name = input("What's your name? \n").capitalize()
			self.surname = input("What's your surname? \n").capitalize()
			self.email = input("Specify your email address: \n")
			self.password = input("Password: \n")
		except Exception:


	def validate_email(self, email):
		if re.match(r"^[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$", email):
			raise Exception('Invalid email address')

	# def register_user(self):
	# 	# Вызов метода регистрации из родительского класса
	# 	self.register(self.name, self.surname, self.email, self.password)

print(f"{' Welcome to registration form ':*^100}\n"
		f"{' In order to register on our website, please provide following information: ':*^100}")
user1 = User()
print(user1.name)




