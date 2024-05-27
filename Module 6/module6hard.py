from math import sqrt

class Figure:

	def __init__(self, color, sides, filled=False):
		self.sides_count = 0
		self.__sides = sides
		self.__color = color
		self.filled = filled

	def set_color(self, color):
		if self.__is_valid_color(color):
			self.__color = list(color)
		else:
			pass

	def get_color(self):
		return self.__color

	def __is_valid_color(self, color):
		if len(color) == len(self.__color):
			if all(0 < i <= 255 for i in color):
				return True
			else:
				return False
		else:
			return False

	def set_sides(self, *args):
		if self.__is_valid_sides(*args):
			self.__sides = list(args)
		else:
			pass

	def get_sides(self):
		return self.__sides

	def __is_valid_sides(self, *args):
		if len(args) == len(self.__sides):
			if any(i > 0 for i in args):
				return True
			else:
				return False
		else:
			return False

	def __len__(self):
		if hasattr(self, 'get_square'):
			return self.get_square()


class Circle(Figure):

	def __init__(self, color, side):
		super().__init__(color, side)
		self.sides_count = 1
		self.__radius = side / (2 * 3.14)

	def get_square(self):
		return int(3.14 * self.__radius ** 2)


class Triangle(Figure):
	def __init__(self, color, *sides):
		super().__init__(color, list(sides))
		self.sides_count = 3
		self.sides = sides
		self.__height = 2 * self.get_square() / sides[0]

	def get_square(self):
		p = sum(self.sides) / 2
		return int(sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])))


#
# class Cube:
# 	sides_count = 12


# Код для проверки:


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
# circle1.set_color((233, 100, 100))
# print(circle1.get_square())
# print(circle1.get_color())
print(len(circle1))
tr1 = Triangle((200, 200, 100), 10, 15, 20)
# print(tr1.get_sides())
tr1.set_sides(10, 55, 20, 30)
print(len(tr1))
# print(tr1._Figure__sides)
# Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# cube1.set_color(300, 70, 15) # Не изменится
# print(circle1.get_color())
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# circle1.set_sides(15) # Изменится
# print(cube1.get_sides())
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())