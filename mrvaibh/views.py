from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import UserProfile
from accounts.forms import EditProfileForm, UserProfileForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')

@login_required
def profile(request, u=None):
	# View User Profile
	try:
		if u:
			user = User.objects.get(username=u)
		else:
			user = request.user
	except:
			return redirect(f'/{request.user}')

	following = request.user.userprofile.following.all()
	followers = request.user.userprofile.followers.all()

	is_following = False
	if user in following:
		is_following = True
	else:
		is_following = False

	args = {'user': user, 'is_following':is_following}
	return render(request, 'profile.html', args)


@login_required
def follow(request):
	user = get_object_or_404(UserProfile, id=request.POST.get('follow_id'))
	print(user)
	is_following = False
	if user.following.filter(id=request.user.id).exists():
		user.followers.remove(request.user)
		is_following = False
	else:
		user.following.add(request.user)
		is_following = True
	return redirect(f'/{user}')