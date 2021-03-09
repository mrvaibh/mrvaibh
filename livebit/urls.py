from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView
from livebit import views

app_name = "livebit"
urlpatterns = [
	path('', HomeView.as_view(), name="home"),
	path('<u>/', views.profile, name="profile"),
	path('like/', views.like_post , name="like_post"),
	path('follow/<id>', views.follow , name="follow"),
	path('profile/edit/', views.edit_profile , name="edit_profile"),
	# path('connect/<operation>/<int:pk>', views.change_friends , name="change_friends"),
	path('explore/', HomeView.as_view(), name="explore"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)