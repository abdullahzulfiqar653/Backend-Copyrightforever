from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserAccountManager(BaseUserManager):
	def create_user(self, email, name, password=None):
		if not email:
			raise ValueError("User must have an email address to register")
		user = self.model(email=self.normalize_email(email), name=name)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, name, password):
		if password is None:
			raise TypeError("super user must have an password")
		user = self.create_user(email, name, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=250, unique=True)
	name = models.CharField(max_length=250,)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserAccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.name

	def __int__(self):
		return self.email

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	from userprofile.models import CustomerProfile
	if created:
		CustomerProfile.objects.create(user=instance)