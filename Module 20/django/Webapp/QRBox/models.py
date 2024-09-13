from django.db import models


class Customer(models.Model):
	email = models.EmailField(max_length=32, unique=True)
	name = models.CharField(max_length=32)
	password = models.CharField(max_length=256)
	USERNAME_FIELD = 'email'  # Поле для логина
	REQUIRED_FIELDS = ['name']  # Обязательные поля при создании суперпользователя

	@property
	def is_authenticated(self):
		return True  # Этот пользователь всегда считается аутентифицированным

	# Метод для имитации "анонимного" пользователя
	@property
	def is_anonymous(self):
		return False  # Этот пользователь никогда не считается анонимным

	def __str__(self):
		return self.name


class QRCodes(models.Model):
	qrcode = models.BinaryField()
	user_id = models.DecimalField(max_digits=10, decimal_places=0)
	q_name = models.CharField(max_length=256)
	user = models.ManyToManyField(Customer, related_name='codes', default=None)

	def __str__(self):
		return self.qrcode
