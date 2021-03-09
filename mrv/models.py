from django.db import models

# Create your models here.

class Fact(models.Model):
	fact_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=5000)
	fact = models.CharField(max_length=5000)
	fact_img = models.ImageField(upload_to='fact/img')

class Service(models.Model):
	service_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=70)
	url = models.TextField(default="")
	description = models.CharField(max_length=500)
	service_img = models.ImageField(upload_to='service/img')