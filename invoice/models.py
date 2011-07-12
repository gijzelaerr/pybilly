from django.db import models
from client.models import Client


class Invoice(models.Model):
	client = models.ForeignKey(Client)
	amount = models.IntegerField()
	paid = models.BooleanField(default=False)
	date = models.DateField()
	description = models.CharField()
	notes = models.CharField()


class Product(models.Model):
	CYCLE_CHOICES = (
		('D', 'Daily'),
		('W', 'Weekly'),
		('M', 'Montly'),
		('Q', 'Quarterly'),
		('Y', 'Yearly'),
	)
	cycle = models.CharField(max_length=1, choices=CYCLE_CHOICES)


class Subscription(models.Model):
	client = models.ForeignKey(Client)
	product = models.ForeignKey(Product)
	start = models.DateField()
	end = models.DateField()
	active = models.BooleanField(default=True)

	
