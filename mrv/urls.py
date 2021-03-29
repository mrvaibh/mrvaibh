from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.index, name="mrvhome"),
	path('features', views.features, name="mrvfeatures"),
	path('pricing', views.pricing, name="mrvpricing"),
	path('blog-list', views.blog_list, name="mrvblog-list"),
	path('about', views.about, name="mrvabout"),
	path('contact', views.contact, name="mrvcontact"),
	path('wiki', views.wiki),
	path('vaibhav-shukla', views.vaibhav_shukla),
	path('gen', views.gen),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
