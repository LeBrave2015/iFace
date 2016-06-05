from django import forms
from .models import Post
from .models import Photo

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('title', 'text')

class ImageForm(forms.ModelForm):
	class Meta:
		model=Photo
		fields=('image',)
