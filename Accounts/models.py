from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# A model is basically a db table written as a simple programming class
# we have extended the default django User model, so that we can add fields 
# in future.

class Pgcorp_user(User):
	pass
