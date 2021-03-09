from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(User, related_name='post_owner', on_delete=models.CASCADE)
	caption = models.CharField(max_length=300, null=True)
	location = models.CharField(max_length=50, null=True)
	alt_text = models.CharField(max_length=50, null=True)
	likes = models.ManyToManyField(User, related_name='like_post', blank=True)
	date_time = models.DateTimeField(default=timezone.now(), null=False)
	post_img = models.ImageField(upload_to='post/img', blank=False)

	def __str__(self):
		return str(self.id)


class PostTag(models.Model):
	post = models.ForeignKey(Post, related_name='post_tag', on_delete=models.CASCADE)
	coords = models.CharField(max_length=20)
	tagged_user = models.ManyToManyField(User)
	tagged_by = models.ForeignKey(User, related_name='post_tagger', on_delete=models.CASCADE)


# class Friend(models.Model):
# 	users = models.ManyToManyField(User)
# 	current_user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)

# 	@classmethod
# 	def make_friend(cls, current_user, new_friend):
# 		friend, created = cls.objects.get_or_create(current_user=current_user)
# 		friend.users.add(current_user, new_friend)

# 	@classmethod
# 	def lose_friend(cls, current_user, new_friend):
# 		friend, created = cls.objects.get_or_create(current_user=current_user)
# 		friend.users.remove(current_user, new_friend)

# 	def __str__(self):
# 		return str(self.current_user)