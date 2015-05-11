from django.db import models

# Create your models here.
class Staff(models.Model):
	name = models.CharField(max_length=20)
	password = models.CharField(max_length=10)
	emp_id = models.IntegerField(unique = True)
	email_id = models.CharField(max_length=30)
	phone = models.IntegerField()
	dob = models.IntegerField()
	salary = models.IntegerField()

	def __unicode__(self):
		return self.name

class Login(models.Model):
	username = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=20)

	def __unicode__(self):
		return self.username

