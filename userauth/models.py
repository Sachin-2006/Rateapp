from django.contrib.auth.models import PermissionsMixin,UserManager,AbstractBaseUser
from django.db import models
from django.utils import timezone

class CustomUserManager(UserManager):
	def _create_user(self,email,password,**extra_fields):
		if not email:
			raise ValueError("Not a Vaild Email")
		email = self.normalize_email(email)
		user = self.model(email=email,**extra_fields)
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_user(self,email = None,password = None,**extra_fields):
		extra_fields.setdefault('is_staff',False)
		extra_fields.setdefault('is_superuser',False)
		return self._create_user(email,password,**extra_fields)

	def create_superuser(self,email = None,password = None,**extra_fields):
		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_superuser',True)
		return self._create_user(email,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
	name = models.CharField(max_length = 255,blank=True,default='')
	email = models.EmailField(blank = True,default ='',unique=  True)
	adm_num = models.IntegerField(null = True)

	is_active = models.BooleanField(default = True)
	is_superuser = models.BooleanField(default = False)
	is_staff = models.BooleanField(default = False)

	data_joined = models.DateTimeField(default = timezone.now)
	last_login  = models.DateTimeField(blank=True,null = True)

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name='User'
		verbose_name_plural = "Users"



class TeacherProfile(models.Model):
	name = models.CharField(max_length = 256)
	s_name = models.CharField(max_length = 8)
	Handling = models.CharField(max_length = 100)
	Rating = models.FloatField(default = 0)
