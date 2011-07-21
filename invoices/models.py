import datetime
from django.db import models
from django.contrib.auth.models import User
import settings

def beginning_of_month(moment=datetime.datetime.today()):
    return datetime.datetime(year=moment.year, month=moment.month, day=1).date()


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
    user = models.ForeignKey(User, related_name='subscriptions')
    product = models.ForeignKey(Product, related_name='subscriptions')
    start = models.DateField(default=beginning_of_month())
    end = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s (%s)" % (self.user.username,
            self.product.name)

    class Meta:
        unique_together = (("user", "product"),)


class Invoice(models.Model):
    subscription = models.ForeignKey(Subscription, related_name='invoices')
    paid = models.BooleanField(default=False)
    date = models.DateField()

    class Meta:
        unique_together = (("subscription", "date"),)

    def __unicode__(self):
        return "%s (%s %s)" % (
                self.subscription.product.name,
                self.subscription.user.username,
                self.date.strftime("%B %Y")
        )


