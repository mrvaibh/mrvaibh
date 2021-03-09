from django.shortcuts import render, redirect
from mrv.models import Service
from .forms import RegistrationForm, EditProfileForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			form = RegistrationForm()
			return redirect('/mrv')
	else:
		form = RegistrationForm()

	args = {'form': form}
	return render(request, 'accounts/registration.html', args)

@login_required
def edit_profile(request):
	service, service_count = Service.objects.all(), Service.objects.all().count()

	# Change User Profile
	if request.method == 'POST':
		edituser_form = EditProfileForm(request.POST, instance=request.user)
		editprofile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

		if edituser_form.is_valid() and editprofile_form.is_valid():
			edituser_form.save()
			editprofile_form.save()
			return redirect('/accounts/edit')
	else:
		edituser_form = EditProfileForm(instance=request.user)
		editprofile_form = UserProfileForm(instance=request.user.userprofile)

	args = {'edituser_form': edituser_form, 'editprofile_form': editprofile_form, 'service':service, 'service_count':service_count}
	return render(request, 'accounts/edit-profile.html', args)


@login_required
def change_password(request):
	user = request.user		
	if user.userprofile.user_img == '':
		user.userprofile.user_img = '/user/img/default.png'

	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/mrv')
	else:
		form = PasswordChangeForm(user=request.user)
	args = {'form': form}
	return render(request, 'accounts/change_password.html', args)

def livebit(request):
	return render(request, 'accounts/livebit.html')