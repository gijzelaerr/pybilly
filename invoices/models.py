from django.db import models
from django.contrib.auth.models import User
import settings


class Product(models.Model):
    CYCLE_CHOICES = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Montly'),
        ('Q', 'Quarterly'),
        ('Y', 'Yearly'),
    )
    cycle = models.CharField(max_length=1, choices=CYCLE_CHOICES)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __unicode__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s (%s)" % (self.user.username,
            self.product.name)


class Invoice(models.Model):
    subscription = models.ForeignKey(Subscription)
    paid = models.BooleanField(default=False)
    date = models.DateField()

    def __unicode__(self):
        return "%s (%s %s)" % (
                self.subscription.product.name,
                self.subscription.user.username,
                self.date.strftime("%B %Y")
        )


