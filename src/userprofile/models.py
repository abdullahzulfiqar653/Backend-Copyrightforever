from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class CustomerProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=21, default='')
	address = models.TextField(default='')
	state = models.CharField(max_length=50, default='')
	postcode = models.CharField(max_length=11, default='')

