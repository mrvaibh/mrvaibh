from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=10)
	dob = models.DateField(null=True, blank=True)
	gender = models.CharField(max_length=50)
	website = models.URLField(default='', blank=True)
	bio = models.TextField(default='')
	is_verified = models.BooleanField(default=False)
	following = models.ManyToManyField(User, related_name='followings', blank=True)
	followers = models.ManyToManyField(User, related_name='followers', blank=True)
	user_img = models.ImageField(upload_to='user/img', blank=True, default='user/img/default.png')

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)