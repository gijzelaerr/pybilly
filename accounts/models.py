from django.db import models


class UserProfile(models.Model):
	user = models.OneToOneField(models.User)
	telephone = models.CharField(max_length=20)

