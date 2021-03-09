from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView
from .forms import HomeForm
from accounts.forms import UserProfileForm, EditProfileForm
from accounts.models import UserProfile
from .models import Post, PostTag
from django.contrib.auth.models import User
from django.template.loader import render_to_string

# Create your views here.

class HomeView(TemplateView):
	template_name = 'livebit/home.html'

	def get(self, request):
		form = HomeForm()
		users = User.objects.exclude(id=request.user.id)

		following = request.user.userprofile.following.all()
		followers = request.user.userprofile.followers.all()
		suggestions = users.difference(following)

		user_posts = Post.objects.filter(user__in=following)
		my_posts = Post.objects.filter(user=request.user)
		posts = user_posts.union(my_posts).order_by('-date_time')

		
		args = {'form':form, 'posts':posts, 'users':users, 'suggestions':suggestions}
		return render(request, self.template_name, args)

	def post(self, request):
		form = HomeForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()

			caption = form.cleaned_data['caption']
			location = form.cleaned_data['location']
			alt_text = form.cleaned_data['alt_text']
			post_img = form.cleaned_data['post_img']
			form = HomeForm()
			return redirect('/livebit')

		args = {'form': form, 'caption': caption, 'location': location, 'alt_text': alt_text, 'post_img': post_img}
		return render(request, self.template_name, args)

def profile(request, u=None):
	# View User Profile
	user = get_object_or_404(User, username=u)

	following = request.user.userprofile.following.all()
	followers = request.user.userprofile.followers.all()
	no_posts = Post.objects.filter(user=request.user).count()

	is_following = False
	if user in following:
		is_following = True
	else:
		is_following = False

	args = {'user': user, 'no_posts':no_posts, 'is_following':is_following}
	return render(request, 'livebit/profile.html', args)

def edit_profile(request):
	# Change User Profile
	if request.method == 'POST':
		edituser_form = EditProfileForm(request.POST, instance=request.user)
		editprofile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

		if edituser_form.is_valid() and editprofile_form.is_valid():
			edituser_form.save()
			editprofile_form.save()
			return redirect('/livebit/profile/edit/')
	else:
		edituser_form = EditProfileForm(instance=request.user)
		editprofile_form = UserProfileForm(instance=request.user.userprofile)

	args = {'edituser_form': edituser_form, 'editprofile_form': editprofile_form}
	return render(request, 'livebit/edit-profile.html', args)


def like_post(request):
	post = get_object_or_404(Post, id=request.POST.get('id'))
	print(post)

	user_posts = Post.objects.filter(user__in=following)
	my_posts = Post.objects.filter(user=request.user)
	posts = user_posts.union(my_posts).order_by('-date_time')

	is_liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.like.remove(request.user)
		is_liked = False
	else:
		post.likes.add(request.user)
		is_liked = True
	args = {'post':post, 'is_liked':is_liked, 'posts':posts}
	if request.is_ajax():
		html = render_to_string('livebit/like-section.html', args, request=request)
		return JsonResponse({'form':html})

def follow(request, id):
	userr = get_object_or_404(UserProfile, id=id)

	users = User.objects.exclude(id=request.user.id)
	following = request.user.userprofile.following.all()
	suggestions = users.difference(following)

	is_following = False
	if request.user.userprofile.following.filter(id=userr.id).exists():
		request.user.userprofile.following.remove(userr.user)
		is_following = False
	else:
		request.user.userprofile.following.add(userr.user)
		is_following = True

	if userr: args = {'is_following':is_following, 'userr':userr, 'users':users, 'suggestions':suggestions}
	else: {'is_following':is_following, 'users':users, 'suggestions':suggestions}

	if request.is_ajax():
		html = render_to_string('livebit/friend-list.html', args, request=request)
		return JsonResponse({'form':html})
	
	if request.POST.get('like_follow') == 'yes': return redirect(f'/livebit/')
	else: return redirect(f'/livebit/{userr}/')