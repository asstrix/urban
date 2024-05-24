class Figure:
	sides_count = 0

	def __init__(self, sides, color, filled):
		self.__sides = sides
		self.__color = color
		self.filled = filled

	def get_color(self):
		pass

	def __is_valid_color(self, r, g, b):
		pass

	def set_color(self, r, g, b):
		pass

	def set_sides(self, *args):
		pass

	def __is_valid_sides(self, *args):
		pass

	def __len__(self):
		pass


class Circle(Figure):
	sides_count = 1

	def __init__(self):
		self.__radius = 0

	def get_square(self):
		pass


class Triangle:
	sides_count = 3


class Cube:
	sides_count = 12