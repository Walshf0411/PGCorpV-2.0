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
	location = models.CharField(max_length=30)
	title = models.CharField(max_length=30, default="default")
	hash = models.CharField(max_length=6)
	rent =  models.IntegerField(validators=(MinValueValidator(limit_value=200), ))
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

