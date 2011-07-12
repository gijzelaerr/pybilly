from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=8)
    email = models.EmailField()
	telephone = model.CharField(max_length=20)

