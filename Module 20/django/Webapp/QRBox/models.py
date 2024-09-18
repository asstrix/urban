from django.db import models


class Customer(models.Model):
	email = models.EmailField(max_length=32, unique=True)
	name = models.CharField(max_length=32)
	password = models.CharField(max_length=256)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	@property
	def is_authenticated(self):
		return True

	# Anonymous user, else django will throw error as the model is custom
	@property
	def is_anonymous(self):
		return False

	def __str__(self):
		return self.name


class QRCodes(models.Model):
	qrcode = models.BinaryField()
	user_id = models.DecimalField(max_digits=10, decimal_places=0)
	q_name = models.CharField(max_length=256)
	user = models.ManyToManyField(Customer, related_name='codes', default=None)

	def __str__(self):
		return self.qrcode
