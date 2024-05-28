class Figure:

	def __init__(self, color, sides, sides_count, subclass, filled=False):
		self.sides_count = sides_count
		self.subclass = subclass
		self.__sides = self.__set_initial_sides(sides)
		self.__color = color
		self.filled = filled

	def __set_initial_sides(self, sides):
		if self.__is_valid_sides(list(sides)):
			if self.subclass == 'Triangle':
				return list(sides)
			else:
				return [sides[0] for i in range(self.sides_count)]
		else:
			return [1 for i in range(self.sides_count)]

	def set_sides(self, *sides):
		if self.__is_valid_sides(sides):
			if self.subclass == 'Triangle':
				self.__sides = list(sides)
			else:
				self.__sides = [sides[0] for i in range(self.sides_count)]

	def get_sides(self):
		return self.__sides

	def __is_valid_sides(self, sides):
		if self.subclass == 'Cube':
			if len(sides) == 1 and all(i > 0 for i in sides):
				return True
			else:
				return False
		else:
			if len(sides) == self.sides_count and all(i > 0 for i in sides):
				return True
			else:
				return False

	def set_color(self, *color):
		if self.__is_valid_color(color):
			self.__color = list(color)
		else:
			pass

	def get_color(self):
		return self.__color

	def __is_valid_color(self, color):
		if len(color) == 3 and all(0 < i <= 255 for i in color):
			return True
		else:
			return False

	def __len__(self):
		if self.subclass == 'Circle':
			return self.__sides[0]
		if self.subclass == 'Triangle':
			return sum(self.__sides)
		if self.subclass == 'Cube':
			return sum(self.__sides)


class Circle(Figure):
	def __init__(self, color, *sides):
		super().__init__(color, sides, subclass='Circle', sides_count=1)
		self.__radius = super().get_sides()[0] / (2 * 3.14)

	def get_square(self):
		return int(3.14 * self.__radius ** 2)


class Triangle(Figure):
	def __init__(self, color, *sides):
		super().__init__(color, sides, subclass='Triangle', sides_count=3)
		self.__height = 2 * self.get_square() / sides[0]

	def get_square(self):
		from math import sqrt
		p = sum(self.get_sides()) / 2
		return int(sqrt(p * (p - super().get_sides()[0]) * (p - super().get_sides()[1]) * (p - super().get_sides()[2])))


class Cube(Figure):
	def __init__(self, color, *sides):
		super().__init__(color, sides, subclass='Cube', sides_count=12)

	def get_volume(self):
		return self.get_sides()[0] ** 3

# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())