class Vehicle:
	vehicle_type = None


class Car:
	price = 1000000

	def horse_powers(self):
		return 100


class Nissan(Vehicle, Car):
	vehicle_type = 'sedan'
	price = 2000000

	def horse_powers(self):
		return 200


spectra = Nissan()
print(spectra.vehicle_type, spectra.price)