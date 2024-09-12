from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.hashers import make_password


class Manager(BaseUserManager):
	def create_user(self, email, name, password=None):
		if not email:
			raise ValueError("Users must have an email address")
		user = self.model(
			email=self.normalize_email(email),
			name=name,
		)
		user.set_password(password)  # Хеширование пароля
		user.save(using=self._db)
		return user

	def create_superuser(self, email, name, password):
		user = self.create_user(
			email=email,
			name=name,
			password=password,
		)
		user.is_admin = True
		user.save(using=self._db)
		return user


class Customer(AbstractBaseUser):
	email = models.EmailField(max_length=32, unique=True)
	name = models.CharField(max_length=32)
	password = models.CharField(max_length=256)

	objects = Manager()

	USERNAME_FIELD = 'email'  # Поле для логина
	REQUIRED_FIELDS = ['name']  # Поля, которые будут запрашиваться при создании суперпользователя

	def __str__(self):
		return self.name

	def set_password(self, raw_password):
		self.password = make_password(raw_password)

	def check_password(self, raw_password):
		return self.check_password(raw_password)


class QRCodes(models.Model):
	qrcode = models.BinaryField()
	user_id = models.DecimalField(max_digits=10, decimal_places=0)
	user = models.ManyToManyField(Customer, related_name='codes', default=None)

	def __str__(self):
		return self.qrcode
