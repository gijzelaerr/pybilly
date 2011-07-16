from django.db import models
from django.contrib.auth.models import User


class Invoice(models.Model):
	user = models.ForeignKey(User)
	amount = models.IntegerField()
	paid = models.BooleanField(default=False)
	date = models.DateField()
	description = models.CharField(max_length=100)
	notes = models.CharField(max_length=500)


class Product(models.Model):
	CYCLE_CHOICES = (
		('D', 'Daily'),
		('W', 'Weekly'),
		('M', 'Montly'),
		('Q', 'Quarterly'),
		('Y', 'Yearly'),
	)
	cycle = models.CharField(max_length=1, choices=CYCLE_CHOICES)
	description = models.CharField(max_length=100)


class Subscription(models.Model):
	user = models.ForeignKey(User)
	product = models.ForeignKey(Product)
	start = models.DateField()
	end = models.DateField()
	active = models.BooleanField(default=True)

