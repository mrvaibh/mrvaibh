from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
	first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'First Name','autofocus':'true'}))
	last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Username'}))
	email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'Email'}))
	password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))


class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'is_active']

	password = None

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [
		'phone',
		'dob',
		'gender',
		'website',
		'bio',
		'user_img'
		]

	phone = forms.CharField(widget=forms.TextInput(attrs={'class':'col-5'}))
	dob = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date', 'class':'col-5', 'autocomplete':'off'}))
	gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], widget=forms.RadioSelect(attrs={'class':'btn btn-primary btn-sm', 'data-toggle': 'gender'}))
	bio = forms.CharField(widget=forms.Textarea(attrs={'rows':'4', 'maxlength':'150'}))
	user_img = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'image', 'style':'display:none;'}))

# class LoginForm(AuthenticationForm):
# 	class Meta:
# 		model = User
# 		fields = ['username', 'password']

# 	username = forms.CharField(widget=forms.TextInput(attrs={'class':'input--style-4'}))
# 	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input--style-4'}))