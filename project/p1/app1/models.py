from django.db import models

# Create your models here.
class student(models.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=100)
	
		