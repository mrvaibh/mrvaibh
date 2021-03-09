from django import forms
from livebit.models import Post

class HomeForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['caption', 'location', 'alt_text', 'post_img']
	caption = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Caption'}))
	location = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Location'}))
	alt_text = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Alt Text'}))
	post_img = forms.ImageField(label='', widget=forms.FileInput(attrs={'style':'border:none; outline:none;', 'hidden':'hidden'}))