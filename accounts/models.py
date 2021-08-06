from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.
class User(AbstractUser):

    email = models.EmailField('Email',unique=True)
    image = models.ImageField("Image 40x40 ",upload_to='profile_images',null=True)
    username = models.CharField('Username', max_length=50,unique=True)
    create = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    update = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)


    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS = ['email','create','read','update','delete']

    def __str__(self) -> str:
        return self.username

    



class Customer(models.Model):
	name = models.CharField("Name",max_length=50)
	email = models.EmailField("Email",unique=True)
	phone = models.CharField('Phone',max_length=50)
	image = models.ImageField("Image", upload_to='customer_image')
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self) -> str:
		return self.name