class Car:
	price = 1000000

	def horse_powers(self):
		return 150


class Nissan(Car):
	price = 2000000

	def horse_powers(self):
		return 250


class Kia(Car):
	price = 3000000

	def horse_powers(self):
		return 350


juke = Nissan()
print(juke.price, juke.horse_powers())
stinger = Kia()
print(stinger.price, stinger.horse_powers())