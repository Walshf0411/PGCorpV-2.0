from django.db import models
from django.contrib.auth.models import User
from General.general import getHash
from django.utils.text import slugify

# Create your models here.
class Flat(models.Model):
	'''The basic linking of the user model and the flats'''
	# The user the flat is posted by.
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class FlatDetails(models.Model):
	'''This is a seperate table as the details can be comfortably increased in future'''
	# The id of the flat for which we have to store the details
	flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
	LOCATION_CHOICES = (
		('Mumbai', 'Mumbai'), 
		('Pune', 'Pune'), 
		('Nashik', 'Nashik'), 
		) 
	location = models.CharField(max_length=30, choices=LOCATION_CHOICES)
	title = models.CharField(max_length=30, default="default")
	hash = models.CharField(max_length=6)
	rent =  models.IntegerField()
	slug = models.SlugField(null=True) 

	def save(self, *args, **kwargs):
		hash = getHash(6)
		while any(hash == x.hash for x in FlatDetails.objects.all()):
			hash = getHash(6)

		self.hash = hash
		self.slug = slugify(self.title)
		super().save(args, kwargs)

	def get_absolute_url(self):
		base_url = "/flats/{}/{}/" # flats/<hash>/<slug>/
		return base_url.format(self.hash, self.slug)

