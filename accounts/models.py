from django.db import models



# Create your models here.




class Customer(models.Model):
	name = models.CharField("Name",max_length=50)
	email = models.EmailField("Email")
	phone = models.CharField('Phone',max_length=50)
	image = models.ImageField("Image")
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self) -> str:
		return self.name