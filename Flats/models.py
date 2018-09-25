from django.db import models
from django.contrib.auth.models import User
from General.general import getHash

# Create your models here.
class Flat(models.Model):
	'''The basic linking of the user model and the flats'''
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class FlatDetails(models.Model):
	'''This is a seperate table as the details can be comfortably increased in future'''
	LOCATION_CHOICES = (
		('Mumbai', 'Mumbai'), 
		('Pune', 'Pune'), 
		('Nashik', 'Nashik'), 
		) 
	location = models.CharField(max_length=30, choices=LOCATION_CHOICES)
	hash = models.CharField(max_length=6)
	rent =  models.IntegerField()

	def save(self, *args, **kwargs):
		hash = getHash(6)
		while any(hash == x.hash for x in FlatDetails.objects.all()):
			hash = getHash(6)

		self.hash = hash
		super().save(args, kwargs)

