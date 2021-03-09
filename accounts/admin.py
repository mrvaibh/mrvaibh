from django.contrib import admin
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'id', 'phone', 'dob', 'gender', 'website', 'bio', 'is_verified', 'user_img']

	# def user_info(self, obj):
	# 	return obj.dob

	# Sorting order of data
	def get_queryset(self, request):
		queryset = super(UserProfileAdmin, self).get_queryset(request)
		queryset = queryset.order_by('id')
		return queryset

admin.site.register(UserProfile, UserProfileAdmin)

# admin.site.site_header = 'Mr. VaiBH Admin Page'
# admin.site.site_title = 'Mr. VaiBH'
