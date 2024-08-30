from django.db import models

# Create your models here.


class Buyer(models.Model):
	name = models.CharField(max_length=32)
	balance = models.DecimalField(max_digits=10, decimal_places=2)
	age = models.DecimalField(max_digits=3, decimal_places=0)

	def __str__(self):
		return self.name


class Game(models.Model):
	title = models.CharField(max_length=32)
	cost = models.DecimalField(max_digits=10, decimal_places=2)
	size = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.CharField(max_length=256)
	age_limited = models.BooleanField(default=False)
	buyer = models.ManyToManyField(Buyer, related_name='games', default=None)

	def __str__(self):
		return self.title