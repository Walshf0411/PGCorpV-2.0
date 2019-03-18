from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
# A model is basically a db table written as a simple programming class
# we have extended the default django User model, so that we can add fields 
# in future.
class User_Type:
	HOUSE_OWNER = 1
	PAYING_GUEST = 2

	def user_type_string(self, user_type):
		user_type = int(user_type)
		if user_type == User_Type.HOUSE_OWNER:
			user_type = "House Owner"
		elif user_type == User_Type.PAYING_GUEST:
			user_type = "Paying Gues"

		return user_type
	

USER_TYPE_CHOICES = (
	(User_Type.HOUSE_OWNER, 'House Owner'),
	(User_Type.PAYING_GUEST, 'Paying Guest') 
)


class Pgcorp_user(User):
	'''
		A model that has the extra details for a user.
	'''
	def save_to_profile_pic(self):
		return os.path.join("profile_images", self.username)

	user_type = models.IntegerField(choices=USER_TYPE_CHOICES)
	profile_pic = models.ImageField(upload_to=save_to_profile_pic, blank=True, null=True)