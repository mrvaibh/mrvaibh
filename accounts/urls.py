from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"
urlpatterns = [
	path('register/', views.register, name="register"),
	path('login/', LoginView.as_view(template_name='accounts/login.html')),
	path('edit/', views.edit_profile, name="edit_profile"),
	path('change-password/', views.change_password, name="change_password"),
	path('reset-password/', PasswordResetView.as_view(template_name='accounts/password_reset_form.html')),
	path('reset-password/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html')),
	path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html')),
	path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html')),
	path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
	path('livebit/', views.livebit),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
