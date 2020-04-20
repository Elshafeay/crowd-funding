from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractUser
)
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
	"""
	Custom user model manager where email is the unique identifiers
	for authentication instead of usernames.
	"""
	def create_user(self, email, password, **extra_fields):
		"""
			Create and save a User with the given email and password.
		"""
		if not email:
			raise ValueError(_('The Email must be set'))
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password, **extra_fields):
		"""
		Create and save a SuperUser with the given email and password.
		"""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError(_('Superuser must have is_staff=True.'))
		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_('Superuser must have is_superuser=True.'))
		return self.create_user(email, password, **extra_fields)


class UserModel(AbstractUser):
	first_name = models.CharField(_('first name'), max_length=30)
	last_name = models.CharField(_('last name'), max_length=30, blank=True)
	email = models.EmailField(_('email address'), unique=True)
	country = models.CharField(max_length=50, null=True, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	facebook_profile = models.CharField(max_length=50, null=True, blank=True)
	avatar = models.ImageField(upload_to='users/avatars', default='users/avatar.png')
	phone = models.CharField(max_length=14)

	username = None
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	objects = UserManager()

	def __str__(self):
		return self.get_full_name()
