from django.db import models
from django.contrib.auth.models import User
from General.general import getHash
from django.utils.text import slugify
from django.core.validators import MinValueValidator
# Create your models here.


class FlatDetails(models.Model):
	'''This is a seperate table as the details can be comfortably increased in future'''
	# The id of the flat for which we have to store the details
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	address = models.CharField(max_length=150)
	description = models.CharField(max_length=200)
	total_space = models.IntegerField(validators=(MinValueValidator(limit_value=50), ))
	total_rent = models.IntegerField(validators=(MinValueValidator(limit_value=200), ))
	deposit = models.CharField(max_length=10)
	possession = models.CharField(max_length=20)
	total_rooms = models.IntegerField(validators=(MinValueValidator(limit_value=1), ))
	property_type = models.CharField(max_length=30)
	floor = models.CharField(max_length=4)
	parking_options = models.CharField(max_length=30, default="No Parking")
	number_of_guests = models.IntegerField(validators=(MinValueValidator(limit_value=1), ))
	hash = models.CharField(max_length=6)
	slug = models.SlugField(null=True)
	date_of_posting = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		hash = getHash(6)
		while any(hash == x.hash for x in FlatDetails.objects.all()):
			hash = getHash(6)

		self.hash = hash
		self.slug = slugify(self.title)
		super().save(args, kwargs)

	def get_absolute_url(self):
		base_url = "/flats/{}/{}/"  # flats/<hash>/<slug>/
		return base_url.format(self.hash, self.slug)


class FavouriteFlats(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	flat = models.ForeignKey(FlatDetails, on_delete=models.CASCADE)


class FlatApplication(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	flat = models.ForeignKey(FlatDetails, on_delete=models.CASCADE)
	allowed_user = models.BooleanField(default=False)