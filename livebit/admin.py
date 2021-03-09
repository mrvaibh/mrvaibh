from django.contrib import admin
from livebit.models import Post, PostTag

# Register your models here.

admin.site.register(Post)
# admin.site.register(PostLike)
admin.site.register(PostTag)
# admin.site.register(Friend)